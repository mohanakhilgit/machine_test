from rest_framework.generics import (
    ListCreateAPIView,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import StudentSerializer
from .models import Student
from .utils import add_watermark


class StudentListCreateAPIView(ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Student.objects.all()
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # profile_pic = request.data.get('profile_pic')
        # if profile_pic:
        #     profile_pic.name = 'profile_pic' + str(serializer.instance.id) + '.jpeg'
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # data = serializer.data
            # profile_pic = data.get('profile_pic')
            # if profile_pic:
            #     # Add watermark to profile pic
            #     profile_pic = add_watermark(profile_pic, 'watermark.png')
            #     request.data['profile_pic'] = profile_pic
            return Response(serializer.data, status=status.HTTP_201_CREATED)
