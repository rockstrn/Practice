class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        b=1
        for i in [0,3,6]:
            for j in [0,3,6]:
                a=[]
                for m in range(3):
                    for n in range(3):
                        if board[m+i][n+j]!='.':
                            if board[m+i][n+j] in a:
                                b=0
                                break
                            else:
                                a.append(board[m+i][n+j])
                    if b==0:
                        break
                if b==0:
                    break
            if b==0:
                break
        if b==1:
            for i in range(9):
                a=[]
                c=[]
                for j in range(9):
                    if board[i][j]!='.':
                        if board[i][j] in a:
                            b=0
                            break
                        else:
                            a.append(board[i][j])
                for j in range(9):
                    if board[j][i]!='.':
                        if board[j][i] in c:
                            b=0
                            break
                        else:
                            c.append(board[j][i])
                    if b==0:
                        break
        return bool(b)
