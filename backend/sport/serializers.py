from django.contrib.auth.models import User

from rest_framework import serializers

from sport.models import UserProfile,Team, TeamMember, Tournament, Match, News\


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id' 'username', 'email')

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('__all__')
        read_only_fields = ('id', 'created_at', 'updated_at')

class TeamSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Team
        fields = ('__all__')
        read_only_fields = ('id', 'created_at', 'updated_at')

class TeamMemberSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = TeamMember
        fields = ('__all__')
        read_only_fields = ('id', 'created_at', 'updated_at')

class TournamentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Tournament
        fields = ('__all__')
        read_only_fields = ('id', 'created_at', 'updated_at')

class MatchSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Match
        fields = ('__all__')
        read_only_fields = ('id', 'created_at', 'updated_at')


class NewsSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = News
        fields = ('__all__')
        read_only_fields = ('id', 'created_at', 'updated_at')

