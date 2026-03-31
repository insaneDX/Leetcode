class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return [[0]]
        if numRows == 1:
            return [[1]]
        
        result = []

        for rows in range(0, numRows+1):
            window = []
            for cols in range(0, rows):
                if rows > 2:
                    if cols > 0 and cols<rows-1:
                        print(result)
                        print(rows, cols)
                        ans = result[rows-1][cols-1] + result[rows-1][cols]
                        window.append(ans)
                    else:
                        window.append(1)
                else:
                    window.append(1)
            result.append(window)
        
        return result[1:]
