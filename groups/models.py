from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

users = User


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    start_date = models.DateField()
    end_date = models.DateField()
    study_days = models.IntegerField()
    students_count = models.IntegerField()

    class Meta:
        verbose_name='Курс'
        verbose_name_plural='Курсы'

    def __str__(self):
        return self.name


class Stream(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    real_start_date = models.DateField()
    real_end_date = models.DateField()
    accepted = models.BooleanField(default=False)
    max_members = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name='Поток'
        verbose_name_plural='Потоки'


    def __str__(self):
        return f"{self.course.name} Stream"


class Group(models.Model):
    name = models.CharField(max_length=255)
    students_count = models.IntegerField()
    student = models.ManyToManyField(users, blank=True)
    stream = models.ForeignKey("Stream", on_delete=models.CASCADE)

    class Meta:
        verbose_name='Группа'
        verbose_name_plural='Группы'


    def str(self):
        return self.name


# def sort_students(request):
#   # course = Course.objects.get()
#   # stream = Stream.objects.filter(course=course)
#   # group = Group.objects.get(stream=stream)
#   if Stream.max_members > Group.students_count:
#         Stream.students_count += 1
#         Stream.save()
#         # group = Group.objects.create()
#         Group.students.add(request.user)
#         Group.save()
#       Необходимо объединить группы в потоки, с количеством учащихся не более n_max.
# Количество потоков должно получится минимальным.
# Срок обучения потока не должен выходить за диапазон каждой из включенных в него, групп, с учтем выходных дней.
# Группа включается только в один поток.
# Обучение в потоке не содержит разрывов,  кроме выходных дней и праздников.

# Поток — таблица в базе данных, содержащая поля:
# id потока
# id курса,
# реальный период обучения (дата начала, дата окончания).


# Полученный список потоков отображается в интерфейсе методиста, где имеется возможность принять или не принять  объединение в поток, для каждой из групп.
# После каждого действия в интерфейсе
