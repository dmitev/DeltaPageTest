from playwright.sync_api import Page, expect
from tools.datepicker import DateSelector

class DeltaMainPage():
    
    def __init__(self, page: Page):
         self.page = page
         self.page.goto("https://www.delta.com/eu/en")

    def changeFlightType(self, type: str):
        """
        Changes the flight type
        Paremeters
        type : str
            a string with the type of flight to be selected
        """
        self.page.get_by_role("combobox", name="Trip Type:, changes will").locator("span").first.click()
        if type.lower() == "multi-city":
            self.page.get_by_role("option", name="Multi-City").click()
        else:
            raise ValueError("Incorrect flight type provided: " + type)

    def changeOrigin(self, origin: dict, isMultiCity = False):
        """
        Changes the origin field
        Paremeters
        origin : dict
            dictionary containing the search param for the origin and the full name
        isMultiCity: bool
            set to True when setting up an origin for a multi-city search, otherwise False
        """
        if isMultiCity:
            self.page.get_by_role("link", name="Flight 1 OTP Deprature").click()
        else:
            self.page.get_by_role("link", name="Departure Airport or City").click()
        self.page.get_by_role("textbox", name="Origin City or Airport").fill(origin['insert_text'])
        self.page.get_by_role("link", name=origin['full_text']).click()

    def changeDestination(self, destination: dict, isMultyCity = False, cityNumber = 0):
        """
        Changes the destination field
        Paremeters
        destination : dict
            dictionary containing the search param for the destination and the full name
        isMultiCity: bool
            set to True when setting up an origin for a multi-city search, otherwise False
        cityNumber: int
            the number of the multi-city flight that will be updated
        """        
        if isMultyCity:
            if cityNumber == 0:
                raise ValueError("No cityNumber value provided")
            self.page.get_by_role("link", name="Flight " + str(cityNumber) + " To Arrival Airport").click()
        else:
            self.page.get_by_role("link", name="To Destination Airport").click()
        self.page.get_by_role("textbox", name="Destination City or Airport").fill(destination['insert_text'])
        self.page.get_by_role("link", name=destination['full_text']).click()

    def setRoundTripDate(self):
        """Set start and end dates for a round trip flight"""
        self.page.get_by_role("button", name=" departureDate returnDate").click()
        today = DateSelector.get_today_date()
        today_format = DateSelector.format_date(today)
        one_week = DateSelector.get_one_week_from_today()
        one_week_format = DateSelector.format_date(one_week)
        self.page.get_by_role("link", name=today_format).click()
        self.page.get_by_role("link", name=one_week_format).click()
        self.page.get_by_role("button", name="done").click()

    def setMultiCityDate(self, date: str, flightNumber: int):
        """
        Sets the departure date for a multi city flight
        Paremeters
        date : str
            formatted date string
        flightNumber : int
            the number of the flight to be set
        """          
        self.page.locator("#input_departureDate_" + str(flightNumber)).click()
        self.page.get_by_role("link", name=date).click()
        self.page.get_by_role("button", name="done").click()

    def changePassengers(self, pass_count: int):
        """
        Changes the amount of passengers
        Paremeters
        destination : int
            number of passengers
        """          
        self.page.get_by_label("Passenger").get_by_text("Passenger").click()
        if pass_count == 1:
            passengers = str(pass_count) + " Passenger"
        if pass_count > 1:
            passengers = str(pass_count) + " Passengers"
        else:
            raise ValueError("Invalid integer provided for pass_count = " + str(pass_count))
        self.page.get_by_role("option", name=passengers).click()

    def pressSearchButton(self):
        """Presses the search button"""
        self.page.get_by_role("button", name="SEARCH Flight Search").click()

    def verifyMissingDestination(self):
        """Verifies the message that the flight destination field is empty"""
        expect(self.page.get_by_text("Please enter a Destination")).to_be_visible()

    def verifyMissingDates(self):
        """Verifies the message that the flight dates fields are empty"""
        expect(self.page.get_by_text("Departure and return dates")).to_be_visible()
