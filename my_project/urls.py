"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import StudentListView , StudentDetailsView , StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', StudentListView.as_view(), name='list-API'),
    path('detail/<int:student_id>/', StudentDetailsView.as_view(), name='detail-API'),
    path('update/<int:student_id>/', StudentUpdateView.as_view(), name='update-API'),
    path('delete/<int:student_id>/', StudentDeleteView.as_view(), name='delete-API'),
]
