from django.shortcuts import render
from .models import Meeting
from django.http import HttpResponse

def index(request):
    return render(request, "invitation/index.html")

def date(request):
    if request.method == "POST":
        print("POST")
        print(request.POST)

        meeting_date = request.POST.get("date")
        print(meeting_date)

        if meeting_date:
            Meeting.objects.create(date=meeting_date)

        return HttpResponse("OK")

    return render(request, "invitation/date.html")


