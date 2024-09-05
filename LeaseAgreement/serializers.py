from rest_framework import serializers
from .models import LeaseAgreement
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'date_of_birth', 'emergency_contact_name', 'emergency_contact_phone', 'profile_picture']
        
class LeaseAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaseAgreement
        fields = ['id', 'tenant','property','rent_amount','security_deposit','payment_frequency','lease_terms','is_active','created_at','lease_start_date','lease_end_date'] # Serialize all fields of the Product model


# LeaseAgreementSerializer: This serializer is for the LeaseAgreement model and should be used to serialize lease agreement data.

# UserSerializer: This serializer should be created to handle serialization of user data.