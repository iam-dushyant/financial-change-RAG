from src.retriever import PolicyRetriever

def test_payment_change_retrieval():
    r = PolicyRetriever()
    hits = r.search("payment database schema change rollback peak hours", top_k=2)
    names ={h.source for h in hits}
    assert "payments-release-policy.md" in names

