from playwright.sync_api import Page, expect
class HomePage:
    def __init__(self, page:Page):
        self.page = page
        self.upgrade_button = page.get_by_role('button', name="upgrade")
        self.performance_link = page.get_by_role('link', name="Performance")
        self.dashboard_link = page.get_by_role('link', name="Dashboard")

        def is_upgrade_button_visible():
            expect(self.upgrade_button).is_visible()

        def is_performance_visible():
            expect(self.performance_link).click()

        def is_dashboard_link_visible():
            self.performance_link.click()
