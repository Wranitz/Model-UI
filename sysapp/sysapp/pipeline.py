from transformers import pipeline

# Initialize the pipeline once
general_model = "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"
general = pipeline("text-generation", model=general_model, max_length=200, num_return_sequences=1)
