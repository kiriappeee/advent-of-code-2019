from . import computer
def get_input():
    input_for_day = open('python/inputday05.txt', 'r').read().split('\n')[0].split(',')
    return [int(x) for x in input_for_day]


def run_part_one():
    puzzle_input = get_input()
    print('Input for this part is 1')
    resulting_array, outputs = computer.run_program(puzzle_input)
    return outputs[-1]

def run_part_two():
    puzzle_input = get_input()
    print('Input for this part is 5')
    resulting_array, outputs = computer.run_program(puzzle_input)
    return outputs[-1]

if __name__ == "__main__":
    print("== DAY 5 PART 1 ==")
    print(run_part_one())
    print("== DAY 5 PART 2 ==")
    print(run_part_two())