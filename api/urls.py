from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers
from rest_framework.authtoken import views

router=routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employees', EmployeeViewSet)



urlpatterns = [
    path('',include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]

# companies/{companyId}/employees
