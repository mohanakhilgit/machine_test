from django.urls import path

from .views import StudentListCreateAPIView

urlpatterns = [
    path('detail/', StudentListCreateAPIView.as_view(), name='student_list_create'),
]
