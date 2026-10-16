from app_resta.resta_logic import restar

def test_restar():
    assert restar(10, 4) == 6
    assert restar(5, 5) == 0