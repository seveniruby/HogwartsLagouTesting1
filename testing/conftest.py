import pprint

import pytest
from _pytest.main import Session


def pytest_collection_modifyitems(session: Session, config, items: list):
    # called after collection is completed
    # you can modify the ``items`` list
    items.reverse()
    session.items = items
