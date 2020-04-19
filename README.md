# periskop-python

[![Build Status](https://api.cirrus-ci.com/github/soundcloud/periskop-python.svg)](https://cirrus-ci.com/github/soundcloud/periskop-go)

[Periskop](https://github.com/soundcloud/periskop) requires collecting and aggregating exceptions on the client side,
as well as exposing them via an HTTP endpoint using a well defined format.

This library provides low level collection and rendering capabilities

## Install

```
pip install periskop
```

## Usage example

```python
import json
from http.server import HTTPServer

from periskop.collector import ExceptionCollector
from periskop.exporter import ExceptionExporter
from periskop.handler import exception_http_handler
from periskop.models import HTTPContext


def faulty_json():
    return json.loads('{"id":')


if __name__ == "__main__":
    collector = ExceptionCollector()
    try:
        faulty_json()
    except Exception as exception:
        # Report without context
        collector.report(exception)
        # Report with HTTP context
        collector.report_with_context(exception,
                                      HTTPContext("GET", "http://example.com", {"Cache-Control": "no-cache"}))

    # Expose collected exceptions in localhost:8081/-/exceptions
    server_address = ('', 8081)
    handler = exception_http_handler(path="/-/exceptions", exporter=ExceptionExporter(collector))
    http_server = HTTPServer(server_address, handler)
    http_server.serve_forever()

```

## Run tests

For running tests [pytest](https://docs.pytest.org) is needed. A recommended way to run all check is installing [tox](https://tox.readthedocs.io/en/latest/install.html) and then just type `tox`. This will run `pytest` tests, [flake8](https://flake8.pycqa.org) and [mypy](http://mypy-lang.org/) static analyzers.

Alternatively you can run `pip install -r requirements-tests.txt` and then run `pytest`.