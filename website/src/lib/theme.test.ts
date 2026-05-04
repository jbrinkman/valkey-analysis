import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import { getTheme, setTheme, resolveTheme } from './theme.ts';

/**
 * Unit tests for theme logic.
 * Validates: Requirements 7.1, 7.2, 7.3, 7.5
 */

/** Creates an in-memory localStorage mock. */
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

/** Creates a matchMedia mock that returns the given dark-mode preference. */
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

/** Stubs localStorage and window.matchMedia for the theme module. */
function setupGlobals(prefersDark: boolean) {
  vi.stubGlobal('localStorage', createMockLocalStorage());
  vi.stubGlobal('matchMedia', createMockMatchMedia(prefersDark));

  if (typeof globalThis.window === 'undefined') {
    vi.stubGlobal('window', globalThis);
  }
  (globalThis as any).window.matchMedia = createMockMatchMedia(prefersDark);
}

describe('Theme Logic', () => {
  afterEach(() => {
    vi.unstubAllGlobals();
  });

  describe('getTheme()', () => {
    it('returns "system" when localStorage is empty', () => {
      setupGlobals(false);
      expect(getTheme()).toBe('system');
    });

    it('returns the stored value when localStorage has a theme', () => {
      setupGlobals(false);
      localStorage.setItem('theme', 'dark');
      expect(getTheme()).toBe('dark');
    });
  });

  describe('setTheme()', () => {
    it('writes "dark" to localStorage', () => {
      setupGlobals(false);
      setTheme('dark');
      expect(localStorage.getItem('theme')).toBe('dark');
    });

    it('writes "light" to localStorage', () => {
      setupGlobals(false);
      setTheme('light');
      expect(localStorage.getItem('theme')).toBe('light');
    });

    it('writes "system" to localStorage', () => {
      setupGlobals(false);
      setTheme('system');
      expect(localStorage.getItem('theme')).toBe('system');
    });

    it('overwrites a previously stored theme', () => {
      setupGlobals(false);
      setTheme('dark');
      setTheme('light');
      expect(localStorage.getItem('theme')).toBe('light');
    });
  });

  describe('resolveTheme()', () => {
    it('returns "dark" for "system" when OS prefers dark', () => {
      setupGlobals(true);
      expect(resolveTheme('system')).toBe('dark');
    });

    it('returns "light" for "system" when OS prefers light', () => {
      setupGlobals(false);
      expect(resolveTheme('system')).toBe('light');
    });

    it('returns "light" for explicit "light" regardless of OS preference', () => {
      setupGlobals(true);
      expect(resolveTheme('light')).toBe('light');
    });

    it('returns "dark" for explicit "dark" regardless of OS preference', () => {
      setupGlobals(false);
      expect(resolveTheme('dark')).toBe('dark');
    });

    it('resolves unrecognized values via OS preference (like "system")', () => {
      setupGlobals(true);
      expect(resolveTheme('unknown')).toBe('dark');
    });
  });

  describe('localStorage error handling', () => {
    it('getTheme returns "system" when localStorage.getItem throws', () => {
      const throwingStorage = {
        getItem: () => { throw new Error('SecurityError'); },
        setItem: () => { throw new Error('SecurityError'); },
        removeItem: () => {},
        clear: () => {},
        length: 0,
        key: () => null,
      } as Storage;
      vi.stubGlobal('localStorage', throwingStorage);

      expect(getTheme()).toBe('system');
    });

    it('setTheme does not throw when localStorage.setItem throws', () => {
      const throwingStorage = {
        getItem: () => null,
        setItem: () => { throw new Error('QuotaExceededError'); },
        removeItem: () => {},
        clear: () => {},
        length: 0,
        key: () => null,
      } as Storage;
      vi.stubGlobal('localStorage', throwingStorage);

      expect(() => setTheme('dark')).not.toThrow();
    });
  });
});
