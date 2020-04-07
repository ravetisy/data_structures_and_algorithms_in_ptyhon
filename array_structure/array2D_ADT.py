from array_ADT import Array

class Array2D:

    def __init__(self, numRows, numCols):
        self._theRows = Array(numRows)

        for i in range (numRows):
            self._theRows[i] = Array(numCols) # for each row create its on dimentsional array.

    def numRows(self):
        return len(self._theRows)

    def numCols(self):
        return len(self._theRows[0])

    def clear(self, value):
        for row in range(self.numRows()):
            row.clear(value)

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "must be 2D array valid x,y"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row <self.numRows() and col >=0 and col <= self.numCols(), "Out of 2DArray range"
        the1dArray = self._theRows[row]
        return the1dArray[col]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "must be 2D array valid x,y"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() and col >= 0 and col <= self.numCols(), "Out of 2DArray range"
        the1dArray = self._theRows[row]
        the1dArray[col] = value
