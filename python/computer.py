def is_instruction(number_to_check):
    possible_opcodes = ['1', '2', '3', '4', '5', '6', '7', '8', '99']
    valid_paramter_mode_digits = set('10')
    possible_two_digit_opcodes = ['0' + po if len(po) < 2 else po for po in possible_opcodes]
    str_version = str(number_to_check)
    if len(str_version) <= 2 and str_version in possible_opcodes:
        return True
    elif len(str_version)< 6 and str_version[-2:] in possible_two_digit_opcodes and all(character in valid_paramter_mode_digits for character in str_version[:-2]):
        return True
    else:
        return False

def getNextOperationMembers(array_to_extract_next_operation_from, starting_index=0):
    if not is_instruction(array_to_extract_next_operation_from[starting_index]):
        return getNextOperationMembers(array_to_extract_next_operation_from, starting_index+1)
    next_instruction = '0' * (5 - len(str(array_to_extract_next_operation_from[starting_index]))) + str(array_to_extract_next_operation_from[starting_index])
    next_operation_to_return = {
        'opcode': int(next_instruction[-2:]),
        'index_of_opcode': starting_index
    }
    next_operation_to_return['parameter_modes'] = [int(c) for c in next_instruction[0:-2]]
    if next_operation_to_return['opcode'] == 99:
        next_operation_to_return['parameters'] = []
    elif next_operation_to_return['opcode'] in [1, 2, 7, 8]:
        next_operation_to_return['parameters'] = array_to_extract_next_operation_from[starting_index+1:starting_index+4]
    elif next_operation_to_return['opcode'] in [3, 4]:
        next_operation_to_return['parameters'] = [array_to_extract_next_operation_from[starting_index+1]]
    elif next_operation_to_return['opcode'] in [5, 6]:
        next_operation_to_return['parameters'] = array_to_extract_next_operation_from[starting_index+1:starting_index+3]
        
    return next_operation_to_return
def executeOperation(operation_specification, array_to_read_from):
    # print(operation_specification)
    parameters = operation_specification['parameters']
    parameter_modes = operation_specification['parameter_modes']
    values = []
    for i in range(len(parameters)):
        values.append(array_to_read_from[parameters[i]] if parameter_modes[2-i] == 0 else parameters[i])
    # print(values)
    if operation_specification['opcode'] == 1:
        return (values[0]
                + values[1])
    elif operation_specification['opcode'] == 2:
        return (values[0]
                * values[1])
    elif operation_specification['opcode'] == 3:
        return int(input('Please enter the number to store: '))
    elif operation_specification['opcode'] == 4:
        return values[0]
    elif operation_specification['opcode'] == 5:
        if values[0] != 0:
            return values[1]
        else:
            return -1
    elif operation_specification['opcode'] == 6:
        if values[0] == 0:
            return values[1]
        else:
            return -1
    elif operation_specification['opcode'] == 7:
        if values[0] < values[1]:
            return 1
        else:
            return 0
    elif operation_specification['opcode'] == 8:
        if values[0] == values[1]:
            return 1
        else:
            return 0

def run_program(full_array):
    instruction_pointer = 0
    outputs = []
    while True:
        next_operation_members = getNextOperationMembers(full_array, instruction_pointer)
        execution_result = executeOperation(next_operation_members, full_array)
        if execution_result is not None:
            if next_operation_members['opcode'] == 4:
                outputs.append(execution_result)
            if next_operation_members['opcode'] not in [5,6]:
                full_array[next_operation_members['parameters'][-1]] = execution_result
                instruction_pointer = len(next_operation_members['parameters']) + 1 + next_operation_members['index_of_opcode']
            else:
                if execution_result == -1:
                    instruction_pointer = len(next_operation_members['parameters']) + 1 + next_operation_members['index_of_opcode']
                else:
                    instruction_pointer = execution_result
        else:
            break
    return full_array, outputs