from django.http import JsonResponse

def my_api(request):
    data={'message':'hello'}
    return JsonResponse(data)