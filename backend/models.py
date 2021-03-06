from django.db import models
from django.utils import timezone


class User(models.Model) :
    user_seq = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=30,null=False)
    password = models.CharField(max_length=40, null=False)
    name = models.CharField(max_length=20)
    ph = models.CharField(max_length=20, default='0')
    user_role = models.CharField(max_length=20,default='U',editable = False)
    delete_yn = models.CharField(max_length=20,default='N',editable = False)
    create_date = models.DateTimeField(default=timezone.now())
    modify_date = models.DateTimeField(auto_now=True, null=True)

    def publish(self):
        self.modify_date = timezone.now()
        self.save()

    class Meta:
      db_table = "User"

class Board(models.Model):
    board_seq = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=30,null=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    modify_date = models.DateTimeField(auto_now_add=True, null=True)

    def publish(self):
        self.modify_date = timezone.now()
        self.save()

    class Meta:
      db_table = "Board"