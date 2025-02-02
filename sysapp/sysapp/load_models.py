from transformers import pipeline

llm_1 = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")
#llm_2 = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_llm_1():
    return llm_1

