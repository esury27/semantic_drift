#! /bin/bash

REPO=$(git rev-parse --show-toplevel)
cd "$REPO"



python ./src/compress.py
python ./src/regenerate.py
python ./src/embed.py
python ./src/similarity.py
python ./src/matrix.py
python ./src/matrix_csv.py
python ./src/pca_plot.py
