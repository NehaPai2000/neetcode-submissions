class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hm={}
        boxes={}
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                box = (i//3,j//3)
                if box in boxes:
                    if board[i][j] in boxes[box]:
                        return False
                
                else:
                    boxes[box]=set()
                boxes[box].add(board[i][j])
                if board[i][j] in hm:
                    return False
                else:
                    hm[board[i][j]]=1
            hm={}
        hm={}
        for i in range(9):
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in hm:
                    return False
                else:
                    hm[board[j][i]]=1
            hm={}
        return True
