
from .fixtures import milhares,milhares_sorteadas,animal,animais
from betengine.bet_numbers_checks import BetNumbersChecks
import pytest

def test_que_verificar_se_milhares_sao_geradas_corretamente(milhares_sorteadas):

    for milhar in milhares_sorteadas:
        assert len(milhar) == 4 and 0 <= int(milhar) <= 9999 and len(milhares_sorteadas) == 5

def test_que_valida_aposta_modalidade_grupo_head(milhares,animal):

    grupo = BetNumbersChecks(milhares)
    ans = grupo.modalidade_grupo(animal,True)

    assert ans == {'group': 18}

def test_que_valida_aposta_modalidade_grupo(milhares,animal):

    grupo = BetNumbersChecks(milhares)
    ans = grupo.modalidade_grupo(animal)

    assert ans == {'group': 3.6}

@pytest.mark.parametrize('dezena',
    [
        ('01','02','03','04'),
        pytest.param(('09','10','11','12'),marks=pytest.mark.xfail(reason="Error Forcado",strict=True))
    ],
    ids=["Dezena-1","Dezena-2"]
)

def test_que_valida_aposta_modalidade_dezena_head(milhares,dezena):

    dez = BetNumbersChecks(milhares)
    ans = dez.modalidade_dezena(dezena,True)

    assert ans ==  {'01': 60}

@pytest.mark.parametrize(
    'dezena,esperado',
    [
        (('01','02','03','04'), {'01': 12, '04': 12}),
        (('09','10','11','12'),{'10': 12})
    ],
    ids=["Dezena-1","Dezena-2"]
)
def test_que_valida_aposta_modalidade_dezena(milhares,dezena,esperado):

    dez = BetNumbersChecks(milhares)
    ans = dez.modalidade_dezena(dezena)

    assert ans == esperado


@pytest.mark.parametrize('centena',[
    ("001","417","152","322","064")
    ]
)
def test_que_valida_aposta_modalidade_centena_head(milhares,centena):

    cem = BetNumbersChecks(milhares)
    ans = cem.modalidade_centena(centena,True)
    assert ans == {'001': 600}

@pytest.mark.parametrize('centena',[
    ("001","417","152","322","064")
    ],ids=["Centenas-1"]
)
def test_que_valida_aposta_modalidade_centena_head(milhares,centena):

    cem = BetNumbersChecks(milhares)
    ans = cem.modalidade_centena(centena)
    assert ans ==  {'001': 120, '152': 120}


@pytest.mark.parametrize('milhar',[
    ("0001","2417","3152","4322","5064")
    ],ids=["Milhar-1"]
)
def test_que_valida_aposta_modalidade_milhar_head(milhares,milhar):

    mil = BetNumbersChecks(milhares)
    ans = mil.modalidade_milhar(milhar,head=True)
    assert ans ==  {'0001': 4000}


@pytest.mark.parametrize('milhar',[
    ("0001","2417","3152","4322","2004")
    ],ids=["Milhar-1"]
)
def test_que_valida_aposta_modalidade_milhar(milhares,milhar):

    mil = BetNumbersChecks(milhares)
    ans = mil.modalidade_milhar(milhar)
    assert ans ==  {'0001': 800, '2004': 800}


def test_que_valida_aposta_modalidade_duque_grupo(milhares,animais):

    anim = BetNumbersChecks(milhares)
    ans = anim.modalidade_duque_grupo(animais)

    assert ans == {'duque': 12.5}


@pytest.mark.parametrize('dezena, esperado',[
    (("01","52"),{'duque': 800}),
    (("04","05"),{'duque': 800}),
    ],ids=["dezena-1","dezena-2"]
)
def test_que_valida_aposta_modalidade_duque_dezena(milhares,dezena,esperado):

    dez = BetNumbersChecks(milhares)
    ans = dez.modalidade_duque_dezena(dezena)
    assert ans == esperado


@pytest.mark.parametrize('grupo, esperado',[
    ([("01","02","03","04"),("05","06","07","08"), ("09","10","11","12")],{'terno': 120}),
    ],ids=["terno-grupo-1"]
)
def test_que_valida_aposta_modalidade_terno_grupo(milhares,grupo,esperado):

    dez = BetNumbersChecks(milhares)
    ans = dez.modalidade_terno_grupo(grupo)
    assert ans == esperado

@pytest.mark.parametrize('dezenas, esperado',[
    (("01","10","52"),{'terno': 3000}),
    ],ids=["terno-dezena-1"]
)
def test_que_valida_aposta_modalidade_terno_dezena(milhares,dezenas,esperado):

    dez = BetNumbersChecks(milhares)
    ans = dez.modalidade_terno_dezena(dezenas)
    assert ans == esperado

