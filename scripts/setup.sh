#!/bin/bash
set -e

REPO=$(git rev-parse --show-toplevel)
cd "$REPO"

python3 -m venv "$REPO/.sea"
source "$REPO/.sea/bin/activate"

pip install --upgrade pip
pip install -r "$REPO/scripts/requirements.txt"

python -m ipykernel install --user --name=repo-env --display-name "Narrative Seeds"

echo ""
echo "Setup complete."