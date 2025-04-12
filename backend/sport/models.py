from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(BaseModel):
    nickname = models.CharField(max_length=50, unique=True)
    about = models.TextField(blank=True, null=True)
    notifications_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.nickname


class Team(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    cover = models.ImageField(upload_to='team_cover/', blank=True, null=True)
    created_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, related_name='teams', null=True)

    def __str__(self):
        return self.name


class TeamMember(BaseModel):
    ROLE_CHOICES = (
        ('capitan', 'Капитан'),
        ('player', 'Игрок'),
        ('substitute', 'Запасной'),
    )

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members', )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Team_members', )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='player', )

    class Meta:
        unique_together = ('team', 'user')

    def __str__(self):
        return f"{self.user.username} - ({self.get_role_display()})"


class Tournament(BaseModel):
    STATUS_CHOICES = (
        ('registration', 'Сбор команд'),
        ('ongoing', 'В процессе'),
        ('finished', 'Завершен'),
    )

    name = models.CharField(max_length=200)
    game = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='registration')
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, related_name='tournaments', null=True)

    def __str__(self):
        return self.name


class Match(BaseModel):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='matches', )
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_team1', null=True)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_team2', null=True)
    match_time = models.DateTimeField()
    score_team1 = models.PositiveIntegerField(default=0)
    score_team2 = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.team1} - {self.team2} - {self.tournament}"


class News(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    cover = models.ImageField(upload_to='news_cover/', blank=True, null=True)
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, related_name='news', null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
