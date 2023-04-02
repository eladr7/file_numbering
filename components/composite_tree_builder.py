from components.composite_items.numbered_line_composite import NumberedLineComposite
from components.composite_items.numbered_line_leaf import NumberedLineLeaf


# CompositeTreeBuilder's sole purpose is to get a list of string representing the lines of
# a file, and create a NumberedLineComposite object that contains the correct hirarchy of
# the lines of the file with their corresponding numbering, using the method
# build_lines_composite_component()
class CompositeTreeBuilder():
    def build_lines_composite_component(self, lines, line_index, current_line_number, parent_number):
        line_composite = NumberedLineComposite()

        if line_index[0] == len(lines):
            return line_composite

        # Add the current line into the current composite item
        line_number_str = self._get_line_number_str(
            current_line_number, parent_number)
        self._add_component_to_composite(
            lines, line_index, line_number_str, line_composite)

        indentation = self._get_indentation(lines[line_index[0]])
        counter_since_current_line = 1

        line_index[0] += 1
        while line_index[0] < len(lines):   
            new_indentation = self._get_indentation(lines[line_index[0]])
            if new_indentation == indentation:
                # Add the new line into the current composite item
                line_number_str = self._get_line_number_str(
                    current_line_number + counter_since_current_line, parent_number)
                self._add_component_to_composite(
                    lines, line_index, line_number_str, line_composite)

                counter_since_current_line += 1
                line_index[0] += 1
            elif new_indentation > indentation:
                # The new line should be a child of the current, thus get its tree and append it as
                # a child of line_composite

                line_composite_child = self.build_lines_composite_component(
                    lines, line_index, 1, line_number_str)
                line_composite.add_line_component(line_composite_child)
            else:
                return line_composite

        return line_composite

    def _get_indentation(self, line):
        return len(line) - len(line.lstrip())

    def _get_line_number_str(self, number_to_print, parent_number):
        return str(number_to_print) + '.' if parent_number == '' else str(parent_number) + str(number_to_print) + '.'

    def _is_leaf(self, lines, line_index):
        if line_index[0] == len(lines) - 1:
            return True

        line_indentation = self._get_indentation(lines[line_index[0]])
        next_line_indentation = self._get_indentation(lines[line_index[0] + 1])

        return next_line_indentation < line_indentation

    def _add_component_to_composite(self, lines, line_index, line_number_str, line_composite: NumberedLineComposite):
        # Check if leaf - if so then add a leaf without a NumberedLineComposite
        if self._is_leaf(lines, line_index):
            line_composite.add_line_component(
                NumberedLineLeaf(lines[line_index[0]], line_number_str))
        else:
            line_composite.add_line_component(NumberedLineComposite(
                NumberedLineLeaf(lines[line_index[0]], line_number_str)))
