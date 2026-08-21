from pathlib import Path
from dataclasses import dataclass
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@dataclass
class Hit:
    source: str
    text: str
    score: float

class PolicyRetriever:
    def __init__(self, policy_dir: str = "data/policies"):
        paths = sorted(Path(policy_dir).glob("*.md"))
        self.sources = [p.name for p in paths]
        self.docs = [p.read_text(encoding='utf-8') for p in paths]
        self.vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
        self.matrix = self.vectorizer.fit_transform(self.docs)

    def search(self, query: str, top_k: int = 2):
        q = self.vectorizer.transform([query])
        scores = cosine_similarity(q, self.matrix)[0]
        idxs = scores.argsort()[::-1][:top_k]
        return [Hit(source=self.sources[i], text=self.docs[i], score=float(scores[i])) for i in idxs]