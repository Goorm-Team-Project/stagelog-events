from django.contrib import admin
from django.urls import include, path

from events import views as events_views
from common.utils import health_check

urlpatterns = [
    path('admin/', admin.site.urls),

    # public
    path('api/events', events_views.event_list, name='event_list'),
    path('api/events/', include('events.urls')),

    # internal
    path('internal/events/<int:event_id>/exists', events_views.internal_event_exists, name='internal_event_exists'),
    path('internal/events/<int:event_id>/summary', events_views.internal_event_summary, name='internal_event_summary'),
    path('internal/events:batch-summary', events_views.internal_events_batch_summary, name='internal_events_batch_summary'),

    path('', health_check),
]
