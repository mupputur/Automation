import pytest
from Applications.Redbus.side_panel.side_panel_page import SidePanelPage

class TestCases:

    @pytest.fixture()
    def Sidepage(self):
        return SidePanelPage()

    def test_naviage_login(self,Sidepage):
        # Sidepage = SidePanelPage()
        Sidepage.naviage_login()
        data = Sidepage.login_page()
        assert 'Sign in to avail exciting discounts and cashbacks!!!' == data

    def test_naviagte_offers(self,Sidepage):
        # Sidepage = SidePanelPage()
        Sidepage.naviagte_offers()
        data = Sidepage.offers_page()
        assert 'Offers' == data

    def test_navigate_refer_and_earn(self,Sidepage):
        # Sidepage = SidePanelPage()
        Sidepage.navigate_refer_and_earn()
        data = Sidepage.refer_and_earn_page()
        assert 'Sign in to refer friends and earn exciting cashbacks!!' == data

    def test_navigate_help(self,Sidepage):
        # Sidepage = SidePanelPage()
        Sidepage.navigate_help()
        data = Sidepage.help_page()
        assert 'Create account or Sign in' == data

    def test_navigate_get_ticket_details(self,Sidepage):
        # Sidepage = SidePanelPage()
        Sidepage.navigate_get_ticket_details()
        data = Sidepage.get_ticket_page()
        assert 'View M-Ticket' == data

    def test_navigate_about_us(self,Sidepage):
        # Sidepage = SidePanelPage()
        Sidepage.navigate_about_us()
        data = Sidepage.about_us_page()
        assert 'About Us' == data

    def test_navigate_cancel_ticket(self,Sidepage):
        # Sidepage = SidePanelPage()
        Sidepage.navigate_cancel_ticket()
        data = Sidepage.cancel_ticket_page()
        assert 'Cancellation' == data

    def test_naviagte_settings(self,Sidepage):
        # Sidepage = SidePanelPage()
        Sidepage.naviagte_settings()
        data = Sidepage.setting_page()
        assert 'Settings' == data

    def test_naviagte_search_buses(self,Sidepage):
        # Sidepage = SidePanelPage()
        Sidepage.naviagte_search_buses()
        data = Sidepage.search_buses_page()
        assert 'SEARCH BUSES' == data

    def test_navigate_reschedule_ticket(self,Sidepage):
        # Sidepage = SidePanelPage()
        Sidepage.navigate_reschedule_ticket()
        data = Sidepage.reschedule_ticket_page()
        assert 'Reschedule' == data
