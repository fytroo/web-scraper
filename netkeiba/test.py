from parameterized import parameterized
import nkapi


@parameterized([
    (1, 3, 4),
    (-200, -80, -280),
    (-3, 0, -3)])
def test_add(x1, x2, expect):

    assert nkapi.add(x1, x2) == expect
