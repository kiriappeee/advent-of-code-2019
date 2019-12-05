from . import computer

def get_input():
    input_for_day = open('python/inputday02.txt', 'r').read().split('\n')[0].split(',')
    return [int(x) for x in input_for_day]

def run_part_one():
    puzzle_input = get_input()
    puzzle_input[1] = 12
    puzzle_input[2] = 2
    return computer.run_program(puzzle_input)[0][0]

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
        program_result = computer.run_program(puzzle_input)[0][0]
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