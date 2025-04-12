from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter

from sport.views import UserProfileViewSet, TeamViewSet, TeamMemberViewSet, TournamentViewSet, MatchViewSet, NewsViewSet

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'team-members', TeamMemberViewSet)
router.register(r'tournaments', TournamentViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]