from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from decimal import Decimal

register = template.Library()

@register.filter
def formataDinheiro(dinheiro):
    if dinheiro == '':
        return ''
    else:
    	try:
    		return intcomma(Decimal(dinheiro).quantize(Decimal('1.00')))
    	except:
    		return ''
    		
        