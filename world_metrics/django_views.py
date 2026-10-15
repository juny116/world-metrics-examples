from django.http import JsonResponse
from .collector import collect_counters

def counters(request):
    return JsonResponse(collect_counters())
