from django.db import models
from datetime import datetime
from users.models import Users


class Question(models.Model):
    content = models.TextField(verbose_name=u"QuestionDescription")
    equation = models.TextField(verbose_name=u"QuestionEquation")
    answer = models.TextField(verbose_name=u"RightAnswer")
    choice_a = models.CharField(max_length=32, verbose_name=u"ChoiceA", default="A.")
    choice_b = models.CharField(max_length=32, verbose_name=u"ChoiceB", default="B.")
    choice_c = models.CharField(max_length=32, verbose_name=u"ChoiceC", default="C.")
    choice_d = models.CharField(max_length=32, verbose_name=u"ChoiceD", default="D.")
    score = models.IntegerField(verbose_name=u"Marks", default=0)
    note = models.TextField(verbose_name=u"CandidateAnswer", default=u"Answer: ")
    boolt = models.CharField(max_length=32, verbose_name=u"DetermineTrue", default="True")
    boolf = models.CharField(max_length=32, verbose_name=u"DeterminFalse", default="False")
    createTime = models.DateField(default=datetime.now, verbose_name=u"CreateTime")

    class Meta:
        verbose_name = u"questions"
        verbose_name_plural = verbose_name

    def get_content_display(self, field):
        return self.content

    def __unicode__(self):
        model = Question
        return "(Question:{0}{1} | Answer:{2} )".format(self.content, self.equation, self.answer)


class PaperList(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"papername", default=u"")
    is_allow = models.BooleanField(default=False, verbose_name=u"if_tested")
    createTime = models.DateField(default=datetime.now, verbose_name=u"CreateTime")

    class Meta:
        verbose_name = u"PaperList"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u"(PaperName:{0} | if_tested:{1})".format(self.name, self.is_allow)


class Paper(models.Model):
    question = models.ForeignKey(Question, verbose_name=u"Question", on_delete=models.CASCADE)
    paperName = models.ForeignKey(PaperList, verbose_name=u"PaperName", on_delete=models.CASCADE)
    createTime = models.DateField(default=datetime.now, verbose_name=u"CreateTime")

    class Meta:
        verbose_name = u"Papers"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u"{0} ({1})".format(self.paperName, self.question.content)
