import pytest
from render_engine.engine import engine
from render_engine.site import Site


@pytest.mark.parametrize("page", ["page1", "page2"])
def test_pages_in_aggregated_feed(aggregated_feed, page):
    template = engine.get_template(aggregated_feed().template)
    assert page in aggregated_feed()._render_from_template(template=template)

def test_page_loads_in_site(aggregated_feed):
    site = Site()
    site.page(aggregated_feed)
    assert aggregated_feed()._slug in site._route_list