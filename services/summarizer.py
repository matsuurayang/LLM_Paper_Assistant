from models import summarizer

def generate_summary(text: str) -> str:
    """生成论文摘要"""
    summary = summarizer(text, max_length=200, min_length=50, do_sample=False)
    return summary[0]['summary_text']
