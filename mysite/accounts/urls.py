from django.urls import path

from .views import SignUpView
# we will call this from view #


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]