import pytest
from Main.WorkFlows.mobile_wf import Mobile_WF

@pytest.mark.usefixtures('init_mobile')
class Test_Mobile:

    def test_1(self):
        Mobile_WF.search("TVM Calculator")
        Mobile_WF.click_on_waanted_result("'TVM Calculator'")
        actual_result = Mobile_WF.get_app_title("'TVM Calculator'")
        Mobile_WF.navigate_to_home_page()
        assert actual_result == "TVM Calculator"

    def test_2(self):
        Mobile_WF.calculate("'6'", "'×'", "'5'")
        assert Mobile_WF.get_result_text() == "30"
