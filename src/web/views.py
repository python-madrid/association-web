from django.views.generic.base import View
from django.shortcuts import render_to_response
from django.template import RequestContext

from meetings.models import Meeting

class HomeView(View):
    def get(self, request):
        context = {
            'latest_meetings': Meeting.objects.all()[:5]
        }
        return render_to_response(
            'web/home.html', context,
            context_instance=RequestContext(request)
        )

