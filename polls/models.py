import datetime
from django.db import models
from django.utils import timezone

"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
"""

################################################################################################


class Quiz(models.Model):
    #general
    title = models.CharField()
    description = models.CharField()
    figure = models.ImageField()
    type = models.CharField()
    category = models.CharField()
    users = None

    #time
    start_together = models.BooleanField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    time_limited = models.BooleanField()
    time_to_do = models.DurationField()

    #other
    random_order = models.BooleanField()
    show_result_mode = models.DecimalField() #0-instantly, 1-check button after all, 2-after the end

    check_auto = models.BooleanField()



class Question(models.Model):
    quiz = models.OneToOneField()
    figure = models.ImageField()
    content = models.CharField()
    tip = models.CharField()
    answers = None

