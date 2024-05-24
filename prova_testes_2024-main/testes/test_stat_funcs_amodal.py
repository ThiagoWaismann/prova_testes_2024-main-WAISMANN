import pytest
from stat_funcs import StatsN2

@pytest.mark.amodal
def test_amodal_com_lista_amodal():
    assert StatsN2.amodal([1, 2, 3, 4, 5]) == "Não existe moda"

@pytest.mark.amodal
def test_amodal_com_lista_modal():
    assert StatsN2.amodal([1, 1, 2, 3, 3, 3]) == "Existe moda"

@pytest.mark.amodal
def test_amodal_com_lista_vazia():
    assert StatsN2.amodal([]) == "Não existe moda"

@pytest.mark.xfail(reason="Propositalmente falho")
@pytest.mark.amodal
def test_amodal_com_falha_esperada():
    assert StatsN2.amodal([1, 2, 3]) == "Existe moda"
