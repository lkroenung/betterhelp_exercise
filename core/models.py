from django.db import models

# Create your models here.

class Survey(models.Model):
    survey_id = models.AutoField(primary_key=True)
    survey_name = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s' % (self.survey_id, self.survey_name)

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    survey_id = models.ForeignKey('Survey')
    question_type = models.CharField(max_length=20)
    question_order = models.IntegerField()
    question_text = models.CharField(max_length=200, default="Question text.")

    def getAnswers(self):
        return Answer.objects.all().filter(question_id = self.question_id)

    def getResponses(self):
        return Response.objects.all().filter(question_id = self.question_id)

    def __unicode__(self):
        return self.question_text
        # return u'%s %s' % (self.question_id, self.survey_id, self.question_text)

class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey('Question')
    answer_text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.answer_text
        # return u'%s %s' % (self.answer_id, self.question_id, self.answer_text)

class Response(models.Model):
    reponse_id = models.AutoField(primary_key=True)
    answer_id = models.ForeignKey('Answer')
    question_id = models.ForeignKey('Question')
    # survey_id =  models.ForeignKey('Survey')

    def getAnswerText(self):
        return unicode(Answer.objects.all().filter(answer_id = self.answer_id))

    def getSurveyID(self):
        return unicode(Question.objects.values_list('survey_id', flat=True).filter(question_id = self.question_id))

    def __unicode__(self):
     return 'Answer: %s' % (self.answer_id)