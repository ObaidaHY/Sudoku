#   Example board to work with
board = [   
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]



def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")
        
        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
            
            if j == 8:
                print(b[i][j])
            
            else:
                print(str(b[i][j]) + " ", end = "")
            



def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b)):
            if b[i][j] == 0:
                return (i,j)
    return None




def valid(b, num, pos):
    
    for j in range(len(b[0])):
        if b[pos[0]][j] == num and j != pos[1]:
            return False
    
    for i in range(len(b)):
        if b[i][pos[1]] == num and i != pos[0]:
            return False
    
    box_i = pos[0]//3
    box_j = pos[1]//3
    for x in range(3*box_i,3*(box_i + 1)):
        for y in range(3*box_j,3*(box_j + 1)):
            if pos != (x,y) and b[x][y] == num:
                return False
    
    return True




def solve(b):
    
    find = find_empty(b)
    if not find:
        return True
    
    i,j = find # coordinates
    for num in range(1,len(b)+1):
        if valid(b, num, (i,j)):
            b[i][j] = num   # it was equal to 0, because it's an empty square
            if solve(b):
                return True
            b[i][j] = 0
    return False

