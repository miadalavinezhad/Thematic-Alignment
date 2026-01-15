# Measuring Thematic Alignment Between Journal Scope and its Published Articles
This project investigates whether articles published in a scientific journal align with the stated Aims & Scope of the journal. I propose a semantic similarity–based methodology that represents both the journal scope and article abstracts in a shared embedding space and quantifies semantic alignment between them using cosine similarity.
Using PLOS Computational Biology as a case study journal, I analyze thematic coherence across the published articles, identify drifts over time and potential outlier articles.

## Methodology
1. Data Collection
    - Article abstracts are retrieved from the Semantic Scholar Graph API
    - Papers are filtered by their venue and availability of abstracts
2. Sentence Embedding
    - The Aims & Scope of journal and article abstracts are encoded using a Sentence-BERT model
    - Each text is represented as a fixed-size semantic embedding
3. Alignment Score
    - Alignment is computed using cosine similarity between article embeddings and the scope embedding
    - Scores range from −1 to 1, with higher values indicating stronger thematic alignment
4. Analysis of Results
    - Distribution of alignment scores
    - Yearly trends and rolling averages
    - Inspection high and low alignment outliers qualitatively

## Clone Repository
```
git clone https://github.com/miadalavinezhad/Thematic-Alignment.git
cd thematic-alignment
```
## Install the Package
```
pip install e .
```

## Usage
Notebooks are made for demonstration and experiment purposes. Core logics are implemented in Python modules.
```
from thematic_alignment import fetch_papers
from thematic_alignment import EmbeddingModel
from thematic_alignment import cosine_alignment
from thematic_alignment import yearly_alignment
```
