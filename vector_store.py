import numpy as np

class VectorStore:

    def __init__(self):
        self.docs = []
        self.vectors = []

    def add(self, doc, vector):
        self.docs.append(doc)
        self.vectors.append(vector)

    def search(self, query_vec, top_k=4):

        vectors = np.array(self.vectors)

        sims = np.dot(vectors, query_vec) / (
            np.linalg.norm(vectors, axis=1) * np.linalg.norm(query_vec)
        )

        top_ids = np.argsort(sims)[-top_k:][::-1]

        results = [(self.docs[i], sims[i]) for i in top_ids]

        return results