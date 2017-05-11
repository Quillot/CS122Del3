from django import template
from agents.models import Agent
register = template.Library()

@register.simple_tag
def get_verbose_field(field):
	field = field.replace("_", " ").title()
	return field