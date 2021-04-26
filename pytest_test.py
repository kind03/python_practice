# test_sample.py
# 被测功能
def func(x):
    return x + 1


# 测试成功
def test_pass():
    assert func(3) == 4


# 测试失败
def test_pass2():
    assert func(4) == 5
