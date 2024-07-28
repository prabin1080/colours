from django.db import models

# Create your models here.


class Colour(models.Model):
    name = models.CharField(max_length=20)


class Project(models.Model):
    name = models.CharField(max_length=50)


class Paint(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    key = models.IntegerField()


class ComboEffect(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    background_colour = models.ForeignKey(Colour, on_delete=models.CASCADE, related_name='background_combo_effect')
    paint_colour = models.ForeignKey(Paint, on_delete=models.CASCADE, related_name='combo_effect')
    visible_colour = models.ForeignKey(Colour, on_delete=models.CASCADE, related_name='combo_effect')
    visibility_rate = models.IntegerField()  # 0 to 10
