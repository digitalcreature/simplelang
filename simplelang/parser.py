#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by Grako.
#
#    https://pypi.python.org/pypi/grako/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals

from grako.buffering import Buffer
from grako.parsing import graken, Parser
from grako.util import re, RE_FLAGS, generic_main  # noqa


__all__ = [
    'SimpleLangParser',
    'SimpleLangSemantics',
    'main'
]

KEYWORDS = {}


class SimpleLangBuffer(Buffer):
    def __init__(
        self,
        text,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        namechars='',
        **kwargs
    ):
        super(SimpleLangBuffer, self).__init__(
            text,
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            namechars=namechars,
            **kwargs
        )


class SimpleLangParser(Parser):
    def __init__(
        self,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        left_recursion=False,
        parseinfo=True,
        keywords=None,
        namechars='',
        buffer_class=SimpleLangBuffer,
        **kwargs
    ):
        if keywords is None:
            keywords = KEYWORDS
        super(SimpleLangParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            parseinfo=parseinfo,
            keywords=keywords,
            namechars=namechars,
            buffer_class=buffer_class,
            **kwargs
        )

    @graken()
    def _start_(self):

        def block0():
            self._expression_()
        self._closure(block0)
        self._check_eof()

    @graken('Expression')
    def _expression_(self):
        with self._choice():
            with self._option():
                self._assign_()
            with self._option():
                self._sum_()
            self._error('no available options')

    @graken('Assign')
    def _assign_(self):
        self._sum_()
        self.name_last_node('left')
        self._token('=')
        self.name_last_node('op')
        self._cut()
        self._expression_()
        self.name_last_node('right')
        self.ast._define(
            ['left', 'op', 'right'],
            []
        )

    @graken()
    def _sum_(self):
        with self._choice():
            with self._option():
                self._add_()
            with self._option():
                self._sub_()
            with self._option():
                self._factor_()
            self._error('no available options')

    @graken('Add')
    def _add_(self):
        self._factor_()
        self.name_last_node('left')
        self._token('+')
        self.name_last_node('op')
        self._cut()
        self._sum_()
        self.name_last_node('right')
        self.ast._define(
            ['left', 'op', 'right'],
            []
        )

    @graken('Subtract')
    def _sub_(self):
        self._factor_()
        self.name_last_node('left')
        self._token('-')
        self.name_last_node('op')
        self._cut()
        self._sum_()
        self.name_last_node('right')
        self.ast._define(
            ['left', 'op', 'right'],
            []
        )

    @graken()
    def _factor_(self):
        with self._choice():
            with self._option():
                self._mult_()
            with self._option():
                self._div_()
            with self._option():
                self._atom_()
            self._error('no available options')

    @graken('Multiply')
    def _mult_(self):
        self._atom_()
        self.name_last_node('left')
        self._token('*')
        self.name_last_node('op')
        self._cut()
        self._factor_()
        self.name_last_node('right')
        self.ast._define(
            ['left', 'op', 'right'],
            []
        )

    @graken('Divide')
    def _div_(self):
        self._atom_()
        self.name_last_node('left')
        self._token('/')
        self.name_last_node('op')
        self._cut()
        self._factor_()
        self.name_last_node('right')
        self.ast._define(
            ['left', 'op', 'right'],
            []
        )

    @graken()
    def _atom_(self):
        with self._choice():
            with self._option():
                self._token('(')
                self._expression_()
                self.name_last_node('@')
                self._token(')')
            with self._option():
                self._NUMBER_()
            with self._option():
                self._IDENTIFIER_()
            self._error('no available options')

    @graken('Number')
    def _NUMBER_(self):
        self._pattern(r'[+-]?([0-9]*.)?[0-9]+')
        self.name_last_node('value')
        self.ast._define(
            ['value'],
            []
        )

    @graken('Identifier')
    def _IDENTIFIER_(self):
        self._pattern(r'[a-zA-Z_@$#%][a-zA-Z0-9_@$#%]*')
        self.name_last_node('id')
        self.ast._define(
            ['id'],
            []
        )


class SimpleLangSemantics(object):
    def start(self, ast):
        return ast

    def expression(self, ast):
        return ast

    def assign(self, ast):
        return ast

    def sum(self, ast):
        return ast

    def add(self, ast):
        return ast

    def sub(self, ast):
        return ast

    def factor(self, ast):
        return ast

    def mult(self, ast):
        return ast

    def div(self, ast):
        return ast

    def atom(self, ast):
        return ast

    def NUMBER(self, ast):
        return ast

    def IDENTIFIER(self, ast):
        return ast


def main(filename, startrule, **kwargs):
    with open(filename) as f:
        text = f.read()
    parser = SimpleLangParser(parseinfo=False)
    return parser.parse(text, startrule, filename=filename, **kwargs)


if __name__ == '__main__':
    import json
    ast = generic_main(main, SimpleLangParser, name='SimpleLang')
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()
