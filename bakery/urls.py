from django.urls import path
from bakery.views import SignUpView,SignInView,CategoryCreateView

urlpatterns = [
    path("register/",SignUpView.as_view(),name="signup"),
    path("",SignInView.as_view(),name="signin"),
    path("categories/add",CategoryCreateView.as_view(),name="add-category"),
    
]

