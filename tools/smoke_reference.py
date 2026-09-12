"""Exercise the reference API on a disposable running instance with synthetic data."""
import json
import sys
import time
import urllib.error
import urllib.request

base = sys.argv[1] if len(sys.argv) > 1 else 'http://127.0.0.1:8080'
if not base.startswith(('http://127.0.0.1:', 'http://localhost:')):
    raise SystemExit('This smoke exercise only targets local disposable servers.')


def request(path, payload=None):
    data = None if payload is None else json.dumps(payload).encode()
    req = urllib.request.Request(base + path, data=data, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=3) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as error:
        return error.code, json.load(error)


for attempt in range(30):
    try:
        if request('/api/health')[0] == 200:
            break
    except (OSError, ValueError):
        pass
    time.sleep(1)
else:
    raise SystemExit('Reference server did not become ready.')

status, categories = request('/api/categories')
assert status == 200 and categories
body = {'name': 'Smoke-' + str(time.time_ns()), 'category_id': categories[0]['id']}
status, item = request('/api/items', body)
assert status == 201
assert request('/api/items/' + str(item['id']))[1]['name'] == body['name']
assert request('/api/items', body)[0] == 409
assert request('/api/items', {'name': ' ', 'category_id': categories[0]['id']})[0] == 422
assert request('/api/items', {**body, 'name': 'Unknown', 'category_id': 999999})[0] == 422
print('Create/read, duplicate conflict, blank input, and foreign-key boundary checks passed.')
