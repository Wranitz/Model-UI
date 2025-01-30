from transforms import pipeline

llm_1 = pipeline("text-to-text", model="Qwen/Qwen2.5-0.5B-Instruct")
llm_2 = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_llm_1():
    return llm_1

def get_llm_2():
    return llm_2