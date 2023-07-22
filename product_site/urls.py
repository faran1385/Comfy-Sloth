from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from django.views.generic import TemplateView

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        "",
        TemplateView.as_view(template_name='index.html')
    ),
    path(
        'product/',
        include(
            "product.urls"
        )
    ),
    path(
        'home/',
        include(
            "home_generate.urls"
        )
    ),
    path(
        'about/',
        include(
            "about.urls"
        )
    ),
    path(
        'user/',
        include(
            "user.urls"
        )
    ),
     path(
         'card/',
         include(
             "card.urls"
         )
     )

] + static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
