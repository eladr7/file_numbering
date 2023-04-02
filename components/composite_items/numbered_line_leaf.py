from components.composite_items.numbered_line_component import NumberedLineComponent


class NumberedLineLeaf(NumberedLineComponent):
    def __init__(self, line, number_str):
        self._line = line
        self._line_number_str = number_str

    def get_numbered_line(self):
        return self._line_number_str + " " + self._line
