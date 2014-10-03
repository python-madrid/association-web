from django.views.generic.base import View
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from meetings.models import Meeting

class MeetingsView(View):
    def get(self, request):
        context = {
            'meetings': Meeting.objects.all().order_by('-datetime')
        }
        return render_to_response(
            'meetings/meetings.html', context,
            context_instance=RequestContext(request)
        )

class MeetingView(View):
    def get(self, request, slug):
        context = {
            'meeting': get_object_or_404(Meeting, slug=slug)
        }
        return render_to_response(
            'meetings/meeting.html', context,
            context_instance=RequestContext(request)
        )
