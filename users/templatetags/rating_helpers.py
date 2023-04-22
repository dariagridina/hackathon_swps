from django import template

register = template.Library()


@register.filter
def rating_star_class(rating, value):
    rating = float(rating)
    value = float(value)
    if rating >= value:
        return "bxs-star"
    elif rating >= value - 0.5:
        return "bxs-star-half"
    else:
        return "bx-star"
