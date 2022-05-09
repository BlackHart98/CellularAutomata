from unittest import result


class SimpleCellularAutomata:
    pass


"""
Rules
000 -> 0
001 -> 1
010 -> 0
011 -> 1
100 -> 1
101 -> 0
110 -> 1
111 -> 0
"""
def updateRule(grid_1D):
    new_grid_1D = [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    for i in range(len(grid_1D)):
        state = ""
        if i == 0:
            # print("head")
            state = grid_1D[len(grid_1D)-1] + grid_1D[i] +  grid_1D[i+1]
        elif i >= len(grid_1D)-1:
            # print("tail")
            state = grid_1D[i-1] + grid_1D[i] + grid_1D[0]
        else:
            # print("inbetween")
            state = grid_1D[i-1] + grid_1D[i] + grid_1D[i+1] 
        # print (f"{state} -> {policy[state]}")
        new_grid_1D[i] = policy[state]
    return new_grid_1D



if __name__ == '__main__':
    grid_1D = [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    policy = {"...":"#", "..#": ".", ".#.": "#", ".##" : ".", "#..": ".", "#.#" : "#", "##." : ".", "###" : "#"}
    
    number_of_epoch = 0
    print("START CELLULAR AUTOMATA: ")
    while number_of_epoch < 100:
        result = ""        
        for x in grid_1D:
            result += x
        print(result)
        grid_1D = updateRule(grid_1D)
        number_of_epoch += 1
