from django.db import models

class usersprofile(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length = 32)
    password = models.CharField(max_length = 32, default='')
    usertype = models.CharField(max_length = 32)
    emailAddress = models.CharField(max_length = 32)
    groupNum = models.CharField(max_length = 32)
    
    class Meta:
        verbose_name = 'User Information'
        verbose_name_plural = verbose_name
        db_table = 'Users'

    def __str__(self):
        return self.username  
    
class Question(models.Model):
    content = models.TextField(verbose_name=u"QuestionDescription")
    equation = models.TextField(verbose_name=u"QuestionEquation")
    answer = models.TextField(verbose_name=u"RightAnswer")
    score = models.IntegerField(verbose_name=u"Marks", default=0)
    note = models.TextField(verbose_name=u"CandidateAnswer", default= u"Answer: ")
    boolt = models.CharField(max_length = 32, verbose_name=u"DetermineTrue", default= "True")
    boolf = models.CharField(max_length = 32, verbose_name=u"DeterminFalse", default= "False")

    class Meta:
        verbose_name = u"questions"
        verbose_name_plural = verbose_name

    def get_content_display(self, field):
        return self.content

    def __unicode__(self):
        model = Question
        return "(Question:{0}{1} | Answer:{2} )".format( self.content,self.equation, self.answer)


class PaperList(models.Model): 
    name = models.CharField(max_length=50, verbose_name=u"papername", default=u"")
    is_allow = models.BooleanField(default=False, verbose_name=u"if_tested")

    class Meta:
        verbose_name = u"PaperList"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u"(PaperName:{0} | if_tested:{1})".format(self.name, self.is_allow)

class Paper(models.Model):
    question = models.ForeignKey(Question, verbose_name=u"Question",on_delete=models.CASCADE)
    paperName = models.ForeignKey(PaperList, verbose_name=u"PaperName",on_delete=models.CASCADE)

    class Meta:
        verbose_name = u"Papers"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u"{0} ({1})".format(self.paperName, self.question.content)

class UserResult(models.Model):
    user = models.ForeignKey(usersprofile, verbose_name=u"Candidate",on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper,verbose_name=u"Paper",on_delete=models.CASCADE)
    answer = models.TextField(verbose_name=u"CandidateAnswer")
    score = models.IntegerField( verbose_name=u"Score", default=0)

    class Meta:
        verbose_name = u"UserResult"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "{0}({1}) score={2}".format(self.user,self.paper,self.score)
 