from django.urls import path, include
from .views import (
    LeaseAgreementListView,
    LeaseAgreementCreateView,
    LeaseAgreementDetailView,
    check_expiring_leases,
    overdue_payments
)

urlpatterns = [
    path('', LeaseAgreementListView.as_view(), name='tenants'),
    path('create/', LeaseAgreementCreateView.as_view(), name='create_lease_agr'),
    path('<int:pk>/', LeaseAgreementDetailView.as_view(), name='lease_agr_details'),
    # new path
    path('expiring-leases/', check_expiring_leases, name='check_expiring_leases'),
    path('overdue-payments/', overdue_payments, name='overdue_payments'),

]
