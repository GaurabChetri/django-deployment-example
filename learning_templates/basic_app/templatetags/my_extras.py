from django import template

register = template.Library()

@register.filter(name="cut")
def cut(value,arg):
    """
    This cuts out all the values in arg

    """
    return value.replace(arg,"")

register.filter('cut',cut)
