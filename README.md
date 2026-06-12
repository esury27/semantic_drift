# Narrative Seeds and the Compression of Experience

## Overview

This project explores whether narrative memories can be represented as progressively compressed forms of experience.

Starting from an original narrative passage, the pipeline generates multiple levels of abstraction:

```
Original
↓
Summary (300 words)
↓
Summary (100 words)
↓
Summary (25 words)
↓
Sentence
↓
Narrative Seed
↓
Regenerated Narrative
```

The central question is:

> What survives when experience is compressed, and what emerges when it is reconstructed?

---

## Motivation

Human memory is not a perfect recording device.

Experiences are forgotten, condensed, reorganized, and retold. This project investigates whether narrative memories can be understood as compressed representations and whether a sufficiently abstract "narrative seed" can generate new narrative instances while preserving underlying structure.

Inspired by:

- Narrative identity theory (Schechtman)
- Memory and forgetting research
- Cognitive science of representation
- Large language models and latent representations

---

## Research Questions

1. How much semantic information survives compression?
2. Do narrative seeds preserve content or structure?
3. Can a seed reconstruct an original narrative?
4. What is lost and gained during regeneration?
5. What geometry emerges from narrative compression?

---

## Project Structure

```text
identity-ml/

├── data/
│   ├── narratives.json
│   ├── embeddings.json
│   ├── similarity_matrix_001.csv
│   └── pca_plot.png
│
├── scripts/
│   ├── compress.py
│   ├── regenerate.py
│   ├── embed.py
│   ├── similarity.py
│   ├── matrix.py
│   ├── matrix_csv.py
│   └── pca_plot.py
│
├── notebooks/
│
└── README.md
```

---

## Pipeline

### 1. Compression

Input:

```json
{
  "id": "001",
  "source": "...",
  "original": "..."
}
```

Generated fields:

- `summary_300`
- `summary_100`
- `summary_25`
- `sentence`
- `seed`

Script:

```bash
python scripts/compress.py
```

---

### 2. Regeneration

Generate a new narrative from the seed.

Script:

```bash
python scripts/regenerate.py
```

Generated field:

```json
"regenerated_from_seed": "..."
```

---

### 3. Embeddings

Text representations are embedded using:

```text
all-MiniLM-L6-v2
```

Each text becomes a 384-dimensional vector.

Script:

```bash
python scripts/embed.py
```

Output:

```text
data/embeddings.json
```

---

### 4. Similarity Analysis

Cosine similarity is computed between narrative representations.

Scripts:

```bash
python scripts/similarity.py
python scripts/matrix.py
python scripts/matrix_csv.py
```

Outputs:

- Pairwise similarity scores
- Similarity matrices
- CSV exports

---

### 5. PCA Visualization

Embedding vectors are projected from:

```text
384 dimensions
↓
2 dimensions
```

using Principal Component Analysis (PCA).

Script:

```bash
python scripts/pca_plot.py
```

Output:

```text
data/pca_plot.png
```

---

## Preliminary Results

Using a passage from *The Passion According to G.H.* by Clarice Lispector:

| Comparison | Similarity |
|------------|------------|
| Original ↔ Summary 300 | 0.6740 |
| Original ↔ Summary 100 | 0.6486 |
| Original ↔ Summary 25 | 0.5594 |
| Original ↔ Sentence | 0.6630 |
| Original ↔ Seed | 0.6174 |
| Original ↔ Regenerated | 0.6151 |

### Observations

- Compression generally reduces semantic similarity.
- Narrative seeds preserve abstraction more than content.
- Regeneration does not reconstruct the original narrative.
- Regeneration remains close to the seed representation.
- Seeds may function more like latent schemas than compressed copies.

---

## PCA Interpretation

Current visualization suggests:

- The original narrative is separated from compressed representations.
- Sentence, seed, and regenerated narrative form a cluster.
- Regeneration remains near the seed rather than returning toward the original.

This suggests that narrative compression may preserve a generative structure rather than a faithful representation of experience.

---

## Future Work

### Dataset Expansion

Collect:

- Clarice Lispector
- Virginia Woolf
- James Joyce
- Diary entries
- Autobiographical memories
- Philosophical reflections

Target size:

```text
20–50 narratives
```

### Additional Analyses

- UMAP visualization
- Cross-narrative clustering
- Compression trajectory comparison
- Reconstruction error analysis
- Seed similarity networks

---

## Long-Term Goal

Develop a computational framework for studying memory as a process of compression and regeneration rather than retrieval.

The project investigates whether narrative identity may emerge from compressed generative structures that persist even as specific experiences are forgotten.