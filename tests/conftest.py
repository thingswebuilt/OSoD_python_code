from glob import glob


def refactor(string: str) -> str:
    """refactor filepaths into import strings"""
    return string.replace("/", ".").replace("\\", ".").replace(".py", "")


pytest_plugins = [
    refactor(fixture) for fixture in glob("tests/fixtures/*.py") if "__" not in fixture
]
