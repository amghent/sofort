from django.urls import reverse

###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions
###


def get_sidebar(slug: str) -> list:
    from interests import views as interests_views
    from questions import views as questions_views

    sb = [
        {"href": reverse(interests_views.interest_group_detail, args=[slug]), "title": "Dashboard"},
        {"href": reverse(interests_views.interest_group_under_construction, args=[slug]), "title": "Bookmarks"},
        {"href": reverse(questions_views.index, args=[slug]), "title": "Questions"},
        {"href": reverse(interests_views.interest_group_under_construction, args=[slug]), "title": "Issues"},
        {"href": reverse(interests_views.interest_group_under_construction, args=[slug]), "title": "Forums"},
        {"href": reverse(interests_views.interest_group_under_construction, args=[slug]), "title": "Tutorials"},
        {"href": reverse(interests_views.interest_group_under_construction, args=[slug]), "title": "Newsletters"},
        {"href": reverse(interests_views.interest_group_under_construction, args=[slug]), "title": "Tags"},
        {"href": reverse(interests_views.interest_group_under_construction, args=[slug]), "title": "Links"},
        {"href": reverse(interests_views.interest_group_about, args=[slug]), "title": "About"},
    ]

    return sb
    
