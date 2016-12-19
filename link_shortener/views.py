from django.http import (HttpResponseBadRequest, HttpResponseNotAllowed,
                         JsonResponse)
from django.shortcuts import get_object_or_404, redirect, render

from link_shortener.models import Link, decode_tiny_url


def index(request):
    if request.method == 'GET':
        return render(request, 'link_shortener/index.html')

    if request.method != 'POST':
        return HttpResponseNotAllowed(['GET', 'POST'])

    try:
        url = request.POST['url']
    except KeyError:
        return HttpResponseBadRequest('No "url" param.')
    try:
        link = Link.objects.get(url=url)
    except Link.DoesNotExist:
        link = Link(url=url)
        link.save()

    tiny_url = '{}{}'.format(request.build_absolute_uri(), link.tiny_url)
    return JsonResponse({'tiny_url': tiny_url})


def redirection(request, tiny_url):
    link = get_object_or_404(Link, id=decode_tiny_url(tiny_url))
    link.visits = link.visits + 1
    link.save()
    return redirect(link.url, permanent=True)
