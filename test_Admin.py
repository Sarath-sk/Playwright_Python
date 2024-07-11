import unittest

import pytest
from Pages.LoginPage import LoginPage
from playwright.sync_api import Page, expect


class TestAdmin(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page
        self.lp = LoginPage(page)
        
        
    def test_validLogin(self):
        user = "standard_user"
        pswd = "secret_sauc"
    
        #lp = LoginPage(page)
        self.lp.login(user,pswd)
    
        expect(self.lp.page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    #@pytest.mark.skip
    def test_inValidLogin(self):
        user = "locked_out_user"
        pswd = "secret_sauce"
        #lp = LoginPage(page)
    
        self.lp.login(user, pswd)
    
        expect(self.page.locator(self.lp.errormsg)).to_have_text("Epic sadface: Sorry, this user has been locked out.")
    
    #@pytest.mark.skip  
    def test_problemuser(self):
        user="problem_user"
        pswd = "secret_sauce"
    
        #lp = LoginPage(page)
    
        self.lp.login(user,pswd)
    
        imgs = self.page.query_selector_all("div.inventory_item div a img")
    
        for i in imgs:
            atrb = i.get_attribute("src")
            assert "/static/media/sl-404.168b1cce.jpg" in atrb

        