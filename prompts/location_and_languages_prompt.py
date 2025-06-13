from playwright.sync_api import Page

class LocationAndLanguagesPrompt:
    
    def __init__(self, page: Page):
        pass

    def isPageShown(page: Page):
        welcome_screen = page.get_by_text("Welcome to Delta")
        if welcome_screen.is_visible:
            return True
        else:
            print("No location page is shown")
            return False

    def selectUS(page: Page):
        page.get_by_role("link", name="Select other Location and Language").click()
        page.get_by_role("link", name="North America").click()
        page.get_by_role("link", name="United States - English").click()
        page.get_by_role("button", name="United States - English").click()