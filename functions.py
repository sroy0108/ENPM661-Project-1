import numpy as np

# functions defined

# func: converting array to integer for easy comparison of nodes
def node_int(node_i):
    a_string = ''
    for integer in np.nditer(node_i):
        a_string += str(integer)
    return a_string


# func: to check solvability
def solvability(A):
    n = 9
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (A[i] > A[j]) and (A[i] != 0) and (A[j] != 0):
                count += 1
    if count % 2 != 0:
        print("The configuration is not solvable.")
        return None
    else:
        print("The configuration is solvable.")
        return A


# func: find the blank tile
def blank_tile(temp_A):
    # n = 9
    index = np.where(temp_A == 0)
    return index[0][0], index[1][0]


# func: move:right (swap blank tile with the right tile )
def move_right(temp_A, x, y):
    '''A: input configuration matrix,
       (x,y): position of blank title '''
    tempr = None
    if y == 2:
        flag = 0

    else:
        tempr = np.copy(temp_A)
        temp_r = tempr[x][y]
        tempr[x][y] = tempr[x][y + 1]
        tempr[x][y + 1] = temp_r
        flag = 1
    return flag, tempr


# func: move: left (swap blank tile with the left tile )
def move_left(temp_A, x, y):
    '''A: input configuration matrix,
       (x,y): position of blank title '''
    templ = None
    if y == 0:
        flag = 0
    else:
        templ = np.copy(temp_A)
        temp_l = templ[x][y]
        templ[x][y] = templ[x][y - 1]
        templ[x][y - 1] = temp_l
        flag = 1
    return flag, templ


#  func: move: up (swap blank tile with the up tile )
def move_up(temp_A, x, y):
    '''A: input configuration matrix,
       (x,y): position of blank title '''
    tempu = None
    if x == 0:
        flag = 0
    else:
        tempu = np.copy(temp_A)
        temp_u = tempu[x][y]
        tempu[x][y] = tempu[x - 1][y]
        tempu[x - 1][y] = temp_u
        flag = 1
    return flag, tempu


# func: move: down (swap blank tile with the down tile )
def move_down(temp_A, x, y):
    '''A: input configuration matrix,
       (x,y): position of blank title '''
    tempd = None
    if x == 2:
        flag = 0
    else:
        tempd = np.copy(temp_A)
        temp_d = tempd[x][y]
        tempd[x][y] = tempd[x + 1][y]
        tempd[x + 1][y] = temp_d
        flag = 1
    return flag, tempd


# defining node
class Node:
    def __init__(self, node_no, data, parent, initial_node, goal_node):
        self.data = data
        self.parent = parent
        # self.n_id = n_id
        self.node_no = node_no
        self.initial_node = initial_node
        self.goal_node = goal_node


# func: backtracking
def backtrace(goal, start_node, visited_nodes):
    last_node = visited_nodes[-1]
    p_current = [last_node.data]
    while not np.all(last_node.data == start_node):
        for node in visited_nodes:
            if np.all(last_node.parent == node.data):
                p_current.append(last_node.parent)
                last_node = node
                break
    p_rev = list(reversed(p_current))

    return p_rev


# func: writing text files
def textFiles(backtrace, nodes, visited):
    # tracking the node path

    f = open("nodePath.txt", "w+")
    for goal in backtrace:
        if goal is not None:
            f.write(str(goal) + "\n")
        else:
            f.write(str(goal) + "\n")
    f.close()

    # tracking the nodes visited

    f = open("Nodes.txt", "w+")
    for obj in visited:
        for i in np.nditer(obj.data):
            f.write(str(i) + " ")
        f.write("\n")
    f.close()

    # tracking the info of nodes

    f = open("NodesInfo.txt", "w+")
    for n_ele in nodes:
        f.write(str(n_ele.node_no) + "\t" + str(n_ele.node_no - 1) + "\n")
    f.close()


# func: puzzle solving
def solve_puzzle(input_config, goal):

    visited = []
    nodes_list = []
    states = [input_config.data]
    nodes_list.append(input_config)

    counter = 0

    while len(nodes_list) > 0:
        if not np.all(nodes_list[0].data == goal):
            Temp_A = nodes_list.pop(0)
            visited.append(Temp_A)

            # checking the right move
            X, Y = blank_tile(Temp_A.data)
            _, node_R = move_right(Temp_A.data, X, Y)
            if node_R is not None:
                counter += 1
                child_node = Node(counter, node_R, Temp_A.data, node_int(input_config.data), node_int(goal))
                node_visited = False
                for node in visited:
                    if np.all(node_R == node.data):
                        node_visited = True
                if not node_visited:
                    states.append(child_node.data)
                    nodes_list.append(child_node)
                    node_r_i = node_int(node_R)
                    if node_r_i == node_int(goal):
                        print("Goal reached")
                        print(goal)
                        return child_node, nodes_list, visited

            # checking the left move
            _, node_L = move_left(Temp_A.data, X, Y)
            if node_L is not None:
                counter += 1
                child_node = Node(counter, node_L, Temp_A.data, node_int(input_config.data), node_int(goal))
                node_visited = False
                for node in visited:
                    if np.all(node_L == node.data):
                        node_visited = True
                if not node_visited:
                    states.append(child_node.data)
                    nodes_list.append(child_node)
                    node_l_i = node_int(node_L)
                    if node_l_i == node_int(goal):
                        print("Goal reached")
                        print(goal)
                        return child_node, nodes_list, visited

            # checking the up move
            _, node_U = move_up(Temp_A.data, X, Y)
            if node_U is not None:
                counter += 1
                child_node = Node(counter, node_U, Temp_A.data, node_int(input_config.data), node_int(goal))
                node_visited = False
                for node in visited:
                    if np.all(node_U == node.data):
                        node_visited = True
                if not node_visited:
                    states.append(child_node.data)
                    nodes_list.append(child_node)
                    node_u_i = node_int(node_U)
                    if node_u_i == node_int(goal):
                        print("Goal reached")
                        print(goal)
                        return child_node, nodes_list, visited

            # checking the down move
            _, node_D = move_down(Temp_A.data, X, Y)
            if node_D is not None:
                counter += 1
                child_node = Node(counter, node_D, Temp_A.data, node_int(input_config.data), node_int(goal))
                node_visited = False
                for node in visited:
                    if np.all(node_D == node.data):
                        node_visited = True
                if not node_visited:
                    states.append(child_node.data)
                    nodes_list.append(child_node)
                    node_d_i = node_int(node_D)
                    if node_d_i == node_int(goal):
                        print("Goal reached")
                        print(goal)
                        return child_node, nodes_list, visited
