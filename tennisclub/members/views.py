from django.template import loader
from django.http import HttpResponse

# Create your views here.
def members(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

