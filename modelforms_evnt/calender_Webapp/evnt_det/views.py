from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from evnt_det.models import Event

class IndexView(generic.ListView):

    context_object_name = 'event_list'
    template_name = 'evnt_det/index.html'

    def get_queryset(self):
        sortby_starttime = sorted(Event.objects.all(), key=lambda x: x.event_starttime, reverse=False)
        return sortby_starttime

class DetailView(generic.DetailView):
    model = Event
    template_name = 'evnt_det/detail.html'

class EventEntry(CreateView):
    model = Event #upon this function being triggered the forms is automatically generated and its template can be defined by the name event_form.html
    # the fields mentioned below become the entry rows in the generated form
    fields = ['event_name', 'event_venue', 'event_description', 'event_starttime', 'event_endtime']

class EventUpdate(UpdateView):
    model = Event
    fields = ['event_name', 'event_venue', 'event_description', 'event_starttime', 'event_endtime']

class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('evnt_det:index')