import json
from world_metrics.collector import parse_counters
from world_metrics.flask_app import create_app


def test_parser_handles_missing_and_split_counters():
    html = '<div class="counter-group"><div class="counter-heading"><span class="counter-item">Births today</span><span class="counter-number"><span class="rts-counter">1,</span><span class="rts-counter">234</span></span></div></div><div class="counter-group"></div>'
    assert parse_counters(html) == {"births_today": 1234}

def test_flask_reuses_injected_collector_without_browser():
    response = create_app(lambda: {"births_today": 42}).test_client().get("/all")
    assert response.status_code == 200 and response.json == {"births_today": 42}

def test_django_adapter_reuses_same_collector(monkeypatch):
    from django.conf import settings
    if not settings.configured: settings.configure(DEFAULT_CHARSET="utf-8")
    import world_metrics.django_views as views
    monkeypatch.setattr(views, "collect_counters", lambda: {"births_today": 42})
    assert json.loads(views.counters(None).content) == {"births_today": 42}
