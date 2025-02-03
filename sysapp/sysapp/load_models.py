from transformers import pipeline

#llm_1 = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")
llm_2 = pipeline("text-generation", model="Qwen/Qwen2.5-Coder-3B-Instruct")


def get_llm_2():
    return llm_2

