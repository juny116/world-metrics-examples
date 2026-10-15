# World Metrics Web Examples

Worldometer의 렌더링된 카운터를 수집해 JSON으로 제공하는 Django·Flask 예제입니다. 두 웹 어댑터가 같은 HTML 파서와 수집기를 사용합니다.

## 코드 구조

| 경로 | 역할 |
|---|---|
| `world_metrics/collector.py` | HTML 숫자 파싱, Selenium 실행과 종료 |
| `world_metrics/flask_app.py` | Flask 앱 팩터리와 /all |
| `world_metrics/django_views.py` | Django JSON 응답 |
| `world_metrics/django_urls.py` | Django URL 연결 |

## 실행

```bash
pip install -e ".[runtime]"
python -m world_metrics.flask_app
```

Django는 본인의 프로젝트 ROOT_URLCONF에 world_metrics.django_urls를 연결합니다. Chrome이 필요하며 요청마다 브라우저를 열고 finally에서 종료합니다. 수집기 인자를 주입해 브라우저 없이 어댑터를 테스트할 수 있습니다.

## Source and license

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for project origins and third-party licenses.
