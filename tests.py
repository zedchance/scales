import unittest
from scales import _get_fret_number


class TestScales(unittest.TestCase):

    def test_fret_num(self):
        assert _get_fret_number('E', 'A') == 5
        assert _get_fret_number('D', 'E') == 2
        assert _get_fret_number('G', 'C') == 5
        assert _get_fret_number('A', 'G#') == 11
        assert _get_fret_number('E', 'E') == 0
        assert _get_fret_number('E', 'F') == 1
        assert _get_fret_number('E', 'B') == 7
        assert _get_fret_number('E', 'A##') == 7
        assert _get_fret_number('E', 'C') == 8
        assert _get_fret_number('E', 'B#') == 8
        assert _get_fret_number('E', 'Dbb') == 8
        assert _get_fret_number('B', 'E') == 5


if __name__ == '__main__':
    unittest.main()
