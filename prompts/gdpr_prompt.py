from playwright.sync_api import Page

class GdprPrompt:
    
    def __init__(self):
        pass

    def closeGdprScreen(page: Page):
        page.get_by_role("button", name="Close", exact=True).click()