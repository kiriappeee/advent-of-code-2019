def get_input():
    instruction_list_A, instruction_list_B = [instruction_line.split(',') for instruction_line in open('./python/inputday03.txt', 'r').read().split('\n')[:2]]
    return instruction_list_A, instruction_list_B

def get_points_from_current_position_to_next(instruction='R0', starting_coordinates=(0,0)):
    direction = instruction[0]
    distance = int(instruction[1:])
    points_travelled = []
    current_x = starting_coordinates[0]
    current_y = starting_coordinates[1]
    for i in range(distance):
        if direction == 'R':
            current_x += 1
        elif direction == 'U':
            current_y += 1
        elif direction == 'L':
            current_x -= 1
        elif direction == 'D':
            current_y -= 1
        points_travelled.append((current_x, current_y))
    return points_travelled

def get_points_for_given_instruction_set(instruction_list=['R0']):
    points_travelled = []
    current_coordinates = (0,0)
    for instruction in instruction_list:
        points_travelled.extend(get_points_from_current_position_to_next(instruction=instruction, starting_coordinates=current_coordinates))
        current_coordinates = points_travelled[-1]
    return points_travelled

def get_intersecting_points_for_given_instruction_set(instruction_list=['R0'], already_travelled_points=[]):
    current_coordinates = (0,0)
    intersecting_points = []
    already_travelled_points_as_set = set(already_travelled_points)
    for instruction in instruction_list:
        points_travelled = (get_points_from_current_position_to_next(instruction=instruction, starting_coordinates=current_coordinates))
        points_travelled_as_set = set(points_travelled)
        current_coordinates = points_travelled[-1]
        intersecting_points.extend(list(points_travelled_as_set & already_travelled_points_as_set))
    return intersecting_points

def get_intersection_points_for_wires(instruction_list_A, instruction_list_B):
    points_travelled_for_A = get_points_for_given_instruction_set(instruction_list=instruction_list_A)
    points_travelled_for_B = get_points_for_given_instruction_set(instruction_list=instruction_list_B)
    #return get_intersecting_points_for_given_instruction_set(instruction_list=instruction_list_B, already_travelled_points=points_travelled_for_A)
    return list(set(points_travelled_for_A) & set(points_travelled_for_B))

def find_smallest_manhattan_distance(instruction_list_A, instruction_list_B):
    intersection_points = get_intersection_points_for_wires(instruction_list_A, instruction_list_B)
    manhattan_distances = [abs(x[0]) + abs(x[1]) for x in intersection_points]
    return min(manhattan_distances)

def find_intersecting_points_with_least_cumulative_steps(instruction_list_A, instruction_list_B):
    points_travelled_for_A = get_points_for_given_instruction_set(instruction_list=instruction_list_A)
    points_travelled_for_B = get_points_for_given_instruction_set(instruction_list=instruction_list_B)
    intersecting_points = list(set(points_travelled_for_A) & set(points_travelled_for_B))
    steps_to_intersecting_points = []
    for intersecting_point in intersecting_points:
        # the +2 is to account for the first step. Indexes start at 0 instead of 1 which means that the number of steps will always be 
        # 2 less than the actual number of steps
        steps_to_intersecting_points.append(points_travelled_for_A.index(intersecting_point) + points_travelled_for_B.index(intersecting_point)+2)
    return min(steps_to_intersecting_points)

def run_part_one():
    instruction_list_A, instruction_list_B = get_input()
    return find_smallest_manhattan_distance(instruction_list_A, instruction_list_B)

def run_part_two():
    instruction_list_A, instruction_list_B = get_input()
    return find_intersecting_points_with_least_cumulative_steps(instruction_list_A, instruction_list_B)

if __name__ == "__main__":
    part_one_result = run_part_one()
    print(part_one_result)
    part_two_result = run_part_two()
    print(part_two_result)