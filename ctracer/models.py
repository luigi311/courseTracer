from django.db import models

# Create your models here.

class courseInfo(models.Model):
    termCode = models.IntegerField()
    termDescr = models.TextField()
    crn = models.IntegerField()
    subj = models.TextField(max_length=2)
    courseNum = models.IntegerField()
    section = models.IntegerField()
    scheduleDesc = models.TextField()
    title = models.TextField()
    maxEnroll = models.IntegerField()
    actEnroll = models.IntegerField()

    def getPrompt(self):
        return self.prompt
 
    def __unicode__(self):
       return self.prompt

    #class Meta:
    #    abstract = True
