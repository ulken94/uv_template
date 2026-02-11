# Project Development Guidelines

이 프로젝트는 **Python 3.12+** 및 **uv**를 기반으로 한 **Flat Layout** 구조를 따릅니다.
프로젝트의 일관성과 유지보수성을 위해 아래 가이드를 준수해 주십시오.

## 1. Project Philosophy & Stack

* **Package Manager**: `uv` (필수) - `pip`를 직접 사용하지 않습니다.
* **Python Version**: `3.12` 이상
* **Linting & Formatting**: `Ruff`
* **Testing**: `Pytest`

## 2. Directory Structure (Flat Layout)

이 프로젝트는 별도의 `src/` 폴더를 두지 않는 **Flat Layout**을 사용합니다.
`main.py`가 프로젝트 루트에 위치하며, 애플리케이션의 진입점(Entry Point) 역할을 합니다.

```text
project-root/
├── .venv/                 # uv가 관리하는 가상환경 (Git 제외)
├── app/                   # (Optional) 핵심 로직 및 모듈
│   ├── __init__.py
│   └── services.py
├── tests/                 # 테스트 코드
│   ├── __init__.py
│   └── test_main.py
├── .gitignore
├── .python-version        # Python 버전 고정 (uv python pin)
├── main.py                # 실행 진입점 (Entry Point)
├── pyproject.toml         # 의존성 및 도구 설정
└── uv.lock                # 의존성 잠금 파일
