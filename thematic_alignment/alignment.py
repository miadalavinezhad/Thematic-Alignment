import numpy as np

def cosine_alignment(emb_vec1: np.ndarray, emb_vec2: np.ndarray) -> float:
    """
    Compute the cosine similarity between first vector(paper abstract) and 
    the second vector(aim & scope).
    """
    dot_product = np.dot(emb_vec1, emb_vec2)
    norm_emb_vec1 = np.linalg.norm(emb_vec1)
    norm_emb_vec2 = np.linalg.norm(emb_vec2)
    if norm_emb_vec1 == 0 or norm_emb_vec2 == 0:
        return 0
    return dot_product / (norm_emb_vec1 * norm_emb_vec2)