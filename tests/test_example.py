# tests/test_example.py
import pytest

from pages.base_page import BasePage


# Define a pytest fixture that returns a BasePage instance
@pytest.fixture
def base_page(setup_driver):
    return BasePage(setup_driver)


# Test case for opening the base page and checking its title
def test_example(base_page):
    base_page.open()  # Open the base page
    assert "Example Domain" in base_page.get_title()  # Assert that the page title is correct
