from django.db import models
from django.utils import timezone

# HELP TEXT - в админке под полем ввода находится подсказка.
'''
class Category(models.Model):
    category_name = models.CharField(verbose_name='Категория', max_length=100, blank=True, null=True)
'''


class Subject(models.Model):
    subject_name = models.CharField(verbose_name='Предмет(ы)', max_length=50, default=' ', blank=False)


class Classes(models.Model):
    level = models.IntegerField(verbose_name='Уровень', default=' ', blank=False)
    letter = models.CharField(verbose_name='Буква', max_length=1, default=' ', blank=False)
    subjects = models.ManyToManyField(Subject, verbose_name='Предмет(ы)')


class Student(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50, default=' ', blank=False)
    surname = models.CharField(verbose_name='Фамилия', max_length=50, default=' ', blank=False)
    # patronymic = father name
    patronymic = models.CharField(verbose_name='Отчество', max_length=50, blank=True, null=True)
    phone = models.CharField(verbose_name='Номер телефона', max_length=50, blank=True, null=True)
    email = models.EmailField(verbose_name='Email', max_length=100, blank=True, null=True)
    password = models.CharField(verbose_name='Пароль', max_length=50, default='1337', blank=False)
    # photo = models.ImageField()
    learn_class = models.ForeignKey(Classes, verbose_name='Класс', default=' ', on_delete=models.CASCADE)


class Teacher(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50, default=' ', blank=False)
    surname = models.CharField(verbose_name='Фамилия', max_length=50, default=' ', blank=False)
    # patronymic = father name
    patronymic = models.CharField(verbose_name='Отчество', max_length=50, blank=True, null=True)
    phone = models.CharField(verbose_name='Номер телефона', max_length=50, blank=True, null=True)
    email = models.EmailField(verbose_name='Email', max_length=100, blank=True, null=True)
    password = models.CharField(verbose_name='Пароль', max_length=50, default='1337', blank=False)
    # photo = models.ImageField()
    subjects = models.ManyToManyField(Subject, verbose_name='Предмет(ы)')
    teach_class = models.ManyToManyField(Classes, verbose_name='Класс(ы)')

'''
class Admin(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50, default=' ', blank=False)
    surname = models.CharField(verbose_name='Фамилия', max_length=50, default=' ', blank=False)
    # patronymic = father name
    patronymic = models.CharField(verbose_name='Отчество', max_length=50, default=' ', blank=False)
    # photo = models.ImageField()
'''

class Quiz(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100, default=' ', blank=False)
    description = models.CharField(verbose_name='Описание', max_length=200, blank=True, null=True)
    # category = models.ForeignKey(Category, verbose_name='Категория')
    # Доработать: создателем может быть не только учитель, надо это как-то наследовать
    # creator = models.ForeignKey(Teacher, verbose_name='Создатель')
    # subjects = creator.subjects
    # Доработать: должно работать иерархическим списком
    #students = models.ManyToManyField(Student, verbose_name='Ученик(и)')

    # figure = models.ImageField()
    # type = models.CharField(max_length=50, blank=True, null=True)

    # attempts_limited = models.BooleanField()
    # max 999 attempts
    # attempts = models.DecimalField(max_digits=3, decimal_places=0)

    """
    time
    
    start_together = models.BooleanField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    time_limited = models.BooleanField()
    time_to_do = models.DurationField()
    """

    pub_date = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now)
    random_order = models.BooleanField(verbose_name='Перемешать вопросы', default=False)

    # 0-instantly, 1-check button after all, 2-after the end
    # show_result_mode = models.DecimalField(max_digits=1, decimal_places=0)
    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, verbose_name='Тест', default=' ', on_delete=models.CASCADE)
    content = models.CharField(verbose_name='Вопрос', max_length=300, default=' ', blank=False)
    # category = models.ForeignKey(Category, verbose_name='Категория')

    # figure = models.ImageField()
    # tip = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.content


class Answer(models.Model):
    question = models.ForeignKey(Question, verbose_name='Вопрос', default=' ', on_delete=models.CASCADE)
    content = models.CharField(verbose_name='Ответ', max_length=50, default=' ', blank=False)
    # Доработать: могут ввести несколько правильных ответов
    is_correct = models.BooleanField(verbose_name='Ответ правильный?', default=False)

    def __str__(self):
        return self.content


class AnsweredQuiz(models.Model):
    quiz = models.ForeignKey(Quiz, verbose_name='Тест', default=' ', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Имя', max_length=50, default=' ', blank=False)

    def __str__(self):
        return self.name
