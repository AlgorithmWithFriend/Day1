# 이 문제는 아주 간단한 구현이다.
# 처음에 순간 2중 for문을 돌릴까...? 라는 생각을 했지만 그렇게 할 필요가 없다고 판단했고,
# 먼저 주어진 좌표를 각각 -1씩해서 인덱스에 맞게 수정을 해준 뒤에
# 왼쪽 아래에서 왼쪽 위, 오른쪽 아래에서 왼쪽 아래, 오른쪽 위에서 오른쪽 아래, 왼쪽 위에서 오른쪽 위 순서대로 회전시키는 방법을 구현하였다.
# 위 방식대로 하다보면 맨 처음시작한 부분이 덮어씌워지기 때문에 temp변수에 따로 빼놓도록 하고,
# 문제에서 요구한것이 회전을 한번 할때마다 가장 작은 값이기 때문에 서대로 회전할때, 4개변을 회전할때, 각 변에서 가장 작은 값을 Min 변수에 넣어주고 min함수를 이용해서 계속 갱신해나가는 방법을 생각했다.

def solution(rows, columns, queries):
    data = [[0]*columns for _ in range(rows)]
    count = 1
    for i in range(rows):
        for j in range(columns):
            data[i][j] += count
            count += 1
    answer = []
    for a,b,c,d in queries:
        x1,y1,x2,y2 = a-1,b-1,c-1,d-1
        temp = data[x1][y1]
        Min = temp
        
        # 왼쪽 아래서 왼쪽 위로 끌어오기
        for i in range(x1,x2):
            flag = data[i+1][y1]
            data[i][y1] = flag
            Min = min(Min,flag)

        # 오른쪽 아래에서 왼쪽 아래로 끌어오기
        for i in range(y1,y2):
            flag = data[x2][i+1]
            data[x2][i] = flag
            Min = min(Min,flag)

        # 오른쪽 위에서 오른쪽 아래로 끌어오기
        for i in range(x2,x1,-1):
            flag = data[i-1][y2]
            data[i][y2] = flag
            Min = min(Min,flag)

        # 왼쪽 위에서 오른쪽 위로 끌어오기
        for i in range(y2,y1,-1):
            flag = data[x1][i-1]
            data[x1][i] = flag
            Min = min(Min,flag)

        # 처음에 시작할 때 빼뒀던 temp 값 위치 시키기
        data[x1][y1+1] = temp
        answer.append(Min)
    return answer