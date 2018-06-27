from django.shortcuts import render

# Create your views here.

from django.views import generic

from evnt_det.forms import EventForm
from evnt_det.models import Event

def makeentry(request):
    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            venue = request.POST.get('venue', '')
            description = request.POST.get('description', '')
            start_time = request.POST.get('start_time', '')
            end_time = request.POST.get('end_time', '')
            e = Event(name=name, venue=venue, description=description, start_time=start_time, end_time=end_time)
            e.save()
            form = EventForm()

        return render(request, 'evnt_det/makeentry.html', {'form': form})
    else:
        form=EventForm()
        return render(request, 'evnt_det/makeentry.html', {'form': form})

class IndexView(generic.ListView):

    context_object_name = 'event_list'
    template_name = 'evnt_det/index.html'

    def get_queryset(self):
        return Event.objects.all()

class DetailsView(generic.DetailView):
    model = Event
    template_name = 'evnt_det/detail.html'
    