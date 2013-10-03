Winnowing
=========

A Python implementation of the Winnowing (local algorithms for document fingerprinting)

Original Work
=============

The original research paper can be found at <http://dl.acm.org/citation.cfm?id=872770>.

Usage
=====

    >>> winnow('A do run run run, a do run run')
    set([(5, 23942), (14, 2887), (2, 1966), (9, 23942), (20, 1966)])
    
    >>> winnow('run run')
    set([(0, 23942)]) # match found!

### Default Hash Function

Quite honestly, I did not know what hash function to use. The paper did not talk about it. So I decided to use a part of SHA-1; more precisely, the last 16 bits of the digest.


### Custom Hash Function

You may use your own hash function as demonstrated below.

    def hash_md5(text):
        import hashlib

        hs = hashlib.md5(text)
        hs = hs.hexdigest()
        hs = int(hs, 16)

        return hs

    # Override the hash function
    winnow.hash_function = hash_md5

    winnow('The cake was a lie')

### Lower Bound of Fingerprint Density

(TODO: Write this section)

