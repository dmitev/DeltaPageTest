import yaml
import pytest
from prompts.gdpr_prompt import GdprPrompt
from pages.delta_main_page import DeltaMainPage
from prompts.location_and_languages_prompt import LocationAndLanguagesPrompt
from pages.flight_search_page import FlightSearchPage
from tools.datepicker import DateSelector
from playwright.sync_api import Page


@pytest.fixture(autouse=True)
def delta_main_page(page: Page):
    # Initialize delta.com web page
    delta_main_page = DeltaMainPage(page)
    # Close GDPR prompt screen
    GdprPrompt.close_gdpr_screen(page)
    # Select US location and English language if prompted
    if LocationAndLanguagesPrompt.is_page_shown(page) : LocationAndLanguagesPrompt.select_us(page)
    return delta_main_page

@pytest.fixture(autouse=True)
def locations():
    with open('yaml/location.yml', 'r') as file:
        locations = yaml.safe_load(file)
    return locations

def test_book_a_roundtrip_from_atl_to_hnl_for_2_passengers(page: Page, delta_main_page, locations) -> None:
    passenger_count = 2
    # Set the origin and destination of the booking
    delta_main_page.changeOrigin(locations['ATL'])
    delta_main_page.changeDestination(locations['HNL'])
    # Set the round trip to starting date today and return 1 week later
    delta_main_page.setRoundTripDate()
    # Set the passenger count
    delta_main_page.changePassengers(passenger_count)
    # Press the search button
    delta_main_page.pressSearchButton()
    # Perform verification on all fields that were set
    flight_page = FlightSearchPage(page)
    flight_page.verify_flight_locations(locations['ATL']['insert_text'], locations['HNL']['insert_text'])
    flight_page.verify_flight_type()
    flight_page.verify_flight_date(DateSelector.format_short_date(DateSelector.get_today_date()))
    flight_page.verify_passengers(2)

def test_book_a_multi_city_flight_from_hnl_to_atl_to_ams(page: Page, delta_main_page, locations) -> None:
    # Change the flight type
    delta_main_page.changeFlightType("multi-city")
    # Change the flight origin
    delta_main_page.changeOrigin(locations['HNL'], True)
    # Change the flight destinations
    delta_main_page.changeDestination(locations['ATL'], True, 1)
    delta_main_page.changeDestination(locations['AMS'], True, 2)
    # Set the flight dates
    tomorrow = DateSelector.get_tomorrow_date()
    delta_main_page.setMultiCityDate(DateSelector.format_date(tomorrow), 1)
    delta_main_page.setMultiCityDate(DateSelector.format_date(DateSelector.get_one_week_from_today()), 2)
    # Press the search button
    delta_main_page.pressSearchButton()
    flight_page = FlightSearchPage(page)
    # Perform verification on all fields that were set
    flight_page.verify_flight_locations(locations['HNL']['insert_text'], locations['ATL']['insert_text'])
    flight_page.verify_flight_date(DateSelector.format_short_date(tomorrow))

def test_search_without_entering_parameters(page: Page, delta_main_page) -> None:
    # Press the search button
    delta_main_page.pressSearchButton()
    # Perform verification on all fields that are mandatory
    delta_main_page.verifyMissingDestination()
    delta_main_page.verifyMissingDates()
