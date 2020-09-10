#storing the graph in form of dictionary where the connected nodes are store in a list
graph = {'S': [['A', 1], ['B', 4]],
        'A': [['S', 1], ['B', 2], ['C', 5], ['G', 12]],
        'B': [['S', 4], ['A', 2],['C', 2]],
        'C': [['A', 5], ['B', 2],['G', 3]],
        'G': [['A', 12], ['C', 3]]
       }

heuristic = {'S': 7, 'A': 6, 'B': 2, 'C': 1, 'G': 0} #storing the heuristic cost in dictionary

cost = {'S': 0} # total cost for nodes visited


def AStarSearch(trace_node):
    global graph, heuristic
    closed = [] # storing the closed nodes in a list
    opened = [['S', 7]] # Storing opened nodes in a list and intiating it with root node/start node

   
    while True:
        fn = [i[1] for i in opened]     # f(n) = g(n) + h(n)
        chosen_index = fn.index(min(fn))
        node = opened[chosen_index][0]  # storing the current node 
        closed.append(opened[chosen_index])

        del opened[chosen_index] #once the node is visited removing it from opened list

        if closed[-1][0] == trace_node:        # if goal is found stop and the while loop stops
            break
        for item in graph[node]: # if the goal  node is not found traverse the graph
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue

            cost.update({item[0]: cost[node] + item[1]}) # update the node and its cost in  'cost' dictionary
            fn_node = cost[node] + heuristic[item[0]] + item[1]# calculate cost f(n)=g(n)+h(n) of current node
            temp = [item[0], fn_node]
            opened.append(temp) # store f(n) of current node in opened

    optimal_sequence = ['G'] # optimal node sequence
    for i in range(len(closed)-2, -1, -1):
        check_node = closed[i][0] # storing the current node in  check_node
        if trace_node in [children[0] for children in graph[check_node]]:
            children_costs = [temp[1] for temp in graph[check_node]]
            children_nodes = [temp[0] for temp in graph[check_node]]

            if cost[check_node] + children_costs[children_nodes.index(trace_node)] == cost[trace_node]:
                optimal_sequence.append(check_node)#append the current node to the optimal  sequence
                trace_node = check_node #change the trace_node to  current node
    optimal_sequence.reverse() # reversing the optimal sequence to get the path from start node to goal node


    return optimal_sequence


if __name__ == '__main__':
    trace_node=input("Enter Goal :")
    trace_node=trace_node.upper()
    optimal_nodes = AStarSearch(trace_node)
    print('Optimal nodes path:  ', str(optimal_nodes))
