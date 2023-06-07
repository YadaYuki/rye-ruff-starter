from src.hello import hello


def test_hello() -> None:
    assert hello("hoge") == "Hello, hoge"
