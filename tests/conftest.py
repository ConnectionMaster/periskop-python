import pytest

from periskop.collector import ExceptionCollector
from periskop.types import HTTPContext


@pytest.fixture
def collector():
    return ExceptionCollector()


@pytest.fixture
def sample_http_context():
    return HTTPContext(request_method="GET", request_url="http://example.com",
                       request_headers={"Cache-Control": "no-cache"})