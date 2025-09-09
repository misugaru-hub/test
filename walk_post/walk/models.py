from django.db import models

# Create your models here.
class Walk(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    weather =models.CharField(verbose_name="天気",blank=True, max_length=50)
    steps =  models.PositiveIntegerField(verbose_name="歩数",blank=True, null=True)
    startpoint = models.CharField(verbose_name="出発地",blank=True, max_length=50)
    startpoint = models.CharField(verbose_name="到着地",blank=True, max_length=50)
    content = models.TextField(verbose_name="コメント",blank=True)
    distance = models.PositiveIntegerField(verbose_name="距離",blank=True, null=True)

    class Meta:
        verbose_name = "散歩"
        verbose_name_plural = "散歩"
    
   

