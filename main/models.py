from django.db import models

class Users(models.Model):
	name = models.TextField("ФИО")
	team = models.IntegerField("Отряд")
	theme = models.TextField("Тема лагеря")
	scores_personal = models.IntegerField("Личный рейтинг")

	def __str__(self) -> str:
	   return self.name
	
	class Meta:
		verbose_name_plural = 'Гости лагеря'
		
class Teams(models.Model):
    team = models.IntegerField("Отряд")
    scores_team = models.IntegerField("Баллы отряда")
    
    def __str__(self) -> str:
        return self.team
        
    class Meta:
        verbose_name_plural = 'Список отрядов'
        
class Contests(models.Model):
    contest = models.TextField("Конкурс")
    data = models.TextField("Дата проведения(сроки)")
    description = models.TextField("Описание")
    
    def __str__(self) -> str:
        return self.contest
        
    class Meta:
        verbose_name_plural = 'Конкурсы'