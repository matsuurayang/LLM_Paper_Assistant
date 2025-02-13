from fastapi import APIRouter
from services.summarizer import generate_summary

router = APIRouter()

@router.get("/summary/{paper_id}")
def get_summary(paper_id: str):
    # 示例化数据
    mock_text = "This is a mock full text of a paper used for summarization."
    summary = generate_summary(mock_text)
    return {"paper_id": paper_id, "summary": summary}
