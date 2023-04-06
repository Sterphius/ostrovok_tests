import json
import os
import allure
import pytest
from requests import Response
from pytest_voluptuous import S

from allure_commons.types import Severity
from tests.API.schemas.covid_restrictions import covid_restrictions_schema
from tests.API.schemas.holidays import holidays_schema
from tests.API.schemas.hotel_search import hotel_search_schema
from tests.API.schemas.hotel_search_history import hotel_search_history_schema


@allure.tag('API')
@allure.label('owner', 'Sterphius')
@allure.feature('API')
@allure.story('popular_destinations')
@allure.severity(Severity.NORMAL)
@pytest.mark.xfail(reason='The response returns an empty list. I need to discuss this with analysts.')
def test_popular_destinations(ostrovok):
    result: Response = ostrovok.get(url='/api/about/v1/popular_destinations')

    assert result.status_code == 200
    assert len(result.json()) != 0


@allure.tag('API')
@allure.label('owner', 'Sterphius')
@allure.feature('API')
@allure.story('covid_restrictions_from_blog')
@allure.severity(Severity.CRITICAL)
@pytest.mark.parametrize('country_code',
                         ['us',
                          pytest.param('ru', marks=pytest.mark.xfail(reason='RU results are broken'))])
@pytest.mark.parametrize('language', ['en', 'ru'])
def test_covid_restrictions(ostrovok, country_code, language):
    result: Response = ostrovok.get(url='/api/about/v1/covid_restrictions_from_blog/', params={
        'country_code': country_code,
        'lang': language
    })

    assert result.status_code == 200
    assert result.json() == S(covid_restrictions_schema)


@allure.tag('API')
@allure.label('owner', 'Sterphius')
@allure.feature('API')
@allure.story('holidays')
@allure.severity(Severity.NORMAL)
@pytest.mark.xfail(reason='Result depends on geo')
def test_holidays(ostrovok):
    result: Response = ostrovok.get(url='/api/v1/holidays')

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files/holidays_list.json'), 'r') as f:
        data = json.load(f)

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files/current_holidays.json'), 'w') as f:
        f.write(result.json()['holidays'])

    assert result.status_code == 200
    assert result.json() == S(holidays_schema)
    assert result.json()['holidays'] == data


@allure.tag('API')
@allure.label('owner', 'Sterphius')
@allure.feature('API')
@allure.story('history')
@allure.severity(Severity.NORMAL)
@pytest.mark.xfail(reason='The response returns an empty list. '
                          'History should not be requested without user data. '
                          'I need to discuss this with analysts.')
def test_hotel_search_history(ostrovok):
    result: Response = ostrovok.get(url='/hotel/search/v1/history/')

    assert result.status_code == 200
    assert result.json() == S(hotel_search_history_schema)
    assert len(result.json()) != 0


@allure.tag('API')
@allure.label('owner', 'Sterphius')
@allure.feature('API')
@allure.story('multicomplete')
@allure.severity(Severity.NORMAL)
@pytest.mark.parametrize('query', ['Moscow%2C%20Russia', 'Istanbul%2C%20Turkiye'])
@pytest.mark.parametrize('locale', ['en', 'ru'])
def test_hotel_search(ostrovok, query, locale):
    result: Response = ostrovok.get(url='/api/site/multicomplete.json', params={
        'query': query,
        'locale': locale
    })

    assert result.status_code == 200
    assert result.json() == S(hotel_search_schema)
