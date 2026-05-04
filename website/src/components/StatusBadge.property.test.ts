import { describe, it, expect } from 'vitest';
import fc from 'fast-check';

/**
 * Pure rendering logic extracted from StatusBadge.astro for testability.
 * The Astro component renders:
 *   <span class={`badge badge--${status}`}>{status.charAt(0).toUpperCase() + status.slice(1)}</span>
 *
 * This function replicates that logic so we can property-test it without
 * needing an Astro rendering pipeline.
 */
function renderBadge(status: 'explicit' | 'implied' | 'none'): string {
  const cssClass = `badge badge--${status}`;
  const label = status.charAt(0).toUpperCase() + status.slice(1);
  return `<span class="${cssClass}">${label}</span>`;
}

describe('Property Tests: StatusBadge Rendering', () => {
  /**
   * Property 2: Status badge CSS class mapping
   * Validates: Requirements 2.4, 6.1, 6.2, 6.3
   *
   * For any valid Valkey_Support_Status value ("explicit", "implied", or "none"),
   * the status badge rendering function produces output containing a CSS class
   * that includes the status value, ensuring each status maps to a visually
   * distinct indicator.
   */
  describe('Property 2: Status badge CSS class mapping', () => {
    const statusArb = fc.constantFrom(
      'explicit' as const,
      'implied' as const,
      'none' as const,
    );

    it('badge output contains CSS class including the status value', () => {
      fc.assert(
        fc.property(statusArb, (status) => {
          const html = renderBadge(status);

          // Output contains `badge--{status}` as a CSS class
          expect(html).toContain(`badge--${status}`);

          // Output contains the base `badge` class
          expect(html).toContain('badge');

          // Full class attribute matches expected pattern
          expect(html).toContain(`class="badge badge--${status}"`);
        }),
        { numRuns: 100 },
      );
    });

    it('badge output contains the capitalized status text', () => {
      fc.assert(
        fc.property(statusArb, (status) => {
          const html = renderBadge(status);
          const expectedLabel = status.charAt(0).toUpperCase() + status.slice(1);

          expect(html).toContain(expectedLabel);
        }),
        { numRuns: 100 },
      );
    });

    it('each status maps to a distinct CSS class', () => {
      fc.assert(
        fc.property(
          statusArb,
          statusArb.filter((s) => true),
          (statusA, statusB) => {
            const htmlA = renderBadge(statusA);
            const htmlB = renderBadge(statusB);

            if (statusA !== statusB) {
              // Different statuses produce different CSS classes
              expect(htmlA).not.toBe(htmlB);
            } else {
              // Same status always produces the same output (deterministic)
              expect(htmlA).toBe(htmlB);
            }
          },
        ),
        { numRuns: 100 },
      );
    });
  });
});
