from playwright.sync_api import Page

class LocationAndLanguagesPrompt:

    def is_page_shown(page: Page):
        """
        Checks if the page is displayed
        Paremeters
        page : Page
            current page
        """ 
        welcome_screen = page.get_by_text("Welcome to Delta")
        if welcome_screen.is_visible():
            return True
        else:
            print("No location page is shown")
            return False

    def select_us(page: Page):
        """
        Selects the US locale and English language
        Paremeters
        page : Page
            current page
        """ 
        page.get_by_role("link", name="Select other Location and Language").click()
        page.get_by_role("link", name="North America").click()
        page.get_by_role("link", name="United States - English").click()
        page.get_by_role("button", name="United States - English").click()