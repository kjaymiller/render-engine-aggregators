import itertools
import more_itertools
import typing 

from render_engine.feeds import RSSFeed

class AggregateFeed(RSSFeed):
    collections: list

    def __init__(self):
        super().__init__()

        if not self.collections:
            raise ValueError("No collections provided") 

        self.pages = itertools.chain.from_iterable(
            map(lambda x:x.pages, self.collections)
        )