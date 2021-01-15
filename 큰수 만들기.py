def solution(number, k):
    number_of_character_chosen = len(number) - k
    answer = ""
    while(number_of_character_chosen != 0):
        temp_number = number[: len(number) - number_of_character_chosen + 1]
        # print(temp_number)
        biggest_num_with_index = find_biggest_num_in_list(temp_number)
        answer += biggest_num_with_index[0]
        number_of_character_chosen -= 1
        number = number[biggest_num_with_index[1] + 1:]
        k += 1
        # print(answer+"___")
    return answer

def find_biggest_num_in_list(temp_number):
    max_letter_with_index = [temp_number[0],0]
    for idx in range(len(temp_number)):
        if (temp_number[idx] == "9"):
            return ["9",idx]
        if (max_letter_with_index[0] < temp_number[idx]):
            max_letter_with_index[0] = temp_number[idx]
            max_letter_with_index[1] = idx
    return max_letter_with_index

# print(solution("1231234",3))
# print(solution("4177252841",4))