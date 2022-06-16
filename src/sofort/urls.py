from django.contrib import admin
from django.urls import path, include

# b: bookmarks
# d: (documentation)
# f: forums
# i: interests
# ISSUES
# l: links
# m: members
# n: newsletters
# p: pages
# q: questions
# s: issues
# t: tags
# u: tutorials
# w: (wiki)

urlpatterns = [
    path('', include('core.urls')),
    path('i/', include('interests.urls')),
    path('p/', include('pages.urls')),
    path('q/', include('questions.urls')),

    path('admin/', admin.site.urls),
]
