from django.db import models
from django.contrib.auth.models import User

users = User

# курс
class Course(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_data = models.DateField()
    study_days = models.IntegerField()
    students_count = models.IntegerField()


    def __str__(self):
        return self.name
    

# поток
class Stream(models.Model):
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    real_start_date = models.DateField()
    real_end_date = models.DateField()
    accepted = models.BooleanField(default=False)
    group_count = models.IntegerField(default=0)
    groups = models.ManyToManyField('Group')


    def __str__(self):
        return f'{self.course.name} Поток'


# группы
class Group(models.Model):
    name = models.CharField(max_length=255)
    student_count = models.IntegerField()
    student = models.ManyToManyField(users)

    def __str__(self):
        return self.name
    



# Необходимо объединить группы в потоки, с количеством учащихся не более n_max.
# Количество потоков должно получится минимальным.
# Срок обучения потока не должен выходить за диапазон каждой из включенных в него, групп, с учтем выходных дней.
# Группа включается только в один поток.
# Обучение в потоке не содержит разрывов,  кроме выходных дней и праздников.

# Поток — таблица в базе данных, содержащая поля:
# id потока
# id курса,
# реальный период обучения (дата начала, дата окончания).


# Полученный список потоков отображается в интерфейсе методиста, где имеется возможность принять или не принять  объединение в поток, для каждой из групп.
# После каждого действия в интерфейсе, отображаемый список перестраивается и визуализация меняется без полной перезагрузки станицы.