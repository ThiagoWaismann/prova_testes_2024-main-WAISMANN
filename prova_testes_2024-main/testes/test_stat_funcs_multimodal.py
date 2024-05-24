import pytest
from stat_funcs import StatsN2

@pytest.mark.multimodal
def test_multimodal_com_lista_multimodal():
    assert StatsN2.multimodal([1, 1, 2, 2, 3, 3, 4, 4]) == [1, 2, 3, 4]

@pytest.mark.multimodal
def test_multimodal_com_lista_nao_multimodal():
    assert StatsN2.multimodal([1, 2, 3, 4, 5]) == "Não é multimodal"

@pytest.mark.multimodal
def test_multimodal_com_lista_vazia():
    assert StatsN2.multimodal([]) == "Não é multimodal"

@pytest.mark.xfail(reason="Propositalmente falho")
@pytest.mark.multimodal
def test_multimodal_com_falha_esperada():
    assert StatsN2.multimodal([1, 2, 3]) == [1, 2, 3]
