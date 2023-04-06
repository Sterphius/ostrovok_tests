from utils.base_session import BaseSession
import os
import pytest
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session', autouse=True)
def ostrovok():
    ostrovok_api_url = os.getenv('OSTROVOK_API_URL')
    return BaseSession(ostrovok_api_url)
