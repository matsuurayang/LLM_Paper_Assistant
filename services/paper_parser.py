import fitz  # PyMuPDF


# 用于提取 PDF 文本的函数
def parse_pdf(file_contents: bytes) -> str:
    # 使用 PyMuPDF 打开 PDF
    doc = fitz.open(stream=file_contents, filetype="pdf")

    # 提取每一页的文本
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()

    return text
