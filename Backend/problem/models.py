from django.db import models
import uuid


# Create your models here.
class Problem(models.Model):
    id = models.CharField(max_length=36, default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    input = models.TextField()
    output = models.TextField()
    inputExample = models.TextField()  # 测试用例输入,中间用'#'隔开
    outputExample = models.TextField()  # 测试用例输出,中间用'#'隔开
    timeLimit = models.IntegerField()  # Ms
    memoryLimit = models.IntegerField()  # Byte

    objects = models.Manager()

    def __str__(self):
        return self.title
