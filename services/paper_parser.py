import pdfplumber

def extract_text_from_pdf(pdf_path: str) -> str:
    """从 PDF 文件中提取文本"""
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text
