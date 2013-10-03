from testify import *
from winnow import *

class DefaultTestCase(TestCase):
    def test_fingerprinting(self):
        actual = winnow('A do run run run, a do run run')
        expected = set([(5, 23942), (14, 2887), (2, 1966), (9, 23942), (20, 1966)])
        assert_equal(actual, expected)

    def test_custom_hash(self):
        def hash_md5(text):
            import hashlib

            hs = hashlib.md5(text)
            hs = hs.hexdigest()
            hs = int(hs, 16)

            return hs

        import winnow

        # Override the hash function
        winnow.hash_function = hash_md5

        actual = winnow.winnow('The cake was a lie')
        expected = set([(9, 65919358278261454015134408903900174701L),
            (6, 10871086811686999948319704115083909333L),
            (5, 89272493548844644660374857453353035753L),
            (2, 119020521100057720362335995528842780418L)])

        assert_equal(actual, expected)

        # Restore the hash function
        winnow.hash_function = winnow.default_hash

if __name__ == "__main__":
    run()
