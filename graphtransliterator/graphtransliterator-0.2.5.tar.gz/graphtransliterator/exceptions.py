# -*- coding: utf-8 -*-

"""
Transliteration exceptions used in Graph Transliterator.
"""


class GraphTransliteratorException(Exception):
    """
    Base exception class. All Graph Transliterator-specific exceptions should
    subclass this class.
    """


class AmbiguousTransliterationRulesException(GraphTransliteratorException):
    """
    Raised when multiple transliteration rules can match the same pattern.
    Details of ambiguities are given in a :func:`logging.warning`.
    """


class NoMatchingTransliterationRuleException(GraphTransliteratorException):
    """
    Raised when no transliteration rule can be matched at a particular
    location in the input string's tokens. Details of the location are given
    in a :func:`logging.warning`.
    """


class UnrecognizableInputTokenException(GraphTransliteratorException):
    """
    Raised when a character in the input string does not correspond to any
    tokens in the GraphTransliterator's token settings. Details of the location
    are given in a :func:`logging.warning`.
    """
