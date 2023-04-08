from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
  

    def __str__(self):
        return self.deptno

class Emp(models.Model):
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    empno=models.IntegerField()
    ename=models.CharField(max_length=100)
    

    def __str__(self):
        return self.empno