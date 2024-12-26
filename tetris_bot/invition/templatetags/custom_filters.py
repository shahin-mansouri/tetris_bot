from django import template

register = template.Library()

@register.filter
def percentage_difference(value, user_coin):
    try:
        difference = ((value - user_coin) / user_coin) * 100
        return round(difference, 2)
    except ZeroDivisionError:
        return 0


@register.filter
def compare_coin(value, user_coin):
    if user_coin > value:
        return 'increase'
    else:
        return 'decrease'
