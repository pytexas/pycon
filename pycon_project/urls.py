from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to

from django.contrib import admin
admin.autodiscover()

from pinax.apps.account.openid_consumer import PinaxConsumer

from pycon_project.views import creole_preview


handler500 = "pinax.views.server_error"


# url pattern overrides
urlpatterns = patterns("",
    url(r"^$", redirect_to, {"url": "/%s/"  % settings.PYCON_YEAR}),
    url(r"^%s/" % settings.PYCON_YEAR, include(patterns("",
        url(r"^$", direct_to_template, {"template": "homepage.html"}, name="home"),
        url(r"^account/signup/$", "pinax.apps.account.views.signup", name="acct_signup"),
        url(r"^account/", include("pinax.apps.account.urls")),
        url(r"^schedule/", include("symposion.schedule.urls")),
        url(r"^admin/", include(admin.site.urls)),
        url(r"^about/$", direct_to_template, {"template": "pytexas/about.html"}, name="about"),
        url(r"^sponsor/$", direct_to_template, {"template": "pytexas/sponsor.html"}, name="sponsor"),
        url(r"^registration/$", direct_to_template, {"template": "pytexas/registration.html"}, name="registration"),
        url(r"^surveys/$", direct_to_template, {"template": "pytexas/surveys.html"}, name="surveys"),
        url(r"^community/$", direct_to_template, {"template": "pytexas/community.html"}, name="community"),
        url(r"^prizes/$", direct_to_template, {"template": "pytexas/prizes.html"}, name="prizes"),
        url(r"^schedule-survey/$", direct_to_template, {"template": "pytexas/schedule_survey.html"}, name="schedule_survey"),
    ))),
)

# static media override
if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"^favicon.ico$", redirect_to, {
            "url": settings.STATIC_URL + "img/favicon.ico",
        }),
        url(r"^%s/site_media/media/(?P<path>.*)$" % settings.DIR_NAME, "django.views.static.serve", {
            "document_root": settings.MEDIA_ROOT,
        }),
        url(r"", include("staticfiles.urls")),
    )

