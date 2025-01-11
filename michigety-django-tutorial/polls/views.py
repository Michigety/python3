from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.views.decorators.http import require_http_methods

from .models import *

# generic
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# 하기 index() 뷰와 동일한 기능.
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list
#     }
#     return HttpResponse(template.render(context, request))

# 상기 index() 뷰를 render() shortcut을 사용하여 축약할 수 있음.
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return render(request, "polls/index.html", context)


# 404 호출 + render() shortcut
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist.")
#     return render(request, "polls/detail.html", {"question": question})


# 404 호출 shortcut get_object_or_404() + render() shortcut
@require_http_methods(('GET', 'POST')) # 이것도 안 먹힘
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})



# DB 값 호출 및 리다이렉트
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # choice 키가 없으면 KeyError 호출, 에러 메시지 및 현재 페이지로 리다이렉트
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        # selected_choice의 votes 값을 불러서 +1
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
    # reverse() 메소드는 주어진 인자로 URL Path 조합해 줌. 아래의 경우, /polls/<id>/results
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


