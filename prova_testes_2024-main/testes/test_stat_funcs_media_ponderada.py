import pytest
from stat_funcs import StatsN2

@pytest.mark.media_ponderada
@pytest.mark.parametrize("lista, pesos, expected", [
    ([1, 2, 3, 4, 5], [0.1, 0.2, 0.3, 0.4, 0.5], 3.6667),
    ([1, 2, 3], [0.2, 0.3, 0.5], 2.5),
    ([], [], ValueError),
])
def test_media_ponderada(lista, pesos, expected):
    if expected == ValueError:
        with pytest.raises(ValueError):
            StatsN2.media_ponderada(lista, pesos)
    else:
        assert pytest.approx(StatsN2.media_ponderada(lista, pesos)) == expected