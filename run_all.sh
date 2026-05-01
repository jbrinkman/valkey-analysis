#!/usr/bin/env bash
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR/scripts"
source "../.venv/bin/activate"

echo "=== Valkey Integration Analysis ==="
echo "Started: $(date)"
echo ""

run_phase() {
    local phase="$1"
    local script="$2"
    local start=$(date +%s)
    echo "--- Phase $phase: $script ---"

    # Run script, show progress lines and summary, suppress noise
    python "$script" 2>&1 | while IFS= read -r line; do
        # Show progress: [N/M] lines
        if echo "$line" | grep -qE "INFO \[[0-9]+/[0-9]+\]"; then
            # Extract the progress and project name
            progress=$(echo "$line" | grep -oE "\[[0-9]+/[0-9]+\]")
            project=$(echo "$line" | grep -oE "[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+$" || echo "")
            printf "\r  Phase %s — Project %s: %s                    " "$phase" "$progress" "$project"
        fi
        # Show phase completion summary
        if echo "$line" | grep -qE "Phase .* complete|Results written|ERROR"; then
            echo ""
            echo "  $line" | sed 's/^.*INFO //'
        fi
    done

    local elapsed=$(( $(date +%s) - start ))
    local mins=$(( elapsed / 60 ))
    local secs=$(( elapsed % 60 ))
    echo "  Duration: ${mins}m ${secs}s"
    echo ""
}

run_phase "1"  "phase1_dependencies.py"
run_phase "2"  "phase2_documentation.py"
run_phase "2b" "phase2b_deepwiki.py"
run_phase "3"  "phase3_code_search.py"
run_phase "4"  "phase4_community_signals.py"
run_phase "5"  "phase5_ecosystem.py"
run_phase "6"  "phase6_synthesize.py"
run_phase "7"  "phase7_assemble.py"

echo "=== Analysis Complete ==="
echo "Finished: $(date)"
echo "Results: $SCRIPT_DIR/results/results.json"
echo "Reports: $SCRIPT_DIR/reports/"
