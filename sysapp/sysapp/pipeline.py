import torch
from transformers import pipeline
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

## Initialize the general model once
general_model = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
general = pipeline("text-generation", model=general_model, max_length=1000, num_return_sequences=1)


## Initialige the image generation model
model_id = "stabilityai/stable-diffusion-2-1"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
imagegen = pipe.to("cuda")




