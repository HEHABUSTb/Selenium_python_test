import pytest

from Pages.Test_Logger import Logger
from Pages.base_page import BasePage
import time

link = 'http://selenium1py.pythonanywhere.com/'
logger = Logger().getLogger()


@pytest.mark.usefixtures('browser')
class TestClass:
    def test_multi_browser(self):
        page = BasePage(self.browser, link)
        time.sleep(2)
        logger.info('It should make logfile')
        page.open()
        assert 1 == 2, 'Allure automate screenshot test'
