from rest_framework.decorators import api_view
from django.http.response import JsonResponse
import pandas as pd
import json
from .utils import *
import numpy as np


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


@api_view(['GET'])
def customer_analysis(request):
    type = request.GET['type']
    if type == 'kmeansClustering' :
        cust_data = kmeans_cluster()
        data = json.dumps(cust_data,cls=NumpyEncoder)
        return JsonResponse(data,safe=False)
        
    elif type == 'elbowmethod':
        cust_data = elbow_method()
        data = json.dumps(cust_data, cls=NumpyEncoder)
        return JsonResponse(data, safe=False)

    else:
        return JsonResponse({'message':'Not a valid request!'})
    
