from django.shortcuts import render

def home_screen_view(request):
    print(request.headers)
    return render(request,"home.html",{})
def show_map(request):
    print(request.headers)
    return render(request,"graph.html",{})

    
