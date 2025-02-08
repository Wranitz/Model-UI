'''
    1. Need to use multi model for different tasks.
    2. First is text to text model for general purpose.
    3. Second is text to text model for programming and math problems.
    4. Third is Image to text model for general purpose.
    5. Fourth is Image to text model for programming and math problems.
    6. Fifth is Image to Image model for Image enhancement.
    7. Sixth is Image to Image model for Image generation.
    8. Seventh is Image to Video model for Video generation.
    9. Partition the different phases of code execution for running multiple models.
'''

from transformers import AutoModelForCausalLM, AutoTokenizer

first_model = "Qwen/Qwen2.5-0.5B-Instruct"
model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
third_model = ""
fourth_model = ""
fifth_model = ""



model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "What is a Quick short algorithm? Give example."
messages = [
    {"role": "system", "content": "You are AI chatbot, You are a helpful assistant for Math and programming problems."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

print(response)
