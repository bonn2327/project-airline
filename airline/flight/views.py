from django.shortcuts import render

from .models import Flight

# Create your views here.
def index(request):
    return render(request, "flight/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flight/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all()
    })
    