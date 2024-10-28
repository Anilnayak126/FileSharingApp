

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serilalizers import FileListSerializer
from rest_framework.parsers import MultiPartParser,FormParser

class HandleFileUpload(APIView):
    parser_classes = [MultiPartParser,FormParser]

    def post(self, request):
        try:
            data = request.data
            print(data)  # For debugging purposes

            serializer = FileListSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Files uploaded successfully',
                    'data': serializer.data
                })

            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)  # Log any exceptions
            return Response({'status': 500, 'message': str(e)})
