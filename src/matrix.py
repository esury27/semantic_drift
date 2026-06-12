import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

with open("data/embeddings.json", "r") as f:
    embeddings = json.load(f)

fields = [
    "original",
    "summary_300",
    "summary_100",
    "summary_25",
    "sentence",
    "seed",
    "regenerated_from_seed"
]

for narrative_id, narrative_embeddings in embeddings.items():
    print(f"\nSimilarity matrix for narrative {narrative_id}")
    print("-" * 80)

    vectors = []

    for field in fields:
        vector = narrative_embeddings[field]
        vectors.append(vector)

    vectors = np.array(vectors)

    matrix = cosine_similarity(vectors)

    print(" " * 24 + " ".join([f"{field[:10]:>10}" for field in fields]))

    for i, field in enumerate(fields):
        row = " ".join([f"{matrix[i][j]:10.4f}" for j in range(len(fields))])
        print(f"{field[:20]:>20} {row}")