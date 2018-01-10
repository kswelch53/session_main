from django.shortcuts import render, HttpResponse, redirect
from datetime import date, datetime
today = str(date.today())
# date_add = "-- added on" + today
secret_key = "wordsgalore"

# Create your views here.
def index(request):
    print("This is index function in views.py")
    # if 'wordlist' not in request.session:
    request.session['wordlist'] = list()
    return render(request, 'session_words/index.html')

def addword(request):
    print("This is addword function in views.py")
    request.session['add_word'] = request.POST['add_word']
    request.session['colorpick'] = request.POST['color']
    try:
        request.session['bigfont'] = request.POST['bigfont']
        print ("Bigfont is:", request.session['bigfont'])
        print(today)

        request.session['bigfont'] == "on"
        print("Bigfont is checked")
        request.session['wordlist'].append([request.session['add_word'], request.session['colorpick'], "8", "-- added " + today])
    except:
        request.session['wordlist'].append([request.session['add_word'], request.session['colorpick'], "3", "-- added " + today])

    print(request.session['wordlist'])

    return redirect('/displayword')

def displayword(request):
    print("This is displayword function in views.py")
    print ("Bigfont is:", request.session['bigfont'])

    return render(request, 'session_words/index.html')

def clear(request):
    print("This is clear function in views.py");
    request.session['wordlist'] = list()
    return redirect('/')
