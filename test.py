from testify import *
from winnow import *

class DefaultTestCase(TestCase):
    def test_fingerprinting(self):
        actual = winnow('A do run run run, a do run run')
        expected = set([(5, 23942), (14, 2887), (2, 1966), (9, 23942), (20, 1966)])
        assert_equal(actual, expected)

if __name__ == "__main__":
    run()
