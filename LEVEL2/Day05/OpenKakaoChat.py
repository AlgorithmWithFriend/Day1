def solution(records):
    # 문자열이 매핑 함수로 인해서 문자열이 하나씩 들어가고 이 문자열을 split해주고 리스트로 바꿔서 반환을 해준다.
    records = list(map(lambda r : r.split(), records))
    # userId, nickname을 딕셔너리를 이용해 key : value 형태로 구분해준다.
    # 또한 리스트를 순회하면서 마지막에 있는 이름으로 바꿔준다.
    users = {}
    for record in records:
        # Leave uid1234라는 경우 제외하고 생각
        if len(record) > 2:
            users[record[1]] = record[2]
    
    msg = {'Enter' : '님이 들어왔습니다.', 'Leave' : '님이 나갔습니다.'}
    message = []
    for record in records:
        if record[0] != 'Change':        
            message.append(users[record[1]] + msg[record[0]])
    return message
            