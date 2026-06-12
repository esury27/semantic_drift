import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

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

narrative_id = list(embeddings.keys())[0]

vectors = np.array([
    embeddings[narrative_id][field]
    for field in fields
])

pca = PCA(n_components=2)

coords = pca.fit_transform(vectors)

plt.figure(figsize=(8,6))

for i, field in enumerate(fields):
    x = coords[i,0]
    y = coords[i,1]

    plt.scatter(x, y)
    plt.text(x, y, field)

for i in range(len(fields)-1):
    plt.plot(
        [coords[i,0], coords[i+1,0]],
        [coords[i,1], coords[i+1,1]]
    )

plt.title("Narrative Compression Trajectory")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.tight_layout()

plt.savefig("data/pca_plot.png", dpi=300)

plt.show()