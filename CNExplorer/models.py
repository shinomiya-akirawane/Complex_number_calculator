from django.db import models

class usersprofile(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length = 32)
    password = models.CharField(max_length = 32, default='')
    usertype = models.CharField(max_length = 32)
    emailAddress = models.CharField(max_length = 32)
    groupNum = models.ForeignKey('Groups', related_name = 'userGroup', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'User Information'
        verbose_name_plural = verbose_name
        db_table = 'Users'

    def __str__(self):
        return self.username
       
class Groups(models.Model):
    id = models.AutoField(primary_key=True)
    groupName = models.CharField(max_length = 32)
    groupCode = models.CharField(max_length = 32, default='')

    class Meta:
        verbose_name = 'Group Information'
        verbose_name_plural = verbose_name
        db_table = 'Groups'
        
    def __str__(self):
        return self.username
    
    
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(verbose_name=u"QuestionDescription")
    equation = models.TextField(verbose_name=u"QuestionEquation")
    answer = models.TextField(verbose_name=u"RightAnswer")

    class Meta:
        verbose_name = u"questions"
        verbose_name_plural = verbose_name

    def get_content_display(self, field):
        return self.content

    def __unicode__(self):
        model = Question
        return "(Question:{0}{1} | Answer:{2} )".format( self.content,self.equation, self.answer)

class QuestionDatabase(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(verbose_name=u"QuestionDescription")
    equation = models.TextField(verbose_name=u"QuestionEquation")
    answer = models.TextField(verbose_name=u"RightAnswer")

    class Meta:
        verbose_name = u"QuestionDatabase"
        verbose_name_plural = verbose_name

class PaperList(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=50, verbose_name=u"papername", default=u"")
    is_allow = models.BooleanField(default=False, verbose_name=u"if_tested")
    groupNum = models.ForeignKey('Groups', related_name = 'paper_Group', on_delete=models.CASCADE)
    is_attempted = models.CharField(max_length = 32, verbose_name = u"paperstatus", default = u"")
    startQuestionID = models.CharField(max_length = 32, default='')


    class Meta:
        verbose_name = u"PaperList"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u"(PaperName:{0} | if_tested:{1})".format(self.name, self.is_allow)

class Paper(models.Model):
    id = models.AutoField(primary_key=True)
    question =     question = models.ForeignKey(Question, verbose_name=u"Question",on_delete=models.CASCADE)

    PaperListID = models.ForeignKey(PaperList, verbose_name=u"PaperName",on_delete=models.CASCADE)

    class Meta:
        verbose_name = u"Papers"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u"{0} ({1})".format(self.paperName, self.question.content)

class CandidateResult(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, verbose_name=u"Question",on_delete=models.CASCADE)
    user = models.ForeignKey(usersprofile, verbose_name=u"Candidate",on_delete=models.CASCADE )
    answer = models.TextField(verbose_name=u"CandidateAnswer")
    paper = models.ForeignKey(PaperList,verbose_name=u"Paper",on_delete=models.CASCADE)

    class Meta:
        verbose_name = u"CandidateResult"
        verbose_name_plural = verbose_name