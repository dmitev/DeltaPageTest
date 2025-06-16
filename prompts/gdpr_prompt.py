from playwright.sync_api import Page

class GdprPrompt:

    def close_gdpr_screen(page: Page):
        """
       Closes the GDPR screen
        Paremeters
        page : Page
            current page
        """ 
        page.get_by_role("button", name="Close", exact=True).click()