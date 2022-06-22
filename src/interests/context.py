from django.urls import reverse

###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions
###


def get_sidebar(slug):
    from interests import views as interests_views
    from pages import views as pages_views
    from questions import views as questions_views

    sb = [
        {"href": reverse(interests_views.interest_group_detail, args=[slug]), "title": "Dashboard"},
        {"href": reverse(pages_views.detail, args=["under_construction"]), "title": "Bookmarks"},
        {"href": reverse(questions_views.index, args=[slug]), "title": "Questions"},
        {"href": reverse(pages_views.detail, args=["under_construction"]), "title": "Issues"},
        {"href": reverse(pages_views.detail, args=["under_construction"]), "title": "Forums"},
        {"href": reverse(pages_views.detail, args=["under_construction"]), "title": "Tutorials"},
        {"href": reverse(pages_views.detail, args=["under_construction"]), "title": "Newsletters"},
        {"href": reverse(pages_views.detail, args=["under_construction"]), "title": "Tags"},
        {"href": reverse(pages_views.detail, args=["under_construction"]), "title": "Links"},
        {"href": reverse(interests_views.interest_group_about, args=[slug]), "title": "About"},
    ]

    return sb
    
