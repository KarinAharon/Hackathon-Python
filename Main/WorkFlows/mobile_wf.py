import allure
from Main import Utilities
from Main.Utilities.common_ops import Common_Ops
from Main.Utilities.manage_pages import Manage_Pages
from Main.Extensions.mobile_actions import Mobile_Actions


class Mobile_WF:

    @staticmethod
    @allure.step("calculate 2 numbers")
    def calculate(number1: str, action: str, number2: str):
        Mobile_Actions.click_action(Utilities.manage_pages.financial_page.get_calc_app())
        Mobile_Actions.click_action(Utilities.manage_pages.calc_page.get_whatEver(number1))
        Mobile_Actions.click_action(Utilities.manage_pages.calc_page.get_whatEver(action))
        Mobile_Actions.click_action(Utilities.manage_pages.calc_page.get_whatEver(number2))

        @staticmethod
        @allure.step("get calculate result")
        def get_result_text():
            return Mobile_Actions.get_text(Utilities.manage_pages.calc_page.get_result())

    @staticmethod
    @allure.step("search functionality")
    def search(search):
        Mobile_Actions.click_action(Utilities.manage_pages.financial_page.get_search_btn())
        Mobile_Actions.insert_value(search, Utilities.manage_pages.financial_page.get_search_input())
        Mobile_Actions.click_action(Utilities.manage_pages.financial_page.go_search())

    @staticmethod
    @allure.step("get result")
    def click_on_waanted_result(reslut_text):
        Mobile_Actions.click_action(Utilities.manage_pages.search_results_po.search_result(reslut_text))

    @staticmethod
    @allure.step("get application's title")
    def get_app_title(app_title):
        return Mobile_Actions.get_text(Utilities.manage_pages.search_results_po.search_result(app_title))

    @staticmethod
    @allure.step("navigate to home page")
    def navigate_to_home_page():
        Mobile_Actions.click_action(Utilities.manage_pages.tmv_page.go_back_btn())
        Mobile_Actions.click_action(Utilities.manage_pages.search_results_po.go_back_btn())

    @staticmethod
    @allure.step("check search functionality")
    def search_flow():
        Mobile_WF.search(Common_Ops.get_data("searchApp"))
        Mobile_WF.click_on_waanted_result(Common_Ops.get_data("xpathMobileText"))
        actual_result = Mobile_WF.get_app_title(Common_Ops.get_data("xpathMobileText"))
        Mobile_WF.navigate_to_home_page()
        return actual_result
