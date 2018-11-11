from django.db import models


class Quote(models.Model):
    movie = 'MV'
    book = 'BK'
    tv = 'TV'
    real = 'RL'
    other = 'OT'
    category_choices = (
        (movie, 'Movie'),
        (book, 'Book'),
        (tv, 'TV Series'),
        (real, 'Real Life'),
        (other, 'Other'),
    )
    body = models.TextField()
    person = models.CharField(max_length=40, blank=True)
    place = models.CharField(max_length=40, blank=True)
    category = models.CharField(max_length=20, choices=category_choices)
    fk_usr = models.ForeignKey(to='manage_users.User', on_delete=models.CASCADE)
    create_time = models.DateField(auto_now_add=True)
