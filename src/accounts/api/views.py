from rest_framework import viewsets
from accounts.api.serializers import TeachingAssistantProfileSerializer, UserSerializer, \
    TeachingAssistantCoordinatorProfileSerializer, TeachingAssistantSupervisorProfileSerializer

from accounts.models import TeachingAssistantProfile, TeachingAssistantCoordinatorProfile,\
    TeachingAssistantSupervisorProfile
from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return get_object_or_404(User,
                                 id=self.request.user.id) if self.action == 'current' else super().get_object()

    @action(methods=['get'], detail=False)
    def current(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)


class TeachingAssistantViewSet(viewsets.ModelViewSet):
    serializer_class = TeachingAssistantProfileSerializer
    queryset = TeachingAssistantProfile.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_object(self):
        return get_object_or_404(TeachingAssistantProfile,
                                 user=self.request.user) if self.action == 'current' else super().get_object()

    @action(methods=['get'], detail=False)
    def current(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)


class TeachingAssistantCoordinatorViewSet(viewsets.ModelViewSet):
    serializer_class = TeachingAssistantCoordinatorProfileSerializer
    queryset = TeachingAssistantCoordinatorProfile.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TeachingAssistantSupervisorViewSet(viewsets.ModelViewSet):
    serializer_class = TeachingAssistantSupervisorProfileSerializer
    queryset = TeachingAssistantSupervisorProfile.objects.all()
