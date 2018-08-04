from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render (request, 'home.html', {'kells':'Mfks'})

def about(request):
    return render(request, 'about.html')

def mgk(request):
    return HttpResponse("""<h1>
        "This is my way to laceUP...!!!"
    </h1>""")

def count(request):
    kellstext = request.GET['KellsText']
    wordlist = kellstext.split()
    worddict = {}

    for word in wordlist:
        if word in worddict:
            #Increase
            worddict[word] += 1
        else:
            #ADD to the dictionary
            worddict[word] = 1
    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'kellstext':kellstext, 'count':len(wordlist), 'variable': worddict})
