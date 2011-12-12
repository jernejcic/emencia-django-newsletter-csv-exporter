from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required, permission_required
from emencia_newsletter_exporter.views import EmenciaMailingListExporterView

urlpatterns = patterns('',
    url(r'mailinglist/(?P<mailing_list_id>\d+)/export/csv/$',
        EmenciaMailingListExporterView.as_csv,
        {},
        name='newsletter_mailinglist_subscribers_exporter_csv'),
)
