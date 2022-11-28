from django.urls import path
from speakers.views import show_speakers, show_speakers_info, SearchResultsView, show_json

app_name = 'speakers'

urlpatterns = [
    path('', show_speakers, name='show_speakers'),
    path('show_speakers_info/<int:id>/', show_speakers_info, name='show_speakers_info'),
    path('search/', SearchResultsView.as_view(), name="search_speakers"),
    path('json/', show_json, name='show_json'),
]