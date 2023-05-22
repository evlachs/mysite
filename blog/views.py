from django.shortcuts import render


def index(request, name='rekruto', message='lets fuck'):
    return render(request,
                  'blog/index.html',
                  {'name': name, 'message': message})
