from django.db import models




#we can created normal function based validators in forms.py or models.py
class SchoolInfo(models.Model):
    scname=models.CharField(max_length=100)
    sclocation=models.CharField(max_length=100)
    subjects=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.subjects


class StudentInfo(models.Model):
    subjects=models.ForeignKey(SchoolInfo,on_delete=models.CASCADE) #based on the parent table primary key column data i need to insert the data in child table
    stname=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    age=models.IntegerField()
    stlocation=models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.age)
