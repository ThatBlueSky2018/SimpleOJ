from django.db import models
from django.utils import timezone
from user.models import User
from problem.models import Problem


# Create your models here.
class JudgeStatus(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    problemID = models.ForeignKey(Problem, on_delete=models.CASCADE)
    result = models.IntegerField(default=-1)
    time = models.IntegerField(default=0)
    memory = models.IntegerField(default=0)
    language = models.CharField(max_length=50)
    submitTime = models.DateTimeField(default=timezone.now)
    judge = models.CharField(max_length=50, default='u')  # 该题的判题机
    code = models.TextField(max_length=200000)
    testCase = models.CharField(max_length=50, default="0")  # 在那个样例出错
    message = models.TextField(default="PENDING")  # 保存编译错误信息，运行时错误信息等

    objects = models.Manager()

    def __str__(self):
        return self.username + ' ' + self.problemID


class CaseStatus(models.Model):
    statusID = models.IntegerField()
    username = models.CharField(max_length=50)
    problemID = models.CharField(max_length=50)
    result = models.CharField(max_length=500, default="System Error")
    time = models.IntegerField(default=0)
    memory = models.IntegerField(default=0)
    testCase = models.CharField(max_length=500, default="unknown")
    caseData = models.CharField(max_length=500)
    outputData = models.CharField(max_length=500, default="")
    userOutput = models.CharField(max_length=500, default="")

    objects = models.Manager()

    def __str__(self):
        return self.statusID
