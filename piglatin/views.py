from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def translate(request):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    text = request.GET.get('text').lower()
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

    new_text = ' '.join(new_text)

    return render(request, 'translate.html',
                  {'original': text, 'translation': new_text})


def about(request):
    return render(request, 'about.html')
