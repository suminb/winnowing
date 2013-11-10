# -*- coding: utf-8 -*- 

__author__ = 'Sumin Byeon'

# DEFINITION 1 (WINNOWING). In each window select the minimum hash value. If
# there is more than one hash with the minimum value, select the rightmost
# occurrence. Now save all selected hashes as the fingerprints of the document.

# Note the record function must compute the global position using the relative
# position, min. Saving this position, together with the selected hash, creates
# a fingerprint.

def sanitize(text):
    """Removes irrelevant features such as spaces and commas.

    :param text: A string of (index, character) tuples.
    """

    import re

    # NOTE: \p{L} or \p{Letter}: any kind of letter from any language.
    # http://www.regular-expressions.info/unicode.html
    p = re.compile(r'\w', re.UNICODE)

    def f(c):
        return p.match(c[1]) != None

    return filter(f, map(lambda x: (x[0], x[1].lower()), text))


def kgrams(text, k=5):
    """Derives k-grams from text."""

    n = len(text)

    if n < k:
        yield text
    else:
        for i in xrange(n - k + 1):
            yield text[i:i+k]


def winnowing_hash(kgram):
    """
    :param kgram: e.g., [(0, 'a'), (2, 'd'), (3, 'o'), (5, 'r'), (6, 'u')]
    """
    kgram = zip(*kgram)

    # FIXME: What should we do when kgram is shorter than k?
    text = ''.join(kgram[1]) if len(kgram) > 1 else ''

    hs = hash_function(text)

    # FIXME: What should we do when kgram is shorter than k?
    return (kgram[0][0] if len(kgram) > 1 else -1, hs)


def default_hash(text):
    import hashlib
    
    hs = hashlib.sha1(text.encode('utf-8'))
    hs = hs.hexdigest()[-4:]
    hs = int(hs, 16)

    return hs


def select_min(window):
    """In each window select the minimum hash value. If there is more than one
    hash with the minimum value, select the rightmost occurrence. Now save all
    selected hashes as the fingerprints of the document.

    :param window: A list of (index, hash) tuples.
    """

    #print window, min(window, key=lambda x: x[1])
    
    return min(window, key=lambda x: x[1])


def winnow(text, k=5):
    n = len(text)

    text = zip(xrange(n), text)
    text = sanitize(text)

    hashes = map(lambda x: winnowing_hash(x), kgrams(text, k))

    windows = map(None, kgrams(hashes, 4))

    return set(map(select_min, windows))


# Specified a hash function. You may override this.
hash_function = default_hash
