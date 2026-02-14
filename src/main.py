"""Main module for uv-template."""

from src.modules.first_module import print_hello


def calculate_area(width: float, height: float) -> float:
    """사각형의 넓이를 계산합니다.

    Args:
        width (float): 사각형의 가로 길이.
        height (float): 사각형의 세로 길이.

    Returns:
        float: 계산된 사각형의 넓이.

    Raises:
        ValueError: width나 height가 음수일 경우 발생합니다.

    Example:
        >>> calculate_area(10, 5)
        50.0
    """
    if width < 0 or height < 0:
        raise ValueError("Dimensions must be positive")
    return width * height


def add(a: int, b: int) -> int:
    """두 정수를 더합니다.

    Args:
        a (int): 첫 번째 정수.
        b (int): 두 번째 정수.

    Returns:
        int: 두 정수의 합.
    """
    return a + b


def main() -> None:
    """메인 함수입니다."""
    print("Hello from uv-template!")
    print_hello("uv-template")


if __name__ == "__main__":
    main()
