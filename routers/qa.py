from fastapi import APIRouter
from services.qa_system import answer_question

router = APIRouter()

@router.post("/qa")
def ask_question(paper_id: str, question: str):
    mock_context = "This is a mock full text of a paper used for question answering."
    answer = answer_question(mock_context, question)
    return {"paper_id": paper_id, "question": question, "answer": answer}
