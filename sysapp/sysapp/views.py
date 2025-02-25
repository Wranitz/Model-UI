import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from transformers import pipeline
from .pipeline import general, textgen


def home(request):
        return render(request, 'home.html')


def generate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data['prompt']
        model = data['model']
        message = [
             {"role": "user", "content": prompt}
        ]
        response = general(message)
        textOutput = response[0]['generated_text'][1]['content']
        #textOutput = "Hello world"
        return JsonResponse({'response': textOutput})
    return JsonResponse({'response': 'Invalid request'})

def classify_text(request):
    if request.method == 'POST':
        text = request.POST['text']
        response = "This is a text classification response"
        return JsonResponse({'response': response})
    return JsonResponse({'response': 'Invalid request'})

def text_from_image(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data['prompt']
        print (prompt)
        image = data['image']
        message = [
            {"role": "user", "content": prompt}
        ]
        response = textgen(message)
        print (response)
        textOutput = response[0]['generated_text'][1]['content']
        return JsonResponse({'response': textOutput})
    return JsonResponse({'response': 'Not implemented yet'})

def image_from_text(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data['prompt']
        #image = imagegen(prompt).images[0]
        #image.save(" /image.png")
        response = "This is an image generation response"
        return JsonResponse({'response': response})
    return JsonResponse({'response': 'Not implemented yet'})

def generate_image_from_image(request):
    return JsonResponse({'response': 'Not implemented yet'})

