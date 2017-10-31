# 一个测试类创建多个测试用例


class TestClass:
    def test_one(self):
        x = "this"
        assert "s" in x

    def test_two(self):
        x = "hello"
        assert x == "hi"
