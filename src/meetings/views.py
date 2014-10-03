from django.views.generic.base import View
from django.shortcuts import render_to_response
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

