import pytest
from stat_funcs import StatsN2

@pytest.mark.variancia
def test_variancia_com_valores_positivos():
    assert pytest.approx(StatsN2.variancia([1, 2, 3, 4, 5])) == 2.5

@pytest.mark.variancia
def test_variancia_com_valores_negativos():
    assert pytest.approx(StatsN2.variancia([-1, -2, -3, -4, -5])) == 2.5

@pytest.mark.variancia
def test_variancia_com_lista_vazia():
    assert pytest.approx(StatsN2.variancia([])) == 0

@pytest.mark.xfail(reason="Propositalmente falho")
@pytest.mark.variancia
def test_variancia_com_falha_esperada():
    assert pytest.approx(StatsN2.variancia([1, 2, 3])) == 2.0
