def get_input():
    input_for_day = open('python/inputday02.txt', 'r').read().split('\n')[0].split(',')
    return [int(x) for x in input_for_day]

def getNextOperationMembers(array_to_extract_next_operation_from, starting_index=0):
    if array_to_extract_next_operation_from[starting_index] == 99:
        return {
            'opcode': 99,
            'parameters': [],
            'index_of_opcode': starting_index
        }
    elif array_to_extract_next_operation_from[starting_index] == 1 or array_to_extract_next_operation_from[starting_index] == 2:
        return {
            'opcode': array_to_extract_next_operation_from[starting_index],
            'parameters': array_to_extract_next_operation_from[starting_index+1:starting_index+4],
            'index_of_opcode': starting_index
        }
    else:
        return getNextOperationMembers(array_to_extract_next_operation_from, starting_index+1)

def executeOperation(operation_specification, array_to_read_from):
    parameters = operation_specification['parameters']
    if operation_specification['opcode'] == 1:
        return (array_to_read_from[parameters[0]]
                + array_to_read_from[parameters[1]])
    elif operation_specification['opcode'] == 2:
        return (array_to_read_from[parameters[0]]
                * array_to_read_from[parameters[1]])

def run_program(full_array):
    instruction_pointer = 0
    while True:
        next_operation_members = getNextOperationMembers(full_array, instruction_pointer)
        execution_result = executeOperation(next_operation_members, full_array)
        if execution_result:
            full_array[next_operation_members['parameters'][-1]] = execution_result
            instruction_pointer = len(next_operation_members['parameters']) + 1 + next_operation_members['index_of_opcode']
        else:
            break
    return full_array

def run_part_one():
    puzzle_input = get_input()
    puzzle_input[1] = 12
    puzzle_input[2] = 2
    return run_program(puzzle_input)[0]

def run_part_two():
    noun = 0
    verb = 0
    while True:
        puzzle_input = get_input()
        if verb == 100:
            noun += 1
            verb = 0
        if noun == 100:
            break
        puzzle_input[1] = noun
        puzzle_input[2] = verb
        program_result = run_program(puzzle_input)[0]
        if program_result == 19690720:
            break
        else:
            verb += 1
    return 100 * noun + verb

if __name__ == "__main__":
    part_one_result = run_part_one()
    print(part_one_result)
    part_two_result = run_part_two()
    print(part_two_result)