from playwright.sync_api import expect, Page
import re

class FlightSearchPage:
    
    def __init__(self, page: Page):
        self.page = page

    def verify_flight_locations(self, origin: str, destination: str):
        """
        Verification method for flight locations
        Paremeters
        origin : str
            flight origin name
        destination : str
            flight destination name
        """
        expect(self.page.get_by_text(origin + destination)).to_be_visible()

    def verify_flight_type(self):
        """Verification method for flight type (one way, round trip or multi-city)"""
        expect(self.page.locator("div").filter(has_text=re.compile(r"^Round Trip$"))).to_be_visible()

    def verify_flight_date(self, date: str):
        """
        Verification method for flight date
        Paremeters
        date : str
            formatted date string
        """
        expect(self.page.locator("#main_nav div").filter(has_text=date)).to_be_visible()

    def verify_passengers(self, pass_count: int):
        """
        Verification method for flight passenger count
        Paremeters
        passCount : int
            number of passengers
        """
        expect(self.page.locator("div").filter(has_text=re.compile(rf"^{pass_count} Passengers$"))).to_be_visible()