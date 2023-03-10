from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from DiscourseIngestion.serializers import DiscourseFeedbackSerializer
from Enterpret.permissions import Permission
from Registration.models import DiscourseRegistration
from django.http import HttpResponseForbidden


# Create your views here.
class DiscourseFeedbackView(GenericAPIView):
    serializer_class = DiscourseFeedbackSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        Push Model where we are giving APIs to push the Feedback
        into database.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        application_id = request.data.get('application')

        if DiscourseRegistration.get_integration_type(application_id) == DiscourseRegistration.PULL_MODEL:
            return HttpResponseForbidden("Cannot push to a pull model")

        if Permission.is_client_authorised(request, request.data.get('application')):
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # idempotency supported by using primary key from the data
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
