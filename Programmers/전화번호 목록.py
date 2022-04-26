def solution(phone_book):
    check_list = {}
    total_num = len(phone_book)
    for i in range(total_num):
        if len(phone_book[i]) in check_list:
            check_list[len(phone_book[i])][phone_book[i]] = len(phone_book[i])
            continue
        check_list[len(phone_book[i])] = {}
        check_list[len(phone_book[i])][phone_book[i]] = len(phone_book[i])

    answer = True
    for i in range(total_num):
        if answer == False:
            break
        for key in check_list:
            if key < len(phone_book[i]):
                if phone_book[i][:key] in check_list[key]:
                    answer = False
                    break
    return answer