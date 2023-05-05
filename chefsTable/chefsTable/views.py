from django.http import Http404, HttpResponse

def handler404(request, exception):
    return HttpResponse("404: Page not found")