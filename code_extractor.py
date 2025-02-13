import re

def extract_code_from_text(text: str) -> str:
    """从论文文本中提取代码片段（简单示例）"""
    code_blocks = re.findall(r"```(.*?)```", text, re.DOTALL)
    return "\n".join(code_blocks) if code_blocks else "No code found."
