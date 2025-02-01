from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thankyou", views.ThankyouView.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path("review/<int:pk>", views.ReviewDetailsView.as_view()),

]
