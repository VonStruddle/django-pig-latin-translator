from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def translate(request):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    text = request.GET.get('text')
    new_text = []

    for word in text.split():
        if word[0] in vowels:
            new_text.append('{}way'.format(word))
        else:
            for index, letter in enumerate(word):
                if letter in vowels:
                    new_text.append('{0}{1}ay'.format(
                        word[index:],
                        word[:index]
                    ))
                    break

    return HttpResponse(' '.join(new_text))
