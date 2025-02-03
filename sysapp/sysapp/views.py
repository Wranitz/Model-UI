import json
from django.shortcuts import render
from django.http import JsonResponse
from sysapp.settings import llm_2

def home(request):
        #prompt = "Write a quick sort algorithm in python"
        #response = llm_2(prompt)[0]['generated_text']
        #print(response)
        return render(request, 'home.html')

def generate_text(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data['prompt']
        response = llm_2(prompt)[0]['generated_text']
        print(response)
        return JsonResponse({'response': response})
    return JsonResponse({'response': 'Invalid request'})

def classify_text(request):
    if request.method == 'POST':
        text = request.POST['text']
        response = llm_2(text)
        return JsonResponse({'response': response})
    return JsonResponse({'response': 'Invalid request'})

def generate_text_from_image(request):
    return JsonResponse({'response': 'Not implemented yet'})

def generate_image_from_text(request):
    return JsonResponse({'response': 'Not implemented yet'})

def generate_image_from_image(request):
    return JsonResponse({'response': 'Not implemented yet'})

