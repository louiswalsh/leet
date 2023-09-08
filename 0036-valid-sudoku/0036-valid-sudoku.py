class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9:[]}
        rows = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9:[]}
        boxes = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9:[]}

        for idxRow, row in enumerate(board):
            for idxVal, val in enumerate(row):
                if val != '.':
                    rows[idxRow].append(val)
                    cols[idxVal].append(val)
                    boxes[self.getBoxVal(idxRow, idxVal)].append(val)
        
        if not self.checkValuesSet(rows.values()) or not self.checkValuesSet(cols.values()) or not self.checkValuesSet(boxes.values()):
            return False

        return True
        
    def checkValuesSet(self, values):
        for val in values:
            valsSet = set(val)
            if len(val) != len(valsSet):
                return False
        return True


    def getBoxVal(self, rowIndex, columnIndex):
        if rowIndex <= 2:
            if columnIndex <= 2:
                return 0
            if 2 < columnIndex <= 5:
                return 1
            if 5 < columnIndex <= 8:
                return 2              
        if 2 < rowIndex <= 5:
            if columnIndex <= 2:
                return 3
            if 2 < columnIndex <= 5:
                return 4
            if 5 < columnIndex <= 8:
                return 5         
        if 5 < rowIndex <= 8:
            if columnIndex <= 2:
                return 6
            if 2 < columnIndex <= 5:
                return 7
            if 5 < columnIndex <= 8:
                return 8  