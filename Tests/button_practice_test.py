import pytest
from Pages.base_page import BasePage
import time

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.mark.usefixtures('browser')
class TestClass:
    def test_multi_browser(self):
        page = BasePage(self.browser, link)
        time.sleep(2)
        page.open()
