import os
import configparser

from components.composite_items.numbered_line_composite import NumberedLineComposite
from components.composite_tree_builder import CompositeTreeBuilder


def write_lines_to_file(lines, filename):
    # Define a generator to yield each line from the list
    def line_generator():
        for line in lines:
            yield line

    with open(filename, "w") as f:
        # Use the generator to write each line to the file
        for line in line_generator():
            f.write(line)


def create_numbered_lines_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, "r") as f:
            lines = f.readlines()

        # Create the NumberedLineComposite object that contains the correct hirarchy of the lines
        # of the file with their corresponding numbering
        line_composite: NumberedLineComposite = (
            CompositeTreeBuilder().build_lines_composite_component(
                lines, [0], 1, "")
        )

        # 'lines' contains the numbered lines in the original order as in the file
        lines = line_composite.get_numbered_line()

        write_lines_to_file(lines, output_file_path)

    except IOError:
        print("Error: could not read file")


def get_file_paths_from_config():
    config = configparser.ConfigParser()
    config.read("config.ini")

    assets_folder = os.path.join(os.getcwd(), config["Files"]["assets"])
    input_file_path = os.path.join(assets_folder, config["Files"]["input"])
    output_file_path = os.path.join(assets_folder, config["Files"]["output"])
    return input_file_path, output_file_path


def main():
    input_file_path, output_file_path = get_file_paths_from_config()
    create_numbered_lines_file(input_file_path, output_file_path)


if __name__ == "__main__":
    main()
