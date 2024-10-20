from django.db import models
from django.db.models import Count, Q



class Student(models.Model):
    img = models.ImageField(blank=True,verbose_name="Фотография")
    name = models.CharField(max_length=45,verbose_name="Имя студента")
    surname = models.CharField(max_length=45,verbose_name="Фамилия студента")
    point = models.IntegerField(verbose_name="Балы",editable=False,blank=True,null=True,default=0)
    number = models.CharField(max_length=25,blank=False,verbose_name="Номер студента")
    place_rating = models.PositiveIntegerField(default=0,blank=True,editable=True)
    def __str__(self):
        return self.name

    @staticmethod
    def sorted_by_truancy_count():

        return Student.objects.annotate(
            truancy_count=Count('truancie', filter=Q(truancie__cause__isnull=True) | Q(truancie__cause=''))
        ).order_by('-truancy_count')

    def truancy_count(self):

        return self.truancie_set.count()

    class Meta:
        verbose_name_plural = "Студенты"
        verbose_name = "Студент"

class Truancie(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,verbose_name="Студент")
    date = models.DateField(blank=False,verbose_name="Дата")
    cause = models.TextField(blank=True,null=True,verbose_name="Причина прогула")

    def __str__(self):
        return self.student.name

    class Meta:
        verbose_name_plural = "Прогулы студентов"

