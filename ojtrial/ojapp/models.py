from django.db import models


class Problem(models.Model):
    Statement = models.CharField(max_length=2000)
    Name = models.CharField(max_length=100)
    Code = models.CharField(max_length=50)
    Difficulty = models.CharField(max_length=10)


class Solutions(models.Model):
    Problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    Verdict = models.CharField(max_length=50)
    SubmittedAt = models.DateTimeField('Date and Time Submitted')

class TestCases(models.Model):
    Input = models.CharField(max_length=2000)
    Output = models.CharField(max_length=2000)
    Problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    