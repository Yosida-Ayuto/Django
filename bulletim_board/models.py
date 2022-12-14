from importlib.resources import contents
from pyexpat import model
from tabnanny import verbose
from turtle import title, update
from accounts.models import CustomUser
from django.db import models
# Create your models here.

class bulletim_board(models.Model):
    # 日記モデル

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)#日記の削除の時消されないようにする
    title = models.CharField(verbose_name='タイトル',max_length=40)
    content = models.TextField(verbose_name='本文', blank = True,null=True)
    photo1 = models.ImageField(verbose_name='写真1',blank=True,null=True)#blank(中身がない'')でもnull(どこにもない)でもいいよ
    photo2 = models.ImageField(verbose_name='写真2',blank=True,null=True)
    photo3 = models.ImageField(verbose_name='写真3',blank=True,null=True)
    created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='更新日時',auto_now=True)

    class Meta:
        verbose_name_plural ='bulletim_board'
    def __str__(self):#toString()
        return self.title

class Comment_Model(models.Model):
    # コメントのモデル

    user = user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)#日記の削除の時消されないようにする
    title = models.CharField(verbose_name='タイトル',max_length=40)
    content = models.TextField(verbose_name='本文', blank = True,null=True)
    created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)

    class Meta:
        verbose_name_plural ='bulletim_board'
    def __str__(self):#toString()
        return self.title
    