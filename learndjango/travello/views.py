from django.shortcuts import render
from .models import Destination

# Create your views here.
# def index(request):
#     # dest1 = Destination()
#     # dest1.name = 'Mumbai'
#     # return render(request,"index.html",{'dest1':dest1}) in html {{dest1.name}}
#     dest1 = Destination()
#     dest1.name = 'Mumbai'
#     dest1.img = 'destination_1.jpg'
#     dest1.desc = 'This is Mumbai'
#     dest1.price = 600
#     dest1.offer = False

#     dest2 = Destination()
#     dest2.name = 'Hydrabad'
#     dest2.img = 'destination_2.jpg'
#     dest2.desc = 'This is Hydrabad'
#     dest2.price = 450
#     dest1.offer = True

#     dest3 = Destination()
#     dest3.name = 'Bangaluru'
#     dest3.img = 'destination_3.jpg'
#     dest3.desc = 'Namma Bangaluru'
#     dest3.price = 700

    
#     dest = [dest1,dest2,dest3]
#     return render(request,'index.html',{'dests':dest})

def index(request):
    dests = Destination.objects.all()
    return render(request,'index.html',{'dests':dests})