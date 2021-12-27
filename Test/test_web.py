import pytest

from Main.WorkFlows.web_wf import Web_WF

@pytest.mark.usefixtures('init_web')
class Test_web:

    def test_01(self):
        Web_WF.register("Yoni", "Choen", "Yoni", "123456")

    def test_02(self):
        Web_WF.login("Yoni", "123456")
        Web_WF.new_bank_account("Leumi", "123456789", "123123123")
        assert Web_WF.current_connected_user() == "@Yoni"
