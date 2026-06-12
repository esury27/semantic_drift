import json
from sentence_transformers import SentenceTransformer

with open("data/narratives.json", "r") as f:
    narratives = json.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

fields_to_embed = [
    "original",
    "summary_300",
    "summary_100",
    "summary_25",
    "sentence",
    "seed",
    "regenerated_from_seed"
]

embeddings = {}

for narrative in narratives:
    narrative_id = narrative["id"]
    embeddings[narrative_id] = {}

    for field in fields_to_embed:
        text = narrative[field]
        embedding = model.encode(text)
        embeddings[narrative_id][field] = embedding.tolist()

with open("data/embeddings.json", "w") as f:
    json.dump(embeddings, f, indent=2)

print("Embeddings saved to data/embeddings.json")