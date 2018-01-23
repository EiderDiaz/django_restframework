from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from .models import Duck
from .serializers import DuckSerializer


class DuckList(generics.ListCreateAPIView):
	queryset = Duck.objects.all()
	serializer_class = DuckSerializer
	def get_object(self):
		queryset = self.get_quertset()
		obj = get_object_or_404(
			queryset,
			pk=self.kawrgs['pk'],)
		return obj



# Create your views here.


 