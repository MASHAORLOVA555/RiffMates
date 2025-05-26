from django.shortcuts import render

# Create your views here.
data = {
    'news':[
    "RiffMates now has a news page",
    "RiffMates has it`s first web page"
]
}
return render(request, 'news.html", data)
              


