import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import fc from 'fast-check';
import { getTheme, setTheme, resolveTheme } from './theme.ts';

/**
 * Mock localStorage for Node/Vitest environment.
 */
function createMockLocalStorage(): Storage {
  const store = new Map<string, string>();
  return {
    getItem: (key: string) => store.get(key) ?? null,
    setItem: (key: string, value: string) => { store.set(key, value); },
    removeItem: (key: string) => { store.delete(key); },
    clear: () => { store.clear(); },
    get length() { return store.size; },
    key: (index: number) => [...store.keys()][index] ?? null,
  };
}

/**
 * Mock matchMedia for Node/Vitest environment.
 * Returns a function matching the window.matchMedia signature.
 */
function createMockMatchMedia(prefersDark: boolean) {
  return (query: string): MediaQueryList => ({
    matches: query === '(prefers-color-scheme: dark)' ? prefersDark : false,
    media: query,
    onchange: null,
    addListener: () => {},
    removeListener: () => {},
    addEventListener: () => {},
    removeEventListener: () => {},
    dispatchEvent: () => false,
  });
}

/**
 * Sets up the global mocks needed by theme.ts (localStorage + window.matchMedia).
 */
function setupGlobals(prefersDark: boolean) {
  vi.stubGlobal('localStorage', createMockLocalStorage());
  vi.stubGlobal('matchMedia', createMockMatchMedia(prefersDark));

  // Ensure window exists and has matchMedia, since resolveTheme checks
  // `typeof window !== 'undefined' && window.matchMedia`
  if (typeof globalThis.window === 'undefined') {
    vi.stubGlobal('window', globalThis);
  }
  (globalThis as any).window.matchMedia = createMockMatchMedia(prefersDark);
}

describe('Property Tests: Theme System', () => {
  beforeEach(() => {
    setupGlobals(false);
  });

  afterEach(() => {
    vi.unstubAllGlobals();
  });

  /**
   * Property 6: Theme persistence round-trip
   * Validates: Requirements 7.5
   *
   * For any valid theme value ("light", "dark", or "system"), storing the
   * value via setTheme() and then retrieving it via getTheme() returns the
   * original value. The resolved DOM theme attribute (resolveTheme) always
   * returns either "light" or "dark" (never "system").
   */
  describe('Property 6: Theme persistence round-trip', () => {
    it('setTheme then getTheme returns the original value', () => {
      const themeArb = fc.constantFrom('light', 'dark', 'system');

      fc.assert(
        fc.property(themeArb, (theme) => {
          setTheme(theme);
          const retrieved = getTheme();
          expect(retrieved).toBe(theme);
        }),
        { numRuns: 100 },
      );
    });

    it('resolveTheme never returns "system"', () => {
      const themeArb = fc.constantFrom('light', 'dark', 'system');
      const prefersDarkArb = fc.boolean();

      fc.assert(
        fc.property(themeArb, prefersDarkArb, (theme, prefersDark) => {
          // Reconfigure matchMedia for this iteration
          (globalThis as any).window.matchMedia = createMockMatchMedia(prefersDark);

          const resolved = resolveTheme(theme);
          expect(resolved).not.toBe('system');
          expect(['light', 'dark']).toContain(resolved);
        }),
        { numRuns: 100 },
      );
    });
  });
});
