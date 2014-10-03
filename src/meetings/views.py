from django.views.generic.base import View
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from meetings.models import Meeting

import datetime

class MeetingsView(View):
    def get(self, request, year=None):
        meetings = Meeting.objects.all().order_by('-datetime')
        if year:
            meetings = meetings.filter(datetime__year=year)
        else:
            current_year = datetime.datetime.today().year
            meetings = meetings.filter(datetime__year=current_year)
        context = {
            'meetings': meetings
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
