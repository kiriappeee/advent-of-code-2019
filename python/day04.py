def is_password_valid(password_to_validate):
    character_to_match = ''
    number_to_be_larger_than = -1
    has_adjacent_characters = False
    has_only_increasing_or_same_numbers = True
    for c in password_to_validate:
        if character_to_match == c:
            has_adjacent_characters = True
        else:
            character_to_match = c
        if number_to_be_larger_than > int(c):
            has_only_increasing_or_same_numbers = False
            break
        else:
            number_to_be_larger_than = int(c)
    return has_adjacent_characters & has_only_increasing_or_same_numbers

def is_password_valid_v2(password_to_validate):
    matching_character_sets = []
    character_to_match = ''
    number_to_be_larger_than = -1
    has_only_increasing_or_same_numbers = True
    has_correct_matching_sets = False
    current_matching_set = ''
    for c in password_to_validate:
        if number_to_be_larger_than > int(c):
            has_only_increasing_or_same_numbers = False
            break
        else:
            number_to_be_larger_than = int(c)
        if character_to_match == c:
            current_matching_set += c
        else:
            if len(current_matching_set) >= 2:
                matching_character_sets.append(current_matching_set)
            current_matching_set = c
            character_to_match = c
    if len(current_matching_set) >= 2:
        matching_character_sets.append(current_matching_set)
    for matching_set in matching_character_sets:
        if len(matching_set) == 2:
            has_correct_matching_sets = True
            break
    return has_correct_matching_sets & has_only_increasing_or_same_numbers

def get_input():
    input_range = open('python/inputday04.txt').readlines()[0].strip()
    return [int(num) for num in input_range.split('-')]

def run_part_one():
    starting_number, ending_number = get_input()
    number_of_valid_passwords = 0
    for i in range(starting_number, ending_number):
        if is_password_valid(str(i)):
            number_of_valid_passwords += 1
    return number_of_valid_passwords

def run_part_two():
    starting_number, ending_number = get_input()
    number_of_valid_passwords = 0
    for i in range(starting_number, ending_number):
        if is_password_valid_v2(str(i)):
            number_of_valid_passwords += 1
    return number_of_valid_passwords

if __name__ == "__main__":
    print("== DAY 4 - PART 1 ==")
    print(run_part_one())
    print("== DAY 4 - PART 2 ==")
    print(run_part_two())