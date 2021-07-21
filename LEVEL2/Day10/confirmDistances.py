# 방향 벡터 사용
# 멘힌튼 거리가 1인것은 아래와 같다.
# 나를 기준으로 상하좌우
dx1 = [1, 0, -1, 0]
dy1 = [0, 1, 0, -1]

# 맨힌튼 거리가 1이고 대각선으로 좌상, 상우, 우하, 우좌 
dx2 = [1, -1, 1, -1]
dy2 = [1, 1, -1, -1]

# 멘힌튼 거리가 2인경우
dx3 = [2, 0, -2, 0]
dy3 = [0, 2, 0, -2]

# 범위 넘기는거 방지 함수
def OOB(x, y):
    return x < 0 or x > 4 or y < 0 or y > 4

def chk(board):
    for i in range(5):
        for j in range(5):
            # 내가 보는 i,j칸이 사람이 아니면 패스
            if board[i][j] != 'P':
                continue
            for dirs in range(4):
                nx = i+dx1[dirs]
                ny = j+dy1[dirs]
                # nx ny에 사람이 있으면 애초에 나가리 그래서 0반환
                if not OOB(nx, ny) and board[nx][ny] == 'P':
                    return 0
            for dirs in range(4):
                nx = i+dx2[dirs]
                ny = j+dy2[dirs] 
                if not OOB(nx, ny) and board[nx][ny] == 'P':                # 1사분면 2사분면 칸을 확인
                    if board[i][ny] != 'X' or board[nx][j] !='X':
                        return 0
            for dirs in range(4):
                nx = i+dx3[dirs]
                ny = j+dy3[dirs]
                if not OOB(nx, ny) and board[nx][ny] == 'P':                # 가운데 확인하는 코드 즉, 파티션
                    if board[i+dx1[dirs]][j+dy1[dirs]] != 'X':
                        return 0
    return 1

def solution(places):
    answer = []
    # 입력값을 for문을 돌아서 return값 append
    for p in places:
        answer.append(chk(p))
    return answer