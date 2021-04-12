def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    result = ''
    for letter in new_id:
        if letter.isalnum() or letter in '-_.':
            result += letter
    new_id = result

    # 3
    count = 0
    result = ''
    for letter in new_id:
        if letter == '.':
            count += 1
            if count > 1:
                continue
        else:
            count = 0
        result += letter
    new_id = result

    # 4
    new_id = new_id.strip('.')

    # 5
    if new_id == '':
        new_id += 'a'
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.strip('.')
    # 7
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id
