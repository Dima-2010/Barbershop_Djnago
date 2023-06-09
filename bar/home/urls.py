from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>', views.details.as_view(), name='details'),
    path('<int:pk>/отзывы', views.reverse.as_view(), name='reverse'),
    path('<int:pk>/work', views.WorkView.as_view(), name='work'),
]
