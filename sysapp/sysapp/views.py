import json, base64, io
from PIL import Image
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from transformers import pipeline
from .pipeline import textgen



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
        #response = general(message)
        #textOutput = response[0]['generated_text'][1]['content']
        textOutput = "Hello world"
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
        prompt = request.POST.get('prompt')
        model = request.POST.get('model')
        image_file = request.FILES.get('image')
        print(prompt)
        print(model)
        print(image_file)

        if(image_file):
            try:
                #read the content of image as bytes
                image_file_content = image_file.read()
                #encode bytes to base64
                base64_encoded_bytes = base64.b64encode(image_file_content)
                #decode base64 to string
                base64_string = base64_encoded_bytes.decode('utf-8')
                #decode back to image data
                #image_data = base64.b64decode(base64_string)
                #open image using PIL
                #image_pil = Image.open(io.BytesIO(image_data))
                #image_pil = image_pil.convert("RGB")
                #print(f"type of image_pil: {type(image_pil)}")
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
                print (response)
                textOutput = response[0]['generated_text'][1]['content']
                #textOutput = "hello from textfromimage"
                #print(textOutput)
                return JsonResponse({'response': textOutput})
            except Exception as e:
                print(f"Error processing image file: {e}")
                return JsonResponse({'response': f'Error converting image to base64:{e}'}, status=500)

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

