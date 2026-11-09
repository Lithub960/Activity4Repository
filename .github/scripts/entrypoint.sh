#!/bin/bash

echo "Starting Frequency Analyzer..."

# Running the Python frequency analyzer
FREQ_RESULT=$(python3 /SoloRepository/.github/scripts/frequency.py /app/data.txt)

# Running update_readme.sh
bash /SoloRepository/.github/scripts/update_readmme.sh "$FREQ_RESULT" "$GITHUB_USER"

echo "Process Completed!"
