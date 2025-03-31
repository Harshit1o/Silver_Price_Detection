from django.shortcuts import render
import pandas as pd
import numpy as np
import joblib
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'predictor/home.html')

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Load the model
            model = joblib.load('silver_prices_model.pkl')
            
            # Prepare input data
            input_data = np.array([
                float(data.get('open', 0)),
                float(data.get('high', 0)),
                float(data.get('low', 0)),
                float(data.get('volume', 0))
            ]).reshape(1, -1)
            
            # Make prediction
            prediction = model.predict(input_data)[0]
            
            return JsonResponse({
                'success': True,
                'prediction': float(prediction)
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
