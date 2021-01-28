from django.db import models


#  所有models  父类
class BaseModel(models.Model):
    is_show = models.BooleanField(default=True, verbose_name='是否显示')
    orders = models.IntegerField(default=1, verbose_name='排序')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    class Meta:
        # 抽象表  不在数据库中生成
        abstract = True
