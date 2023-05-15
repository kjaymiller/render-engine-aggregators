import pytest
from render_engine.engine import engine



@pytest.mark.parametrize("page", ["page1", "page2"])
def test_pages_in_aggregated_feed(aggregated_feed, page):
    template = engine.get_template(aggregated_feed.template)
    assert page in aggregated_feed._render_from_template(template=template)