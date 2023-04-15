import allure
import pytest
from requests import Response
from pytest_voluptuous import S
from urllib import parse

from tests.API.data.holidays import holidays_list
from tests.API.schemas.covid_restrictions import covid_restrictions_schema
from tests.API.schemas.holidays import holidays_schema
from tests.API.schemas.hotel_search import hotel_search_schema
from tests.API.schemas.hotel_search_history import hotel_search_history_schema


@allure.tag('API')
@allure.feature('API')
class TestAPI:
    @allure.feature('Popular Destinations')
    class TestPopularDestinations:
        @pytest.mark.xfail(reason='The response returns an empty list. I need to discuss this with analysts.')
        @allure.story('Popular Destinations')
        def test_popular_destinations(self, ostrovok):
            result: Response = ostrovok.get(url='/api/about/v1/popular_destinations')

            assert result.status_code == 200
            assert not result.json()

    @allure.feature('Covid Restrictions')
    class TestCovidRestrictions:
        @pytest.mark.parametrize('country_code',
                                 ['us',
                                  pytest.param('ru', marks=pytest.mark.xfail(reason='RU results are broken'))])
        @pytest.mark.parametrize('language', ['en', 'ru'])
        @allure.story('Covid Restrictions')
        def test_covid_restrictions(self, ostrovok, country_code, language):
            result: Response = ostrovok.get(url='/api/about/v1/covid_restrictions_from_blog/', params={
                'country_code': country_code,
                'lang': language
            })

            assert result.status_code == 200
            assert result.json() == S(covid_restrictions_schema)

    @allure.feature('Holidays')
    class TestHolidays:
        @pytest.mark.xfail(reason='Result depends on geo')
        @allure.story('Holidays')
        def test_holidays(self, ostrovok):
            result: Response = ostrovok.get(url='/api/v1/holidays')

            assert result.status_code == 200
            assert result.json() == S(holidays_schema)
            assert result.json()['holidays'] == holidays_list

    @allure.feature('History')
    class TestHistory:
        @pytest.mark.xfail(reason='The response returns an empty list. '
                                  'History should not be requested without user data. '
                                  'I need to discuss this with analysts.')
        @allure.story('History')
        def test_hotel_search_history(self, ostrovok):
            result: Response = ostrovok.get(url='/hotel/search/v1/history/')

            assert result.status_code == 200
            assert result.json() == S(hotel_search_history_schema)
            assert not result.json()

    @allure.feature('Multicomplete')
    class TestMulticomplete:
        @pytest.mark.parametrize('query', ['Moscow, Russia', 'Istanbul, Turkiye'])
        @pytest.mark.parametrize('locale', ['en', 'ru'])
        @allure.story('Multicomplete')
        def test_hotel_search(self, ostrovok, query, locale):
            result: Response = ostrovok.get(url='/api/site/multicomplete.json', params={
                'query': parse.quote(query),
                'locale': locale
            })

            assert result.status_code == 200
            assert result.json() == S(hotel_search_schema)
