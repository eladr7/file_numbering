from typing import List

from components.composite_items.numbered_line_component import NumberedLineComponent


class NumberedLineComposite(NumberedLineComponent):
    def __init__(self, component=None):
        self._numbered_lines: List[NumberedLineComponent] = []
        if component is not None:
            self._numbered_lines.append(component)

    def add_line_component(self, component):
        self._numbered_lines.append(component)

    def get_numbered_line(self):
        lines = []
        for child in self._numbered_lines:
            line = child.get_numbered_line()
            self._append_line_to_list(lines, line)
        return lines

    def _append_line_to_list(self, lines: List[str], line):
        if isinstance(line, list):
            lines += line
        else:
            lines.append(line)
