import pytest
from Pages.LoginPage import LoginPage
from playwright.sync_api import Page, expect




#@pytest.mark.skip
def test_validLogin(page: Page):
    user = "standard_user"
    pswd = "secret_sauce"
    
    lp = LoginPage(page)
    lp.login(user,pswd)
    
    expect(lp.page).to_have_url("https://www.saucedemo.com/inventory.html")
    
#@pytest.mark.skip
def test_inValidLogin(page: Page):
    user = "locked_out_user"
    pswd = "secret_sauce"
    lp = LoginPage(page)
    
    lp.login(user, pswd)
    
    expect(page.locator(".error-message-container")).to_have_text("Epic sadface: Sorry, this user has been locked out.")
    
#@pytest.mark.skip  
def test_problemuser(page:Page):
    user="problem_user"
    pswd = "secret_sauce"
    
    lp = LoginPage(page)
    
    lp.login(user,pswd)
    
    imgs = page.query_selector_all("div.inventory_item div a img")
    
    for i in imgs:
        atrb = i.get_attribute("src")
        assert "/static/media/sl-404.168b1cce.jpg" in atrb

    