from django.http import Http404
from django.shortcuts import render_to_response


def detail(request):

    return render_to_response('pages/wedding.html')
