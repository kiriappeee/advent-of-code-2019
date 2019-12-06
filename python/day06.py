def get_input():
    input_for_day = [l.strip() for l in open('python/inputday06.txt', 'r').readlines()  if l.strip() != '' ]
    return input_for_day

def generate_orbit_map(orbit_input_array):
    orbit_map = {
        'COM': {'orbits': [], 'orbitted_by': []}
    }
    for orbital_relationship in orbit_input_array:
        object_being_orbitted, object_doing_orbitting = orbital_relationship.split(')')
        if object_being_orbitted not in orbit_map:
            orbit_map[object_being_orbitted] = {'orbits': [], 'orbitted_by': []}
        if object_doing_orbitting not in orbit_map:
            orbit_map[object_doing_orbitting] = {'orbits': [], 'orbitted_by': []}
        orbit_map[object_being_orbitted]['orbitted_by'].append(object_doing_orbitting)
        orbit_map[object_doing_orbitting]['orbits'].append(object_being_orbitted)
    return orbit_map

def get_number_of_orbits_for_given_object(object_to_check, orbit_map):
    orbits = orbit_map[object_to_check]['orbits']
    direct_orbits = len(orbits)
    indirect_orbits = 0
    for orbit in orbits:
        indirect_orbits += get_number_of_orbits_for_given_object(orbit, orbit_map)
    return direct_orbits + indirect_orbits

def get_total_number_of_orbits(orbit_map):
    total_number_of_orbits = 0
    for orbit in orbit_map:
        total_number_of_orbits += get_number_of_orbits_for_given_object(orbit, orbit_map)
    return total_number_of_orbits
def run_part_one():
    puzzle_input = get_input()
    orbit_map = generate_orbit_map(puzzle_input)
    return get_total_number_of_orbits(orbit_map)

def run_part_two():
    puzzle_input = get_input()
    return

if __name__ == "__main__":
    print("== DAY 6 PART 1 ==")
    print(run_part_one())
    print("== DAY 6 PART 2 ==")
    print(run_part_two())