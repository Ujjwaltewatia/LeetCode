class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        DIRECTIONS=[(0,-1),(0,1),(-1,0),(1,0)]
        EMPTY=2147483647
        ROWS=len(rooms)
        COLUMNS=len(rooms[0])
        queue=[]
        for i in range(ROWS):
            for j in range(COLUMNS):
                if rooms[i][j]==0:
                    queue.append([i,j])
        
        while queue:
            point=queue.pop(0)
            row=point[0]
            column=point[1]
            
            for i,j in DIRECTIONS:
                r=row+i
                c=column+j
                
                if r<0 or r>ROWS-1 or c<0 or c>COLUMNS-1 or rooms[r][c]!=EMPTY:
                    continue
                rooms[r][c]=rooms[row][column]+1
                queue.append([r,c])
