from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Walk(models.Model):
    created = models.DateField(auto_now_add=True)
    weather =models.CharField(verbose_name="天気",blank=True, max_length=50)
    steps =  models.PositiveIntegerField(verbose_name="歩数",blank=True, null=True)
    startpoint = models.CharField(verbose_name="出発地",blank=True, max_length=50)
    endpoint = models.CharField(verbose_name="到着地",blank=True, max_length=50)
    content = models.CharField(verbose_name="コメント",blank=True)
    image = models.ImageField(upload_to="images/uploaded/", default=None, null=True, blank=True)
    class Meta:
        verbose_name = "散歩"
        verbose_name_plural = "散歩"
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
   

