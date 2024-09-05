from django.urls import path

from .views import LeaseAgreementListView,LeaseAgreementCreateView,LeaseAgreementDetailView, non_staff_users
urlpatterns = [
  path('',LeaseAgreementListView.as_view(),name='tenants'),
  path('create/',LeaseAgreementCreateView.as_view(),name='create_lease_agr'),
  path('<int:pk>',LeaseAgreementDetailView.as_view(),name='lease_agr_details' ),
  path('non-staff-users/', non_staff_users, name='non_staff_users'),
]