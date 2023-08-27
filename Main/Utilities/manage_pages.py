from Main.PageObject.desktop.calc_page import CalcPage
from Main.PageObject.electron.electron_page import Electron_Page
from Main.PageObject.mobile.calc_page import Calc_Page
from Main.PageObject.mobile.financial_page import Financial_Page
from Main.PageObject.mobile.search_results_po import Search_Page
from Main.PageObject.mobile.tmv_page import TMV_Page
from Main.PageObject.web.bank_details_page import Bank_Details_Page
from Main.PageObject.web.login_page import LoginPage
from Main.PageObject.web.main_page import MainPage
from Main.PageObject.web.new_bank_account_page import Bank_Account_Page
from Main.PageObject.web.notifications_page import Notification_Page
from Main.PageObject.web.register_page import RegisterPage


class Manage_Pages:

    @staticmethod
    def init_web_pages(driver):
        globals()['login_page'] = LoginPage(driver)
        globals()['register_page'] = RegisterPage(driver)
        globals()['bank_account_page'] = Bank_Account_Page(driver)
        globals()['main_page'] = MainPage(driver)
        globals()['notification_page'] = Notification_Page(driver)
        globals()['bank_details_page'] = Bank_Details_Page(driver)

    @staticmethod
    def init_desktop_page(driver):
        globals()['calc_page'] = CalcPage(driver)

    @staticmethod
    def init_electron_page(driver):
        globals()['electron_page'] = Electron_Page(driver)

    @staticmethod
    def init_mobile_pages(driver):
        globals()['calc_page'] = Calc_Page(driver)
        globals()['financial_page'] = Financial_Page(driver)
        globals()['search_results_po'] = Search_Page(driver)
        globals()['tmv_page'] = TMV_Page(driver)