from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    url = "https://newsapi.org/v2/everything?q=Marvel&from=2022-01-05&sortBy=popularity&apiKey=d8d1bcd35cd54e16b951dfaa0c5388fa"

    cricket_news = requests.get(url).json()

    a = cricket_news['articles']
    desc = []
    title = []
    img = []


    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])


    mylist = zip(title, desc, img)
    context = {'mylist': mylist}

    return render(request, 'index.html', context)

