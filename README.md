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
