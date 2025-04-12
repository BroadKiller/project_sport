from django.contrib import admin

from sport.models import UserProfile, Team, TeamMember, Tournament, Match, News


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'about', 'notifications_enabled', 'created_at', 'updated_at')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cover', 'created_by', 'created_at', 'updated_at')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'user', 'role', 'created_at', 'updated_at')



@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'game', 'status', 'description', 'created_by', 'created_at', 'updated_at')


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'tournament', 'team1', 'team2', 'match_time', 'score_team1', 'score_team2', 'created_at', 'updated_at')



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'cover', 'author', 'published_at', 'is_published', 'created_at', 'updated_at')

