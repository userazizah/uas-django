from django.http import HttpResponse
from django.template import loader

def main(request):
    temlate = loader.get_template('main.html')
    return HttpResponse(temlate.render())