import json
import numpy as np
import pandas as pd
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
    vectors = np.array([narrative_embeddings[field] for field in fields])

    matrix = cosine_similarity(vectors)

    df = pd.DataFrame(matrix, index=fields, columns=fields)

    output_path = f"data/results/similarity_matrix_{narrative_id}.csv"
    df.to_csv(output_path)

    print(f"Saved {output_path}")