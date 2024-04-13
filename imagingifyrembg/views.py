from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import numpy as np
import rembg

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt  # For simplicity, disable CSRF protection. Use appropriate measures in production.
def remove_background(request):
    if request.method == 'POST':
        # Get the image file from the request
        image_file = request.FILES.get('image')

        if image_file:
            # Open the image using PIL
            with Image.open(image_file) as img:
                # Convert image to numpy array
                img_array = np.array(img)

            # Apply background removal using rembg
            output_array = rembg.remove(img_array)

            # Create a PIL Image from the output array
            output_img = Image.fromarray(output_array)

            # Create a response with the processed image
            response = HttpResponse(content_type="image/png")
            output_img.save(response, format="PNG")
            return response

    return JsonResponse({'error': 'Invalid request'}, status=400) 