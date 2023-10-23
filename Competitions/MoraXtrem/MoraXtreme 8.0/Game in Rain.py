import tokenize
from io import BytesIO

def swap_operators(expression):
    swapped_expression = expression.replace('-', '_').replace('+', '-').replace('_', '+').replace('*', '%').replace('/', '*').replace('%','//').replace('(', '^').replace(')', '(').replace('^', ')')
    return swapped_expression


def tokens_with_base(tokens, base):
    for token in tokens:
        if token.type == tokenize.NUMBER:
            try:
                value = int(token.string, base)
            except ValueError:
                pass
            else:
                token = tokenize.TokenInfo(
                    type   = tokenize.NUMBER,
                    string = str(value),
                    start  = token.start,
                    end    = token.end,
                    line   = token.line
                )

        yield token

def evaluate_expression(string, base):
    tokens = tokenize.tokenize(BytesIO(string.encode()).readline)
    transformed = tokens_with_base(tokens, base)
    return tokenize.untokenize(transformed)


base, expression = input().strip().split(',')
base = int(base)

swapped_expression = swap_operators(expression)

result = eval(evaluate_expression(swapped_expression, base))
split_expression = swapped_expression.split('*')

parts = ''
for i in range(len(split_expression)):
    if i<len(split_expression)-1:
        parts += '(' + split_expression[i] + ')*'
    else:
        parts += '(' + split_expression[i] + ')'


split_expression2 = swapped_expression.split('/')
result2 = eval(evaluate_expression(parts, base))

parts2 = ''

for i in range(len(split_expression2)):
    if i<len(split_expression2)-1:
        parts2 += '(' + split_expression2[i] + ')//'
    else:
        parts2 += '(' + split_expression2[i] + ')'


result3 = eval(evaluate_expression(parts2, base))

max_result = max(result, result2,result3)

print(max_result)
