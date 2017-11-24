from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
  
def index(request):
    return render(request, 'words/index.html')

def process(request):
    if 'stored_words' not in request.session:
        request.session['stored_words'] =[]

    if 'big' in request.POST:
        print "hello"
        data = {
            'word': request.POST['word'],
            'color': request.POST['color'],
            'size': "big",
            'time': datetime.now().strftime("%-I %M %S %p -- %B %d %Y"),
        }
        request.session['stored_words'].append(data)
    else: 
        data = {
            'word': request.POST['word'],
            'color': request.POST['color'],
            'size': "small",
            'time': datetime.now().strftime("%-I %M %S %p -- %B %d %Y"),
        }
        request.session['stored_words'].append(data)
    request.session.modified = True
    return redirect('/')
def clear(request):
    request.session.clear()
    return redirect('/')