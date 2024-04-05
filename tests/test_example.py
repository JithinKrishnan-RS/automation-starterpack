# tests/test_example.py
import pytest

from locators import base_page_locators
from pages.base_page import BasePage


@pytest.fixture
def base_page(setup_driver):
    return BasePage(setup_driver)


def test_example(base_page):
    base_page.open()
    assert "Example Domain" in base_page.get_title()
