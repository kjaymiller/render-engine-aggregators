import pytest
from render_engine.collection import Collection
from render_engine.page import Page
from src.render_engine_aggregators.feed import AggregateFeed


@pytest.fixture()
def aggregated_feed():

    class page1(Page):
        content = "page1"


    class page2(Page):
        content = "page2"


    class Collection1(Collection):
        pages = [page1()]


    class Collection2(Collection):
        pages = [page2()]


    class AggregateFeed1(AggregateFeed):
        collections = [Collection1, Collection2]


    return AggregateFeed1()
