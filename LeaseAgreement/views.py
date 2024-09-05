from django.shortcuts import render
from .models import LeaseAgreement
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import LeaseAgreementSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model() 

class LeaseAgreementListView(ListAPIView):

  queryset = LeaseAgreement.objects.all()
  serializer_class = LeaseAgreementSerializer
  
class LeaseAgreementCreateView(CreateAPIView):
  queryset = LeaseAgreement.objects.all()
  serializer_class = LeaseAgreementSerializer
  
class LeaseAgreementDetailView(RetrieveUpdateDestroyAPIView):
  queryset = LeaseAgreement.objects.all()
  serializer_class = LeaseAgreementSerializer

@api_view(['GET'])
def non_staff_users(request):
    users = User.objects.filter(is_staff=False)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)