from stack import Stack



def validParentheses(symbols):

    s = Stack()
    i = 0

    start = '({['
    end = ')}]'

    while i < len(symbols):

        symbol = symbols[i]

        if symbol not in start + end:
            pass

        elif symbol in start:
            s.push(symbol)

        else:

            if s.isEmpty() or start.index(s.pop()) != end.index(symbol):
                return False

        i += 1

    return s.isEmpty()



if __name__ == '__main__':


    assert validParentheses('((()))') == True
    assert validParentheses('(()()()())') == True
    assert validParentheses('(((())))') == True
    assert validParentheses('(()((())()))') == True
    assert validParentheses('(()') == False
    assert validParentheses('((((((())') == False
    assert validParentheses('()))') == False
    assert validParentheses('(()()(()') == False
    assert validParentheses('()[]{}') == True
    assert validParentheses('(]') == False
    assert validParentheses('([)]') == False
    assert validParentheses('{[]}') == True
    assert validParentheses('( ( ( ) ] ) )') == False
    assert validParentheses('( [ ) ]') == False
    assert validParentheses('[ { ( ) ]') == False
