from django.db import models
from django.db.models import Count, Max

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

    # show questions in order
    class Meta:
        ordering = ['question_order']

    def getAnswers(self):
        return Answer.objects.all().filter(question_id = self.question_id)

    def getResponses(self):
        return Response.objects.all().filter(question_id = self.question_id)

    def countAnswers(self, responses):
        # count up all the different answers, groups them by answer_id, dcount
        counts = responses.values('answer_id').annotate(dcount=Count('answer_id'))

        # if there are any responses
        if len(counts) > 0:
            results = max(counts, key = lambda x: x['dcount'])['answer_id']
        else:
            return [{'answer_text': 'No responses for this question.'}]
            
        return Answer.objects.all().filter(answer_id=results)[:1]

    def getMostPopMaleAnswer(self):
        # gets all male responses
        male_responses = Response.objects.filter(answer_id__answer_text='Male').values('response_group_id')
        # pulls response objects that match any male response group id
        final_responses = Response.objects.filter(question_id = self.question_id).filter(response_group_id__in=male_responses)
        return self.countAnswers(final_responses)

    def getMostPopFemaleAnswer(self):
        # gets all female responses
        female_responses = Response.objects.filter(answer_id__answer_text='Female').values('response_group_id')
        # pulls response objects that match any female response group id
        final_responses = Response.objects.filter(question_id__survey_id=self.survey_id).filter(question_id = self.question_id).filter(response_group_id__in=female_responses)
        return self.countAnswers(final_responses)

    def __unicode__(self):
        return self.question_text

class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey('Question')
    answer_order = models.IntegerField(default=0)
    answer_text = models.CharField(max_length=200)

    # show answers in order
    class Meta:
        ordering = ['answer_order']

    def __unicode__(self):
        return self.answer_text

class Response(models.Model):
    response_id = models.AutoField(primary_key=True)
    response_group_id = models.IntegerField(default=0)
    answer_id = models.ForeignKey('Answer')
    question_id = models.ForeignKey('Question')

    def getAnswerText(self):
        return unicode(Answer.objects.all().filter(answer_id = self.answer_id))

    def getSurveyID(self):
        return unicode(Question.objects.values_list('survey_id', flat=True).filter(question_id = self.question_id))

    def getResponsesInGroup(self):
        return Response.objects.all().filter(response_group_id = self.response_group_id).filter(question_id = self.question_id)

    def __unicode__(self):
     return '%s' % (self.answer_id)