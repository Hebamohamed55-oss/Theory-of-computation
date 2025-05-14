def CYK_parser(grammar, string):
    n = len(string)

    table = [[set() for _ in range(n)] for _ in range(n)]


    for i in range(n):
        for lhs, rhs_list in grammar.items():
            for rhs in rhs_list:
                if len(rhs) == 1 and rhs[0] == string[i]:
                    table[i][i].add(lhs)

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                for lhs, rhs_list in grammar.items():
                    for rhs in rhs_list:
                        if len(rhs) == 2 and rhs[0] in table[i][k] and rhs[1] in table[k + 1][j]:
                            table[i][j].add(lhs)

    return 'S' in table[0][n - 1]


grammar = {
    'S': [('A', 'B'), ('B', 'A')],
    'A': [('a',)],
    'B': [('b',)]
}

string = "ab"
print(CYK_parser(grammar, string))  
