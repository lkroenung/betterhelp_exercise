from django.db import models
from django.db.models import Count

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

    def getMostPopMaleAnswer(self):
        # gets all male responses
        x = Response.objects.filter(answer_id=1).values('response_group_id')
        # pulls response objects that match male response group id
        y = Response.objects.filter(question_id = self.question_id).filter(response_group_id__in=x)

        # count up all the different answers
        counts = y.values('answer_id').annotate(dcount=Count('answer_id'))

        counter = -1
        results = None

        for each in counts:
            if each['dcount'] >= counter:
                results = each['answer_id']
                counter = each['dcount']

        return Answer.objects.all().filter(answer_id=results)[:1]

    def getMostPopFemaleAnswer(self):
        # gets all female responses
        x = Response.objects.filter(answer_id=2).values('response_group_id')
        # pulls response objects that match female response group id
        y = Response.objects.filter(question_id = self.question_id).filter(response_group_id__in=x)

        # count up all the different answers
        counts = y.values('answer_id').annotate(dcount=Count('answer_id'))

        counter = -1
        results = None

        for each in counts:
            if each['dcount'] >= counter:
                results = each['answer_id']
                counter = each['dcount']

        return Answer.objects.all().filter(answer_id=results)[:1]

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
    response_id = models.AutoField(primary_key=True)
    response_group_id = models.IntegerField(default=0)
    answer_id = models.ForeignKey('Answer')
    question_id = models.ForeignKey('Question')
    # survey_id =  models.ForeignKey('Survey')

    def getAnswerText(self):
        return unicode(Answer.objects.all().filter(answer_id = self.answer_id))

    def getSurveyID(self):
        return unicode(Question.objects.values_list('survey_id', flat=True).filter(question_id = self.question_id))

    def getResponsesInGroup(self):
        return Response.objects.all().filter(response_group_id = self.response_group_id)

    def __unicode__(self):
     return '%s' % (self.answer_id)