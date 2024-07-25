from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

from .serializers import MediaSerializer
from PIL import Image
import io

class ImageToPDFApiView(CreateAPIView):
    serializer_class = MediaSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image = serializer.validated_data['media']

        if image:
            try:
                img = Image.open(image)
                img_byte_arr = io.BytesIO()
                img.save(img_byte_arr, format='PDF')
                img_byte_arr = img_byte_arr.getvalue()

                response = HttpResponse(img_byte_arr, content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{image.name}.pdf"'
                return response
            except Exception:
                return Response({'error': 'Your file must be image'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)