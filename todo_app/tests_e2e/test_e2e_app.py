#import selenium
from selenium import webdriver # type: ignore
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv, find_dotenv
import pytest

file_path = find_dotenv('tests/.env.test')
load_dotenv(file_path, override=True)

@pytest.fixture(scope='module')
def driver():
    opts = Options()
    opts.headless = True
    with webdriver.Firefox(options=opts) as driver:
        yield driver
