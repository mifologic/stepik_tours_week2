from django.urls import path

from tours import views


urlpatterns = [
    path('', views.main_view),
    path('departure/<str:departure>/', views.departure_view),
    path('tours/<int:tour_id>/', views.tour_view)
]

handler404 = views.custom_handler404
handler500 = views.custom_handler500
