def get_input():
    puzzle_input = open('./python/inputday01.txt', 'r').read()
    return puzzle_input.split('\n')[:-1]

def get_fuel_required(module_mass=0):
    return (module_mass//3)-2

def get_fuel_required_for_fuel(fuel_volume=0):
    fuel_volume_required = (fuel_volume // 3)-2
    if fuel_volume_required <= 0:
        return 0
    else:
        return fuel_volume_required + get_fuel_required_for_fuel(fuel_volume=fuel_volume_required)

def run_part_one():
    puzzle_input = get_input()
    total_fuel_required = 0
    for module_mass in puzzle_input:
        total_fuel_required += get_fuel_required(module_mass=int(module_mass))
    return total_fuel_required

def run_part_two():
    # I could have simply modified the function for get_fuel_required
    # but I wanted to make sure the process of part one and part two remained
    # intact
    puzzle_input = get_input()
    total_fuel_required = 0
    for module_mass in puzzle_input:
        basic_fuel_for_module = get_fuel_required(module_mass=int(module_mass))
        total_fuel_required += get_fuel_required_for_fuel(fuel_volume = basic_fuel_for_module) + basic_fuel_for_module
    return total_fuel_required

if __name__ == "__main__":
    part_one_answer = run_part_one()
    print(part_one_answer)
    part_two_answer_new = run_part_two()
    print(part_two_answer_new)
