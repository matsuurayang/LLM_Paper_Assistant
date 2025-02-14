from transformers import T5ForConditionalGeneration, T5Tokenizer

# 加载 T5-small 模型和分词器
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# 返回加载的模型和分词器，供其他模块使用
def get_model():
    return model

def get_tokenizer():
    return tokenizer
