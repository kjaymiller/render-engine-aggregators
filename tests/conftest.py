import pytest
from render_engine.collection import Collection
from render_engine.blog import Blog
from render_engine.page import Page
from src.render_engine_aggregators.feed import AggregateFeed


@pytest.fixture()
def aggregated_feed(tmp_path):

    path = tmp_path / "content"
    path.mkdir()
    post = path / "page2.md"
    content = """---
title: page2
---

page2"""
    post.write_text(content)

    class page1(Page):
        content = "page1"


    class Collection1(Collection):
        pages = [page1()]


    class Collection2(Blog):
        content_path = str(path)


    class AggregateFeed1(AggregateFeed):
        collections = [Collection1, Collection2]


    return AggregateFeed1
