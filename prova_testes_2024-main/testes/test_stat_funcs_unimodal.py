import pytest
from stat_funcs import StatsN2

@pytest.mark.unimodal
def test_unimodal_com_lista_unimodal():
    assert StatsN2.unimodal([1, 2, 3, 3, 4, 5]) == 3

@pytest.mark.unimodal
def test_unimodal_com_lista_nao_unimodal():
    assert StatsN2.unimodal([1, 2, 2, 3, 4, 5]) == "Não é unimodal"

@pytest.mark.unimodal
def test_unimodal_com_lista_vazia():
    assert StatsN2.unimodal([]) == "Não é unimodal"

@pytest.mark.xfail(reason="Propositalmente falho")
@pytest.mark.unimodal
def test_unimodal_com_falha_esperada():
    assert StatsN2.unimodal([1, 2, 3]) == 4
