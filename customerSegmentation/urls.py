"""customerSegmentation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from user import views as user_view
from analysis import views as analysis

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_view.user_register, name="User Registration"),
    path('authenticate/', user_view.user_authentication, name="User Authentication"),
    path('user_search_history/', user_view.user_search_history, name="User Search History"),
    path('verifyemail/', user_view.verify_email),
    path('forgot/', user_view.forgot_details, name="forgot"),

    path('analysis/', analysis.customer_analysis, name='Twitter analysis')
]
