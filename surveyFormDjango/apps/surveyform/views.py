from django.shortcuts import render, HttpResponse, redirect
  
def survey(request):
    if not 'count' in request.session:
        request.session['count'] = 0
    return render(request, 'surveyform/survey.html')

def process(request):
    if request.method == "POST":
        request.session['count'] += 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    return render(request, 'surveyform/result.html')
