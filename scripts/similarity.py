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
    print(f"\nNarrative {narrative_id}")
    print("-" * 40)

    original_vector = np.array(narrative_embeddings["original"]).reshape(1, -1)

    for field in fields:
        comparison_vector = np.array(narrative_embeddings[field]).reshape(1, -1)

        score = cosine_similarity(original_vector, comparison_vector)[0][0]

        print(f"original vs {field}: {score:.4f}")