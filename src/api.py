from fastapi import FastAPI
from pydantic import BaseModel, Field
from src.retriever import PolicyRetriever
from src.llm import generate_answer

app = FastAPI(title="Financial Change RAG Copilot", version="1.0")
retriever = PolicyRetriever()

class AskRequest(BaseModel):
    question: str = Field(min_length=5, max_length=500, description="The question to ask the RAG copilot.")

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/ask")
def ask(request: AskRequest):
    hits = retriever.search(request.question, top_k=2)
    context = "\n\n".join(f"SOURCE: {h.source}\n{h.text}" for h in hits)
    answer = generate_answer(request.question, context)
    return {
        "answer": answer,
        "sources": [{"name": h.source, "score": round(h.score, 3)} for h in hits]
    }