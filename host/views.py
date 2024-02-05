from django.http import HttpResponseRedirect, HttpResponse


def page_not_found_view(request, exception):
    return HttpResponseRedirect("/")
