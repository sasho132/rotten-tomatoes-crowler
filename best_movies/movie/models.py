from django.db import models

class Movie(models.Model):
    title = models.CharField('Title', max_length=255, unique=True)
    critics_consensus = models.TextField('Critics Consensus', blank=True, null=True)
    average_grade = models.DecimalField(
        'Average Grade', max_digits=3, decimal_places=2, blank=True, null=True
    )
    poster = models.ImageField('Poster', blank=True, null=True)
    amount_reviews = models.PositiveBigIntegerField('Amount Reviews', blank=True, null=True)
    approval_percentage = models.PositiveBigIntegerField('Approval Percentage', blank=True, null=True)

    def __str__(self):
        return self.title
    