def check_sudoku(sudoku):
    n=len(sudoku[0])
    for i in range(n):
        for j in range(n):
            if(j+1 not in sudoku[i]):
                return False
    
    for i in range(n):
        list=[]
        for j in range(n):
            list.append(j+1)
        for k in range(n):
            if(sudoku[k][i] not in list):
                return False
            list.remove(sudoku[k][i])
    return True
sudoku=[[2,1,3],[1,3,1],[3,2,1]]
if(check_sudoku(sudoku)):
    print("yes")
else:
    print("no")