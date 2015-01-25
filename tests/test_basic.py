from winnowing import *


def test_fingerprinting():
    actual = winnow('A do run run run, a do run run')
    expected = set([(5, 23942), (14, 2887), (2, 1966), (9, 23942), (20, 1966)])
    assert actual == expected


def test_custom_hash():
    def hash_md5(text):
        import hashlib

        hs = hashlib.md5(text.encode('utf-8'))
        hs = hs.hexdigest()
        hs = int(hs, 16)

        return hs

    import winnowing

    # Override the hash function
    winnowing.hash_function = hash_md5

    actual = winnowing.winnow('The cake was a lie')
    expected = set([(9, 65919358278261454015134408903900174701),
        (6, 10871086811686999948319704115083909333),
        (5, 89272493548844644660374857453353035753),
        (2, 119020521100057720362335995528842780418)])

    assert actual == expected

    # Restore the hash function
    winnowing.hash_function = winnowing.default_hash
