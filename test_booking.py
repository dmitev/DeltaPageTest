import yaml
from prompts.gdpr_prompt import GdprPrompt
from pages.delta_main_page import DeltaMainPage
from prompts.location_and_languages_prompt import LocationAndLanguagesPrompt
from pages.flight_search_page import FlightSearchPage
from tools.datepicker import DateSelector
from playwright.sync_api import Page, expect


def test_book_a_roundtrip_from_atl_to_hnl_for_2_passengers(page: Page) -> None:
    passengerCount = 2
    # Initialize delta.com web page
    delta_main_page = DeltaMainPage(page)
    # Close GDPR prompt screen
    GdprPrompt.closeGdprScreen(page)
    # Select US location and English language if prompted
    if LocationAndLanguagesPrompt.isPageShown(page) : LocationAndLanguagesPrompt.selectUS(page)
    # Set the origin and destination of the booking
    with open('yaml/location.yml', 'r') as file:
        locations = yaml.safe_load(file)
    delta_main_page.changeOrigin(locations['ATL'])
    delta_main_page.changeDestination(locations['HNL'])
    # Set the round trip to starting date today and return 1 week later
    delta_main_page.setRoundTripDate()
    # Set the passenger count
    delta_main_page.changePassengers(passengerCount)
    # Press the search button
    delta_main_page.pressSearchButton()
    # Perform verification on all fields that were set
    flight_page = FlightSearchPage(page)
    flight_page.verifyFlightLocations(locations['ATL']['insert_text'], locations['HNL']['insert_text'])
    flight_page.verifyFlightType()
    flight_page.verifyFlightDate(DateSelector.formatShortDate(DateSelector.getTodayDate()))
    flight_page.verifyPassengers(2)
