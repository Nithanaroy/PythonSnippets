#!/bin/python

# Check Google Drive Interview Experiences folder for entire question

class Token:
    def __init__(self, commentId, sentenceIndex, word):
        self.commentId = commentId
        self.sentenceIndex = sentenceIndex
        self.word = word


class CoOccurrence:
    def __init__(self, word1, word2, count):
        self.word1 = word1
        self.word2 = word2
        self.count = count

    def __str__(self):
        return '(%s, %s, %s)' % (self.word1, self.word2, self.count)


from sets import Set
import operator


def findFrequentCoOccurrences(n, tokens):
    res = []
    c_s = {}
    w_w = {}
    for t in tokens:
        upsert(c_s, (t.commentId, t.sentenceIndex), t.word)
    for cs in c_s:
        ts = sorted(c_s[cs])  # tokens for this comment, sentence sorted lexi
        for i in range(0, len(ts)):
            for j in range(i + 1, len(ts)):
                inc(w_w, (ts[i], ts[j]), 1)

    sorted_w_w = sorted(w_w.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(0, n):
        res.append(CoOccurrence(sorted_w_w[i][0][0], sorted_w_w[i][0][1], sorted_w_w[i][1]))
    return res


def inc(hash, key, inc_by):
    if key in hash:
        hash[key] += inc_by
    else:
        hash[key] = inc_by


def upsert(hash, key, value):
    if key in hash:
        hash[key].add(value)
    else:
        hash[key] = Set([value])


def main():
    _n = int(raw_input())
    _array_size = int(raw_input())
    _tokens = []
    for i in range(0, _array_size):
        _parts = raw_input().split(',')
        _tokens.append(Token(int(_parts[0]), int(_parts[1]), _parts[2]))

    _result = findFrequentCoOccurrences(_n, _tokens)
    _output = ''
    for _item in _result:
        _output += (', ' if _output else '') + '%s' % _item

    print '[%s]' % _output


main()
