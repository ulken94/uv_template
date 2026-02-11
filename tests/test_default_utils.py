from utils.default_utils import greet


# 2. Pytest 코드
def test_greet(capsys):
    # 함수 실행
    greet("World")

    # capsys가 현재까지 콘솔에 출력된 내용을 읽어옵니다.
    captured = capsys.readouterr()

    # captured.out: 표준 출력(stdout)에 찍힌 내용
    # 주의: print() 함수는 끝에 줄바꿈(\n)을 자동으로 추가합니다.
    assert captured.out == "Hello, World!\n"
