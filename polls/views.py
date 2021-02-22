from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from .models import Choice, Question, Thoughts

class ThoughtsView(generic.ListView):
    model = Thoughts
    template_name = 'polls/thoughts.html'

class ThoughtsListView(generic.ListView):
    model = Thoughts
    template_name = 'polls/thoughts/list.html'
    def get_queryset(self):
        """Return the last five published questions."""
        return Thoughts.objects.all()

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter( pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def submitThought(request):
    if request.method == 'POST':
        thought_text_val = request.POST['thoughtText']
        thought_title_val = request.POST['thoughtTitle']

        newThought = Thoughts(thought_title = thought_title_val, thought_text = thought_text_val)
        newThought.save()
        return HttpResponse("Successfully submitted!")

def vote(request, question_id):
    print("here")
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))