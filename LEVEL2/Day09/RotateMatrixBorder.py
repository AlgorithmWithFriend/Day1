# 38. 행렬 테두리 회전하기

def solution(rows, columns, queries):
    answer = []

    # 행렬 만들기
    board = [[] for _ in range(rows)]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            board[i - 1].append((i - 1) * columns + j)

    for x1, y1, x2, y2 in queries:
        temp = board[x1 - 1][y2 - 1]
        min_value = 10001

        # 북쪽 테두리
        min_value = min(min(board[x1 - 1][y1 - 1: y2 - 1]), min_value)
        board[x1 - 1][y1:y2] = board[x1 - 1][y1 - 1: y2 - 1]

        # 서쪽 테두리
        for i in range(x1, x2):
            min_value = min(board[i][y1 - 1], min_value)
            board[i - 1][y1 - 1] = board[i][y1 - 1]

        # 남쪽 테두리
        min_value = min(min(board[x2 - 1][y1:y2]), min_value)
        board[x2 - 1][y1 - 1:y2 - 1] = board[x2 - 1][y1:y2]

        # 동쪽 테두리
        for i in range(x2 - 2, x1 - 2, -1):
            min_value = min(board[i][y2 - 1], min_value)
            board[i + 1][y2 - 1] = board[i][y2 - 1]

        board[x1][y2 - 1] = temp
        min_value = min(min_value, temp)

        answer.append(min_value)
    return answer

rows_1 = 6
rows_2 = 3
rows_3 = 100

columns_1 = 6
columns_2 = 3
columns_3 = 97

queries_1 = [[2, 2, 5, 4],
             [3, 3, 6, 6],
             [5, 1, 6, 3]
             ]
queries_2 = [[1, 1, 2, 2],
             [1, 2, 2, 3],
             [2, 1, 3, 2],
             [2, 2, 3, 3]
             ]
queries_3 = [[1, 1, 100, 97]]

# print(solution(rows_1, columns_1, queries_1))
# print(solution(rows_2, columns_2, queries_2))
# print(solution(rows_3, columns_3, queries_3))

import numpy as np
def solution_mine(rows, columns, queries):
    answer = []

    '''
    [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     ...
    만들기 성공
    '''
    matrix = []
    for i in range(1, rows * columns - rows + 2, rows):
        tmp = []
        for j in range(i, columns + i):
            tmp.append(j)
        matrix.append(tmp)
    matrix_np = np.array(matrix)

    # 회전을 어떻게 시켜야할지 구현이 안 됨.
    for query in queries:
        x1, y1, x2, y2 = query
        mid_x = round((x2 - x1) / 2)
        mid_y = round((y2 - y1) / 2)
        change_matrix = matrix_np[x1 - 1:x2 - x1][y1 - 1:y2 - y1]
        print(change_matrix)
    return answer

def solution_other(rows, columns, queries):
    answer = []

    # 행렬 만들기
    array = [[0 for col in range(columns)] for row in range(rows)]
    t = 1
    for row in range(rows):
        for col in range(columns):
            array[row][col] = t
            t += 1

    for x1, y1, x2, y2 in queries:
        tmp = array[x1 - 1][y1 - 1]
        mini = tmp

        for k in range(x1 - 1, x2 - 1):
            test = array[k + 1][y1 - 1]
            array[k][y1 - 1] = test
            mini = min(mini, test)

        for k in range(y1 - 1, y2 - 1):
            test = array[x2 - 1][k + 1]
            array[x2 - 1][k] = test
            mini = min(mini, test)

        for k in range(x2 - 1, x1 - 1, -1):
            test = array[k - 1][y2 - 1]
            array[k][y2 - 1] = test
            mini = min(mini, test)

        for k in range(y2 - 1, y1 - 1, -1):
            test = array[x1 - 1][k - 1]
            array[x1 - 1][k] = test
            mini = min(mini, test)

        array[x1 - 1][y1] = tmp
        answer.append(mini)

    return answer

print(solution_other(rows_1, columns_1, queries_1))
print(solution_other(rows_2, columns_2, queries_2))
print(solution_other(rows_3, columns_3, queries_3))