const THEME_KEY = 'theme';
const DEFAULT_THEME = 'system';

/**
 * Reads the stored theme preference from localStorage.
 * Returns "system" if localStorage is unavailable or no value is stored.
 */
export function getTheme(): string {
  try {
    return localStorage.getItem(THEME_KEY) ?? DEFAULT_THEME;
  } catch {
    return DEFAULT_THEME;
  }
}

/**
 * Writes the theme preference to localStorage.
 * Silently fails if localStorage is unavailable (e.g., private browsing).
 */
export function setTheme(theme: string): void {
  try {
    localStorage.setItem(THEME_KEY, theme);
  } catch {
    // localStorage unavailable — ignore
  }
}

/**
 * Resolves a theme value to either "light" or "dark".
 * For "system", checks the OS preference via the prefers-color-scheme media query.
 * For explicit "light" or "dark", returns the value directly.
 * Any unrecognized value is treated as "system" and resolved via the media query.
 */
export function resolveTheme(theme: string): 'light' | 'dark' {
  if (theme === 'light') return 'light';
  if (theme === 'dark') return 'dark';

  // "system" or any unrecognized value — resolve from OS preference
  if (typeof window !== 'undefined' && window.matchMedia) {
    return window.matchMedia('(prefers-color-scheme: dark)').matches
      ? 'dark'
      : 'light';
  }

  // Fallback when matchMedia is unavailable (e.g., SSR / Node)
  return 'light';
}
