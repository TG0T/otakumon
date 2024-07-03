from django import template

register = template.Library()

def formatonumero(value):
    return "{:,}".format(value).replace(",", ".")

register.filter('formatonumero', formatonumero)