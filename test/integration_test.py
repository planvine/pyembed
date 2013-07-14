from rembed import *

from hamcrest import *
import pytest

@pytest.mark.xfail
def test_should_get_correct_embedding():
    consumer = REmbedConsumer()
    embedding = consumer.embed('https://twitter.com/BarackObama/status/266031293945503744')
    assert_that(embedding, contains_string('Four more years.'))