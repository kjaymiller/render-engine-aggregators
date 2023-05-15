import itertools

from render_engine.feeds import RSSFeed
from render_engine.page import Page


class AggregateFeed(RSSFeed, Page):
    collections: list

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if not self.collections:
            raise ValueError("No collections provided") 

        self.pages = itertools.chain.from_iterable(
            map(lambda x:x().__iter__(), self.collections)
        )