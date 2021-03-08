
from django.shortcuts import render




def math(request, one, what, two_number):

    string = f'{one} {what} {two_number} ='
    if what == '+':
        answer = one + two_number
        rez = string + str(answer)
        return render(request, 'user/math.html', {'rez': rez})

    elif what == '-':
        answer = one - two_number
        rez = string + str(answer)
        return render(request, 'user/math.html', {'rez': rez})

    elif what == '*':
        answer = one * two_number
        rez = string + str(answer)
        return render(request, 'user/math.html', {'rez': rez})
    elif what == 'dil':
        answer = one // two_number
        rez = string + str(answer)
        return render(request, 'user/math.html', {'rez': rez})
