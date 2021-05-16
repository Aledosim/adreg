from math import floor


class Views:
    value = None
    isChanged = None
    clicks = None
    shares = None


def initial_views(invest):
    # Return the initial views, without clicks
    return int(0.3 * invest)


def click_count(views_count):
    return floor(views_count * 3 / 25)


def share_count(clicks):
    return floor(clicks * 3 / 20)


def update_views(views):
    clicks = click_count(views.value)
    shares = share_count(clicks)

    views.clicks = clicks

    if shares > views.shares and shares >= 1:
        views.value += 40 * (shares - views.shares)
        views.isChanged = True
        views.shares = shares
    else:
        views.isChanged = False


def calculator(investment):
    views = Views()
    views.value = initial_views(investment)
    views.isChanged = True
    views.clicks = 0
    views.shares = 0

    layer = 1
    while views.isChanged and layer <= 3:
        update_views(views)
        layer += 1

    views.clicks = click_count(views.value)
    views.shares = share_count(views.clicks)

    return views.value, views.clicks, views.shares
