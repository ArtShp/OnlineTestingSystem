from django.db import models
from django.utils import timezone

# HELP TEXT

class Quiz(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100, blank=False)
    pub_date = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now)
    description = models.CharField(verbose_name='Описание', max_length=200, blank=True)

    # figure = models.ImageField()
    # type = models.CharField(max_length=50, blank=True)

    # create class Category for Quiz and Question
    # category = models.CharField(max_length=50, blank=True)

    # attempts_limited = models.BooleanField()
    # max 999 attempts
    # attempts = models.DecimalField(max_digits=3, decimal_places=0)

    # subject = None
    # author = None # create class

    # quiz_creator can choose: student(s), class(es), parallel(s), all(school)
    # users = None # create class

    """
    time
    
    start_together = models.BooleanField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    time_limited = models.BooleanField()
    time_to_do = models.DurationField()
    """

    random_order = models.BooleanField(verbose_name='Перемешать вопросы')

    # 0-instantly, 1-check button after all, 2-after the end
    # show_result_mode = models.DecimalField(max_digits=1, decimal_places=0)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, verbose_name='Тест', on_delete=models.CASCADE)
    content = models.CharField(verbose_name='Вопрос', max_length=300, blank=False)

    # figure = models.ImageField()
    # tip = models.CharField(max_length=100, blank=True)

    # quiz_creator can choose: one from many, many from many, field(s) to fill
    # answers = None # create class

    def __str__(self):
        return self.content


class Category(models.Model):
    pass


class Author(models.Model):
    pass


class User(models.Model):
    pass


class Answer(models.Model):
    pass
