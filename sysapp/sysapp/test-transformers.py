from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B", max_length=1000, num_return_sequences=1)
output = pipe(messages)
textOutput = output[0]['generated_text'][1]['content']
print(textOutput)