import pytest
from stat_funcs import StatsN2

@pytest.mark.media
def test_media_com_lista_vazia():
    with pytest.raises(ZeroDivisionError):
        StatsN2.media([])

@pytest.mark.xfail(reason="Esperando que a função seja corrigida")
def test_media_com_valores_negativos():
    assert StatsN2.media([-1, -2, -3, -4, -5]) == -3.0