import sys
sys.path.append(".\src")

from main import *
from utils import *
from num import *
from sym import *
from data import *

n = 0

def test_the():
    oo(options)
    return True


def test_sym():
    symObj = Sym()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        symObj.add(x)
    return "a" == symObj.mid() and 1.379 == rnd(symObj.div(), 3)


def test_num():
    num = Num()
    for x in [1, 1, 1, 1, 2, 2, 3]:
        num.add(x)
    return 11 / 7 == num.mid() and 0.787 == rnd(num.div(), 3)


def no_of_chars_in_file(t):
    global n
    n += len(t)


def test_csv():
    csv(options['file'], no_of_chars_in_file)
    return n == 8 * 399


def test_data():
    dataObj = DATA(options['file'])
    return len(dataObj.rows) == 398 and dataObj.cols.y[0].w == -1 and dataObj.cols.x[1].at == 1 and len(dataObj.cols.x) == 4


def test_stats():
    data = DATA(options['file'])
    dataDict = {'y': data.cols.y, 'x': data.cols.x}
    for k, cols in dataDict.items():
        print(k, 'mid', data.stats('mid', cols, 2))
        print(' ', 'div', data.stats('div', cols, 2))
        print()
    return True


if __name__ == '__main__':
    eg('the', 'show settings', test_the)
    eg('sym', 'check syms', test_sym)
    eg('num', 'check nums', test_num)
    eg('csv', 'read from csv', test_csv)
    eg('data', 'read DATA csv', test_data)
    eg('stats', 'stats from DATA', test_stats)
    main(options, help, egs)

