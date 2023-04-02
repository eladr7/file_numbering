import configparser
import os
from unittest import TestCase

from run import create_numbered_lines_file


class TestCorrectOutputResults(TestCase):
    def test_output_file_against_input(self):
        # Get path to ~/<path_to_repo_folder>
        base_path = os.path.dirname(os.path.abspath("run.py"))

        config = configparser.ConfigParser()
        config.read("config.ini")
        assets_folder = os.path.join(base_path, config["Files"]["assets"])

        input_file_path = os.path.join(assets_folder, config["Files"]["input_test"])
        output_file_path = os.path.join(assets_folder, config["Files"]["output"])
        create_numbered_lines_file(input_file_path, output_file_path)

        # Check that the generated output file matches the expected output file
        with open(output_file_path, "r") as f1, open(
            os.path.join(assets_folder, config["Files"]["output_test_expected"]), "r"
        ) as f2:
            output_contents = f1.read()
            expected_output_contents = f2.read()
            self.assertEqual(output_contents, expected_output_contents)
