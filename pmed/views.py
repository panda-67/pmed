from django.views.generic import TemplateView


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

class WelcomeView(TemplateView):
    template_name = "welcome.html"