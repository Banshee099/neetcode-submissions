class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d = {}
        temp_list=[]
        for i in range(9):
            temp_list = [item for item in board[i][:8] if item!="."]
            if len(set(temp_list)) != len(temp_list):
                return False
        
        temp_list=[]
        for i in range(9):
            for j in range(9):
                if board[j][i]!=".":
                    temp_list.append(board[j][i])
            if len(set(temp_list)) != len(temp_list):
                return False
            temp_list = []
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                temp_list=[]
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        if board[x][y] != ".":
                            temp_list.append(board[x][y])
                if len(set(temp_list)) != len(temp_list):
                    return False
                temp_list=[]

        return True