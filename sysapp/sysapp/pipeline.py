import torch
from transformers import pipeline
##from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

## Initialize the general model once
general_model = "unsloth/Phi-4-mini-instruct-unsloth-bnb-4bit"
general = pipeline("text-generation", model=general_model, max_length=400, num_return_sequences=1)


## Initialige the image generation model
##image_from_text = "stabilityai/stable-diffusion-2-1"
##pipe = StableDiffusionPipeline.from_pretrained(image_from_text, torch_dtype=torch.float16)
##pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
##imagegen = pipe.to("cuda")
## Commenting out because of heavy memory usage


## Initialize the image from text model
#text_from_image = "llava-hf/llava-onevision-qwen2-0.5b-ov-hf" 
#textgen = pipeline("image-text-to-text", model=text_from_image)




