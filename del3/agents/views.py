from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required

from .models import Agent
from del3.models import Invite

import random

def index(request):
	agent_list = Agent.objects.all()
	attribs = Agent._meta.fields
	return render(request, 'agents/index.html', {'agent_list': agent_list, 'attribs': attribs})

@staff_member_required
def delete_agent(request, agent_id):
	agent = Agent.objects.get(pk=agent_id)
	agent.delete()
	return HttpResponseRedirect(reverse('agents:index'))	

@staff_member_required
def generate(request):
	check = False
	code = random.randint(100000, 1000000)
	invite = Invite(invite_code=code, used=False)
	invite.save()
	agent_list = Agent.objects.all()
	attribs = Agent._meta.fields
	return render(request, 'agents/index.html', {'agent_list': agent_list, 'attribs': attribs, 'code': code})
