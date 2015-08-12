from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

from core.models import Survey, Question, Answer, Response
from django.db.models import Max
from django.contrib import messages

def index(request):
    all_surveys = Survey.objects.raw('SELECT * FROM core_survey')[:]
    return render(request, 'home.html', { 'all_surveys': all_surveys })


def view_survey(request, surveyID):
    survey_obj = Survey.objects.raw('SELECT * FROM core_survey WHERE survey_id =  %s', [surveyID])[0]
    survey_questions = Question.objects.all().filter(survey_id=surveyID).order_by('question_order')
    return render(request, 'survey.html', { 'survey_data': survey_obj, 'survey_questions': survey_questions })


def submit_response(request):
    error_msg = "No POST data sent."

    if request.method == "POST":
        # grab largest group ID and increment it for these new responses
        newID = Response.objects.all().aggregate(Max('response_group_id'))['response_group_id__max'] + 1
        error_msg = "You didn't submit any answers!"
        for key in request.POST:
            if key == "surveyID":
                surveyID = request.POST[key]
            # check all keys that aren't the survey_id or the csrftoken
            elif key != "csrfmiddlewaretoken":
                error_msg = None
                # for checkboxes, more than one answer
                if request.POST.getlist(key):
                    for each in request.POST.getlist(key):
                        answer = Answer.objects.get(answer_id=each)
                        question = Question.objects.get(question_id=key)
                        newResponse = Response(response_group_id=newID, answer_id=answer, question_id=question)
                        newResponse.save()
                # for single answers
                else:
                    answer = Answer.objects.get(answer_id=request.POST[key])
                    question = Question.objects.get(question_id=key)
                    newResponse = Response(response_group_id=newID, answer_id=answer, question_id=question)
                    newResponse.save()
    if error_msg:
        messages.error(request, error_msg)
    return HttpResponseRedirect('/results/'+ surveyID +'/')


def view_results(request, surveyID):
    survey_obj = Survey.objects.raw('SELECT * FROM core_survey WHERE survey_id =  %s', [surveyID])[0]
    survey_questions = Question.objects.all().filter(survey_id=surveyID).order_by('question_order')
    # show popular answers for the base survey
    showPopular = True if survey_obj.survey_id == 1 else False
    return render(request, 'results.html', { 'survey_data': survey_obj, 'survey_questions': survey_questions, 'showPopular':showPopular })