from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response

from .models import ConnectionModel
from .serializers import ConnectionModelSerializer
from rest_framework import viewsets,status
from .permissions import IsAuthenticatedOrReadOnly


class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = ConnectionModel.objects.all()
    serializer_class =ConnectionModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        full_name = serializer.validated_data.get('fullname')
        email = serializer.validated_data.get('email')
        phone_number = serializer.validated_data.get('phone_number')
        management = serializer.validated_data.get('management')
        text_information = serializer.validated_data.get('text')
        subject = 'New Connection Information'
        message = (f'Full Name: {full_name}\nEmail: {email}\nPhone Number: '
                   f'{phone_number}\nManagement: {management}\nText Information: {text_information}')
        from_email = settings.EMAIL_HOST_USER
        to_email = ['info@tmsiti.uz']

        send_mail(subject, message, from_email, to_email, fail_silently=False)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

