from django.shortcuts import render, get_object_or_404
from .models import Avto
# from rest_framework.generics import ListAPIView
# from rest_framework.viewsets import ViewSet
# from .serializers import AvtoApiSerializer

#
# class AvtoListView(ViewSet):
#     queryset = Avto.objects.all()
#     serializer_class = AvtoApiSerializer




def home(request):
    lates_new = Avto.objects.order_by('-id').first()
    news = Avto.objects.order_by('-id')[:5]
    chevrolet = Avto.objects.filter(category__name="Chevrolet")
    bmw = Avto.objects.filter(category__name="Bmw")
    mers = Avto.objects.filter(category__name="Mers")
    context={
        "lates_new":lates_new,
        "news":news,
        "chevrolet":chevrolet,
        "bmw":bmw,
        "mers":mers,

    }
    return render(request,'index.html',context)






def aloqa(request):
    return render(request,'contact.html')

