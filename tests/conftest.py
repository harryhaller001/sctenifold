import pytest

from scTenifold.data import fetch_data


@pytest.fixture(scope="session")
def morphine_datasets():
    """Fetch morphine dataset."""
    morphine = fetch_data("morphine")
    return morphine


@pytest.fixture(scope="session")
def aging_datasets():
    """Fetch aging dataset."""
    aging = fetch_data("aging")
    return aging
