def get_input():
    input_for_day = open('python/inputday02.txt', 'r').read().split('\n')[0].split(',')
    return [int(x) for x in input_for_day]

def getNextOperationMembers(array_to_extract_next_operation_from, starting_index=0):
    if array_to_extract_next_operation_from[starting_index] == 99:
        return [99, starting_index]
    elif array_to_extract_next_operation_from[starting_index] == 1 or array_to_extract_next_operation_from[starting_index] == 2:
        operators_to_return = array_to_extract_next_operation_from[starting_index:starting_index+4]
        operators_to_return.append(starting_index)
        return operators_to_return
    else:
        return getNextOperationMembers(array_to_extract_next_operation_from, starting_index+1)

def getNextOperationArray(complete_array, current_index):
    next_operation_members = getNextOperationMembers(complete_array[current_index:])
    if len(next_operation_members) < 4:
        return (complete_array[current_index:], len(complete_array))
    else:
        return (complete_array[current_index:], current_index + 4)

def executeOperation(operation_specification, array_to_read_from):
    if operation_specification[0] == 1:
        return (array_to_read_from[operation_specification[1]]
                + array_to_read_from[operation_specification[2]])
    elif operation_specification[0] == 2:
        return (array_to_read_from[operation_specification[1]]
                * array_to_read_from[operation_specification[2]])

def run_program(full_array):
    starting_index = 0
    while True:
        next_operation_members = getNextOperationMembers(full_array, starting_index)
        execution_result = executeOperation(next_operation_members, full_array)
        if execution_result:
            full_array[next_operation_members[3]] = execution_result
            starting_index = 4 + next_operation_members[4]
        else:
            break
    return full_array

def run_part_one():
    puzzle_input = get_input()
    puzzle_input[1] = 12
    puzzle_input[2] = 2
    return run_program(puzzle_input)[0]

if __name__ == "__main__":
    part_one_result = run_part_one()
    print(part_one_result)