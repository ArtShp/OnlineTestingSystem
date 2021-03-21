import datetime
from django.db import models
from django.utils import timezone

"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
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
    """general"""
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200, blank=True)
    figure = models.ImageField()
    type = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50, blank=True)
    attempts_limited = models.BooleanField()
    # max 999 attempts
    attempts = models.DecimalField(max_digits=3, decimal_places=0)

    # must be inherited from quiz_creator
    subject = None
    author = None

    # quiz_creator can choose: student(s), class(es), parallel(s), all(school)
    users = None

    """time"""
    start_together = models.BooleanField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    time_limited = models.BooleanField()
    time_to_do = models.DurationField()

    """other"""
    random_order = models.BooleanField()
    # 0-instantly, 1-check button after all, 2-after the end
    show_result_mode = models.DecimalField(max_digits=1, decimal_places=0)

    check_auto = models.BooleanField()



class Question(models.Model):
    quiz = models.OneToOneField(Quiz)
    figure = models.ImageField()
    content = models.CharField(max_length=300, blank=False)
    tip = models.CharField(max_length=100, blank=True)

    # quiz_creator can choose: one from many, many from many, field(s) to fill
    answers = None

