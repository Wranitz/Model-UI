import torch
from transformers import pipeline
##from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

## Initialize the general model once
##general_model = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
##general = pipeline("text-generation", model=general_model, max_length=400, num_return_sequences=1)


## Initialige the image generation model
##image_from_text = "stabilityai/stable-diffusion-2-1"
##pipe = StableDiffusionPipeline.from_pretrained(image_from_text, torch_dtype=torch.float16)
##pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
##imagegen = pipe.to("cuda")
## Commenting out because of heavy memory usage


## Initialize the image from text model
text_from_image = "unsloth/Qwen2.5-VL-7B-Instruct-unsloth-bnb-4bit" 
textgen = pipeline("image-text-to-text", model=text_from_image)




