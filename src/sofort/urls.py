from django.contrib import admin
from django.urls import path, include
from filebrowser.sites import site as fb_site

from django.conf.urls.static import static
from django.conf import settings

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


# fb_site.storage.location = settings.BASE_DIR.
print(f"storage location: {fb_site.storage.location}")
fb_site.storage.location = settings.MEDIA_ROOT
fb_site.directory = "upload/"


urlpatterns = [
    path('admin/filebrowser/', fb_site.urls),
    path('grappelli/', include('grappelli.urls')),
    
    path('', include('core.urls')),
    path('i/', include('interests.urls')),
    path('p/', include('pages.urls')),
    path('q/', include('questions.urls')),

    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
