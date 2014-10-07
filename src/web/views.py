from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect

from meetings.models import Meeting

class HomeView(View):
    def get(self, request):
        context = {
            'latest_meetings': Meeting.objects.all().order_by('-datetime')[:5]
        }
        return render_to_response(
            'web/home.html', context,
            context_instance=RequestContext(request)
        )

class RedirectPostView(View):
    def get(self, request, slug):
        return HttpResponseRedirect(reverse('meetings:meeting', args=[slug]))

