from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FileListSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class HandleFileUpload(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        print(request.data) 

        serializer = FileListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'message': 'Files uploaded successfully',
                'data': serializer.data
            })

        print(serializer.errors)  
        return Response({
            'status': 400,
            'message': 'File upload failed',
            'errors': serializer.errors
        })
