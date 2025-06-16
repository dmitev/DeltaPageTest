from playwright.sync_api import Page
from tools.datepicker import DateSelector

class DeltaMainPage(DateSelector):
    
    def __init__(self, page: Page):
         self.page = page
         self.page.goto("https://www.delta.com/eu/en")

    def changeOrigin(self, origin: dict):
        """
        Changes the origin field
        Paremeters
        origin : dict
            dictionary containing the search param for the origin and the full name
        """
        self.page.get_by_role("link", name="Departure Airport or City").click()
        self.page.get_by_role("textbox", name="Origin City or Airport").fill(origin['insert_text'])
        self.page.get_by_role("link", name=origin['full_text']).click()

    def changeDestination(self, destination: dict):
        """
        Changes the destination field
        Paremeters
        destination : dict
            dictionary containing the search param for the destination and the full name
        """        
        self.page.get_by_role("link", name="To Destination Airport").click()
        self.page.get_by_role("textbox", name="Destination City or Airport").fill(destination['insert_text'])
        self.page.get_by_role("link", name=destination['full_text']).click()

    def setRoundTripDate(self):
        """Set start and end dates for a round trip flight"""
        self.page.get_by_role("button", name=" departureDate returnDate").click()
        today = DateSelector.getTodayDate()
        todayFormat = DateSelector.formatDate(dateToFormat=today)
        oneWeek = DateSelector.getOneWeekFromToday()
        oneWeekFormat = DateSelector.formatDate(dateToFormat=oneWeek)
        self.page.get_by_role("link", name=todayFormat).click()
        self.page.get_by_role("link", name=oneWeekFormat).click()
        self.page.get_by_role("button", name="done").click()

    def changePassengers(self, passCount: int):
        """
        Changes the amount of passengers
        Paremeters
        destination : int
            number of passengers
        """          
        self.page.get_by_label("Passenger").get_by_text("Passenger").click()
        if passCount == 1:
            passengers = str(passCount) + " Passenger"        
        if passCount > 1:
            passengers = str(passCount) + " Passengers"
        else:
            raise Exception("Invalid integer provided for passCount = " + str(passCount))
        self.page.get_by_role("option", name=passengers).click()

    def pressSearchButton(self):
        """Presses the search button"""
        self.page.get_by_role("button", name="SEARCH Flight Search").click()
