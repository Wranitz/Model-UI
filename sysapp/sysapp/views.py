import json, base64, io
from PIL import Image
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from transformers import pipeline
from .pipeline import general



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

def text_from_image(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        model = request.POST.get('model')
        image_file = request.FILES.get('image')
        if(image_file):
            try:
                #read the content of image as bytes
                image_file_content = image_file.read()
                #encode bytes to base64
                base64_encoded_bytes = base64.b64encode(image_file_content)
                #decode base64 to string
                base64_string = base64_encoded_bytes.decode('utf-8')
                message = [
                        {
                            "role": "user", 
                            "content": [
                                {"type": "image", "image": base64_string},
                                {"type": "text", "text": prompt}
                            ]
                        }
                    ]
                response = textgen(text=message, max_new_tokens=20)
                textOutput = response[0]['generated_text'][1]['content']
                return JsonResponse({'response': textOutput, 'image': base64_string})
            except Exception as e:
                print(f"Error processing image file: {e}")
                return JsonResponse({'response': f'Error converting image to base64:{e}'}, status=500)

    return JsonResponse({'response': 'Not implemented yet'})

def image_from_text(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data['prompt']
        #print(prompt)
        image = imagegen(prompt).images[0]
        #print(f"image type: {type(image)}")
        #print(f"image size: {image.size}")
        image.show()
        image_bytes = io.BytesIO()
        image.save(image_bytes, format='PNG')
        image_str = base64.b64encode(image_bytes.getvalue()).decode('utf-8')
        response = "This is an image generation response"
        return JsonResponse({'response': response, 'image': image_str})
    return JsonResponse({'response': 'Not implemented yet'})

def generate_image_from_image(request):
    return JsonResponse({'response': 'Not implemented yet'})

