import datetime
from django.utils import timezone
from django.db import models

class Opinion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    score_int = models.IntegerField('score', default=1, null=False)

    # Lets add a str method so we understand what the question is when object is returned
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
