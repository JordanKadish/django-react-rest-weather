from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    ''' simplest view possible
        Args:
            request (django.http.HttpRequest): a request object
        Returns:
            HttpResponse(django.http.HttpResponse) a response object
    '''
    return HttpResponse("Hello, world. You're at the weather index.")
