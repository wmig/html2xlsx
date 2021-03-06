from .cell import Cell

class Row(object):
    def __init__(self, data=[], is_header=False, style=None):
        self._cells = data
        self._is_header = is_header
        self._style = style

    def add_cell(self, cell):
        assert isinstance(cell, Cell)
        self._cells.append(cell)

    def __iter__(self):
        for cell in self._cells:
            yield cell

    @property
    def cells(self):
        return self._cells

    @property
    def is_header(self):
        return self._is_header

    @property
    def height(self):
        return self._style['height']