import numpy as np
import functions

# user input
user_ip_list = [int(x) for x in input("Enter your configuration separated by space: ").split()]
A = np.array(user_ip_list)
input_config = A.reshape((3, 3))
input_int = functions.node_int(input_config)
print(input_config)


# final configuration to reach
goal = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0]).reshape((3, 3))

# to compare with goal node
goal_list = [1, 2, 3, 4, 5, 6, 7, 8, 0]
goal_int = functions.node_int(goal)

# checking solvability
state = functions.solvability(A)
if state is not None:
    # checking node info
    Class_data = functions.Node(0, input_config, None, input_int, goal_int)
    # checking all possible nodes
    _, nodes, visited = functions.solve_puzzle(Class_data, goal)
    if visited is None:
        print("Invalid input")
    else:
        visited.append(functions.Node(-1, goal, visited[-1].data, input_int, goal_int))
        functions.textFiles(functions.backtrace(goal, input_config, visited), nodes, visited)
