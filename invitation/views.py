from django.shortcuts import render
from .models import Meeting

def index(request):
    return render(request, "invitation/index.html")
def date(request):
    if request.method == "POST":
        meeting_date = request.POST.get("date")

        if meeting_date:
            Meeting.objects.create(date=meeting_date)
            
        return render(request, "invitation/date.html", {
            "success": True
        })
    return render(request, "invitation/date.html")


