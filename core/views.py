from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

from core.models import Survey, Question, Answer, Response

def index(request):
    all_surveys = Survey.objects.raw('SELECT * FROM core_survey')[:]
    return render(request, 'home.html', { 'all_surveys': all_surveys })


def view_survey(request, surveyID):
    survey_obj = Survey.objects.raw('SELECT * FROM core_survey WHERE survey_id =  %s', [surveyID])[0]
    survey_questions = Question.objects.all().filter(survey_id=surveyID).order_by('question_order')
    return render(request, 'survey.html', { 'survey_data': survey_obj, 'survey_questions': survey_questions })


def submit_response(request):
    if request.method == "POST":
        for key in request.POST:
            if key != "csrfmiddlewaretoken":
                # for check all that apply
                if request.POST.getlist(key):
                    for each in request.POST.getlist(key):
                        answer = Answer.objects.get(answer_id=each)
                        question = Question.objects.get(question_id=key)
                        newResponse = Response(answer_id=answer, question_id=question)
                        newResponse.save()
                else:
                    answer = Answer.objects.get(answer_id=request.POST[key])
                    question = Question.objects.get(question_id=key)
                    newResponse = Response(answer_id=answer, question_id=question)
                    newResponse.save()

    # TODO: need to get survey_id here
    return HttpResponseRedirect('/results/1/')


def view_results(request, surveyID):
    # doing this per question, so i have a question to start from
    # find all responses to this question, question_id = question_id
    # Response.objects.all().filter(question_id__question_id = question_id)
    #       join those responses with responses where question_id__question_text='What is your gender?' so a.reponse_group_id == b.reponse_group_id
    #       count responses where answer_id__answer_text='Male' or 'Female'

    survey_obj = Survey.objects.raw('SELECT * FROM core_survey WHERE survey_id =  %s', [surveyID])[0]
    survey_questions = Question.objects.all().filter(survey_id=surveyID).order_by('question_order')
    return render(request, 'results.html', { 'survey_data': survey_obj, 'survey_questions': survey_questions })