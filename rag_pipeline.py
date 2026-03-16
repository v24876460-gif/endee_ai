from sentence_transformers import SentenceTransformer
from vector_store import VectorStore

model = SentenceTransformer("all-MiniLM-L6-v2")

store = VectorStore()

def index_chunks(chunks):

    for chunk in chunks:

        emb = model.encode(chunk)

        store.add(chunk, emb)


def retrieve(question):

    q_vec = model.encode(question)

    return store.search(q_vec)