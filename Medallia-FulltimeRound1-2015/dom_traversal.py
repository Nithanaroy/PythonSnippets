#!/bin/python

# Check Google Drive Interview Experiences folder for entire question

import re
import collections

"""
An 'Element' node of the DOM tree.
@param tag: string
@param id: string
@param children: array of nodes which could be either 'Element' or 'Content' instances
"""


class Element:
    def __init__(self, tag, id, children):
        self.tag = tag
        self.id = id
        self.children = children


"""
A 'Content' node of the DOM tree
@param content: string
"""


class Content:
    def __init__(self, content):
        self.content = content


"""
A 'DOM' tree
@param root: an instance of 'Element' which represents to the root of the tree
"""


class Dom:
    def __init__(self, root):
        self.root = root


"""
Complete the function below.
@param dom: An instance of the Dom class
@param whiteList: An array of strings
@return the output that will be sent to the STDOUT
"""


def format(dom, whiteList):
    hash = {}
    level_order(hash, dom.root, 0, whiteList)
    res = ""
    for l in hash:
        ls = ""
        for e in hash[l]:
            ls += get_element_string(e) + " "
        res += (ls.strip() + "\n")
    res.strip()
    return res


def get_element_string(e):
    str = e.tag
    if e.id:
        str += " " + e.id

    # get direct content children
    for c in e.children:
        if isinstance(c, Content):
            str += " " + c.content
    return str


def level_order(hash, node, level, whitelist):
    if node:
        # element node only
        s = get_element_string(node)
        for w in whitelist:
            if w in s:
                return  # ignore this node and its children

        upsert(hash, level, node)
        for c in node.children:
            # can be an element or content node
            if isinstance(c, Element):
                level_order(hash, c, level + 1, whitelist)


def upsert(hash, key, value):
    if key in hash:
        hash[key].append(value)
    else:
        hash[key] = [value]


"""
The following code is not relevant for this exercise. It is only here to help
running the tests.
"""


def main():
    _html = raw_input()
    _whiteList = raw_input()
    _whiteListArray = [] if not _whiteList else _whiteList.split(",")
    _dom = Dom(Parser(_html).parse())

    _output = format(_dom, _whiteListArray)

    print _output


class Token:
    def __init__(self, type, tag, id, content):
        self.type = type
        self.tag = tag
        self.id = id
        self.content = content


class Parser:
    START_ELEMENT_PATTERN = re.compile('^<(.*?)>')
    END_ELEMENT_PATTERN = re.compile('^<\/(.*?)>')
    CLASS_PATTERN = re.compile("(.*) id='(.*)'")
    CONTENT_PATTERN = re.compile('^(.*?)<')

    def __init__(self, html):
        self.position = 0
        self.tokens = self.tokenise(html)

    def parse(self):
        return self._parse()

    def _parse(self):
        _token = self.tokens[self.position]
        _children = []
        self.position += 1
        while self.position < len(self.tokens):
            _currentToken = self.tokens[self.position]
            if _currentToken.type == 'START':
                _children.append(self._parse())
            elif _currentToken.type == 'CONTENT':
                _children.append(Content(_currentToken.content))
            else:
                break
            self.position += 1
        return Element(_token.tag, _token.id, _children)

    def tokenise(self, input):
        _tokens = []
        while input:
            _endElement = self.END_ELEMENT_PATTERN.match(input)
            if _endElement:
                _tokens.append(Token('END', _endElement.group(1), None, None))
                input = input[len(_endElement.group(0)):]
            else:
                _startElement = self.START_ELEMENT_PATTERN.match(input)
                if _startElement:
                    _classElement = self.CLASS_PATTERN.match(_startElement.group(1))
                    if _classElement:
                        _tokens.append(Token('START', _classElement.group(1), _classElement.group(2), None))
                    else:
                        _tokens.append(Token('START', _startElement.group(1), None, None))
                    input = input[len(_startElement.group(0)):]
                else:
                    _content = self.CONTENT_PATTERN.match(input)
                    if _content:
                        _tokens.append(Token('CONTENT', None, None, _content.group(1)))
                        input = input[len(_content.group(1)):]
                    else:
                        _tokens.append(Token('CONTENT', None, None, input))
                        input = ''
        return _tokens


main()
