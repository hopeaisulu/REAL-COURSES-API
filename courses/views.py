from rest_framework import generics 
from .serializers import *
from .models import *


class CourseApiViews (generics.ListCreateAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

	def perform_create (self, serializer):
		serializer.save()


class BranchApiViews (generics.ListCreateAPIView):
	queryset = Branch.objects.all()
	serializer_class = BranchSerializer


class CategoryApiViews (generics.ListCreateAPIView):
	queryset = Category.objects.all()
	serializer_class = ContactSerializer


class CourseDetail (generics.RetrieveUpdateDestroyAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
