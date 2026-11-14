import importlib
import sys

import pytest


@pytest.fixture
def pyexiv2():
    # The dev extra cannot install pyexiv2 on 3.15+ (no wheel yet), so only
    # there is a missing module a skip instead of a failure.
    if sys.version_info >= (3, 15):
        return pytest.importorskip("pyexiv2")
    return importlib.import_module("pyexiv2")
