from playwright.sync_api import Page

class LoginPage:
    
    userName = "Username"
    password = "Password"
    LoginBtn = "#login-button"
    errormsg = ".error-message-container"
    
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("https://www.saucedemo.com/")
        #self.userName = self.page.get_by_placeholder("Username")
        
        #self.password = self.page.get_by_placeholder("Password")
        
        #self.LoginBtn = self.page.locator("#login-button")
        
        #self.errormsg = self.page.locator(".error-message-container")
        
        
    
    
    def login(self, username, password):
        #self.userName.fill(username)
        #self.password.fill(password)
        #self.LoginBtn.click()
        
        self.page.get_by_placeholder(self.userName).type(username)
        
        self.page.get_by_placeholder(self.password).type(password)
        
        self.page.locator(self.LoginBtn).click()