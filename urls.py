# myapp/urls.py

from django.urls import path
from .views import admin_page,  CreateMedicalTestView, MedicalTestListView, UnansweredCustomerList, AnsweredCustomerList #CustomerList,

urlpatterns = [
    path('admin/', admin_page, name='admin_page'),
    #path('customers/', CustomerList.as_view(), name='customer_list'),
    path('create-medical-test/', CreateMedicalTestView.as_view(), name='create_medical_test'),
    path('medical-tests/', MedicalTestListView.as_view(), name='medical_test_list'),
    path('unanswered-customers/', UnansweredCustomerList.as_view(), name='unanswered_customer_list'),
    path('answered-customers/', AnsweredCustomerList.as_view(), name='answered_customer_list'),
]
