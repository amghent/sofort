from django.template import defaultfilters
from django.urls import reverse
from django.utils.translation import gettext, ngettext
from jinja2 import Environment
from django.templatetags.static import static
import pytz
from django.conf import settings


def environment(**options):
    env = Environment(extensions=['jinja2.ext.i18n'], **options)

    env.filters.update({
        'dt_to_user_frmt': datetime_to_user_frmt,
    })

    env.install_gettext_callables(gettext=gettext, ngettext=ngettext, newstyle=True)

    env.globals.update({
        'static': static,
        'url': reverse,
        'dj': defaultfilters
    })

    return env


def datetime_to_user_frmt(value):
    tz = pytz.timezone(settings.TIME_ZONE)
    local_dt = value.astimezone(tz)

    return local_dt.strftime(settings.DATE_TIME_FORMAT)
