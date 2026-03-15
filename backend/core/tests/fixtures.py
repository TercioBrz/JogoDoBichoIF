import pytest
from betengine.bet_generate_numbers import gerar_cinco_milhares

@pytest.fixture
def milhares_sorteadas():
    return gerar_cinco_milhares()


@pytest.fixture
def milhares():
    datas = (
        "0001",
        "1152",
        "1010",
        "1305",
        "2004"
    )

    return datas


@pytest.fixture
def animal():
    avestruz = ('01','02','03','04')

    return avestruz

@pytest.fixture
def animais():
    Aguia = ('05','06','07','08')
    Burro = ('09','10','11','12')

    return [Aguia, Burro]

