def solution(board, moves):
    basket = []
    answer = 0
    for j in moves:
        for i in range(len(board)):
            if board[i][j-1] != 0:      
                basket.append(board[i][j-1])		
                board[i][j-1] = 0
                
                if len(basket) >= 2:
                    while (basket[-1] == basket[-2]):   
                        basket.pop()
                        basket.pop()
                        answer += 2
                        if len(basket) < 2:
                            break
                break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))