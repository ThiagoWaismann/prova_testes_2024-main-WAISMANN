import pytest
from stat_funcs import StatsN2

@pytest.mark.mediana
def test_mediana_com_lista_impar():
    assert StatsN2.mediana([1, 2, 3, 4, 5]) == 3

@pytest.mark.mediana
def test_mediana_com_lista_par():
    assert StatsN2.mediana([1, 2, 3, 4]) == 2.5

@pytest.mark.mediana
def test_mediana_com_lista_vazia():
    assert StatsN2.mediana([]) == 0

@pytest.mark.xfail(reason="Propositalmente falho")
@pytest.mark.mediana
def test_mediana_com_falha_esperada():
    assert StatsN2.mediana([1, 2, 3]) == 4
