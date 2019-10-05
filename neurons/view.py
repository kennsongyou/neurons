from django.shortcuts import render


def hello(request):
    context = {'hello': 'Hello World!', 'aa': '11'}
    return render(request, 'top-page/top-page.html', context)
