from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from FeedbackIngestion.models import Feedback
from FeedbackIngestion.serializers import FeedbackSerializers


# Create your views here.


class FeedbackListView(GenericAPIView):
    serializer_class = FeedbackSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Feedback.objects.filter(application__client_id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        feedbacks = self.get_queryset()
        page = self.paginate_queryset(feedbacks)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
