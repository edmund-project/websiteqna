from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, JsonResponse
from .forms import signupform, contactform
from websiteqna.models import *
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
import markdown2
import bleach




def viewquestion(request, qid, qslug):
    context = {}
    question = Question.objects.get(qid=qid, slug=qslug)

    question_json = json.loads(serializers.serialize('json', [ question ]))[0]['fields']
    question_json['date_posted'] = question.date_posted
    question_json['qid'] = question.qid
    question_json['question_detail'] = bleach.clean(markdown2.markdown(question_json['question_detail']), tags=['p', 'pre', 'code', 'sup', 'strong', 'hr', 'sub', 'a'])
    context['question'] = question_json
    context['answers'] = []
    answers = Answer.objects.filter(qid=qid)
    for answer in answers:
        answer.answer_detail = bleach.clean(markdown2.markdown(answer.answer_detail), tags=['p', 'pre', 'code', 'sup', 'strong', 'hr', 'sub', 'a'])
        context['answers'].append(answer)
    return render(request, 'viewquestion.html', context)


@csrf_exempt
def ajaxanswerquestion(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            answer = json_data['answer']
            posted_by = json_data['posted_by']
            qid = json_data['qid']
            a = Answer(answer_detail=answer, posted_by=posted_by, qid=Question.objects.get(qid=qid))
            a.save()
            return JsonResponse({'success': 'Answer has been posted!'})
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'Something went wrong!'})
    return render(request, 'viewquestion.html')        



@login_required(login_url=settings.LOGIN_URL)
def newquestion(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        detail = request.POST.get('detail')
        posted_by = request.POST.get('posted_by')
        q = Question(question_title=title, question_detail=detail, posted_by=posted_by)
        q.save()
        messages.success(request, 'question has been added!')
        return redirect('newquestion') 
    return render(request, 'newquestion.html')



def home(request):
    context = {}
    context['questions'] = Question.objects.all()
    return render(request, 'home.html', context)

 
def contact(request):
    if request.method == 'GET':
        form = contactform()
    else:
        form = contactform(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = 'FeedBack From K3QA'
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['edmundcontact123@gmail.com'], fail_silently=False)
                messages.success(request, 'Thanks for your FeedBack!')
                return redirect('contact')
            except BadHeaderError:
                return HttpResponse('invalid header found!')
            return redirect('contact')        

    return render(request, 'contact.html', {'form':form})


def signup(request):
    if request.method == 'POST':
       form = signupform(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, 'User has been successfully created!')
           return redirect('signup')

    else:
        form = signupform()
    return render(request, 'account/signup.html', {'form':form})           





def about(request):
    return render(request, 'about.html') 




