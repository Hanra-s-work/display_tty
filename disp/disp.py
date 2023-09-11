
"""
The file in charge of managing the beautified output on the terminal
"""

import sys
import time


class Disp:
    """ The class in charge of Displaying messages """

    def __init__(self, toml_content: dict, save_to_file: bool = False, file_name: str = "text_output_run.txt", file_descriptor: any = None) -> None:
        self.toml_content = toml_content
        self.nb_chr = 40
        self.nb_side_walls = 2
        self.max_whitespace = self.nb_chr - self.nb_side_walls
        self.title_wall_chr = self.toml_content["TITLE_WALL_CHARACTER"]
        self.sub_title_wall_chr = self.toml_content["SUB_TITLE_WALL_CHARACTER"]
        self.sub_sub_title_wall_chr = self.toml_content["SUB_SUB_TITLE_WALL_CHARACTER"]
        self.message_char = self.toml_content["MESSAGE_CHARACTER"]
        self.message_error_char = self.toml_content["MESSAGE_ERROR_CHARACTER"]
        self.message_success_char = self.toml_content["MESSAGE_SUCCESS_CHARACTER"]
        self.message_inform_char = self.toml_content["MESSAGE_INFORM_CHARACTER"]
        self.message_warning_char = self.toml_content["MESSAGE_WARNING_CHARACTER"]
        if self.toml_content["PRETTY_OUTPUT_IN_BLOCS"] is True:
            self.message_animation_delay = self.toml_content["MESSAGE_ANIMATION_DELAY_BLOCKY"]
        else:
            self.message_animation_delay = self.toml_content["MESSAGE_ANIMATION_DELAY"]
        self.tree_node_char = self.toml_content["TREE_NODE_CHAR"]
        self.tree_node_end_char = self.toml_content["TREE_NODE_END_CHAR"]
        self.tree_line_seperator_char = self.toml_content["TREE_LINE_SEPERATOR_CHAR"]
        self.tree_column_seperator_char = self.toml_content["TREE_COLUMN_SEPERATOR_CHAR"]
        self.file_name = file_name
        self.save_to_file = save_to_file
        self.file_descriptor = file_descriptor
        self.open_file()

    def close_file(self) -> None:
        """ Close the log file if it was opened """
        if self.file_descriptor != None:
            self.file_descriptor.close()

    def open_file(self) -> None:
        """ Open the file if required and add the current date and time """
        if self.save_to_file == True and self.file_descriptor == None:
            self.file_descriptor = open(
                self.file_name,
                "a",
                encoding="utf-8",
                newline="\n"
            )
        if self.file_descriptor != None:
            self.append_run_date()

    def is_safe(self, content: any) -> bool:
        """ Check if an item is safe to write or not """
        if isinstance(content, (str, int, float, tuple, complex, bytes, bytearray, memoryview)) == False:
            return False
        return True

    def create_string(self, length, character) -> str:
        """ Create a string based of a character and a length """
        line = [character for i in range(0, length)]
        string = "".join(line)
        return string

    def display_animation(self, message: str = "Hello World!", delay: float = 0.02) -> None:
        """ Print the message letter by letter while applying a provided delay """
        if " " in message and self.toml_content["PRETTIFY_OUTPUT"] is True and self.toml_content["PRETTY_OUTPUT_IN_BLOCS"] is True:
            for letter in message.split(" "):
                sys.stdout.write(letter)
                sys.stdout.flush()
                sys.stdout.write(" ")
                time.sleep(delay)
        elif self.toml_content["PRETTIFY_OUTPUT"] is True:
            for letter in message:
                sys.stdout.write(letter)
                sys.stdout.flush()
                time.sleep(delay)
        else:
            sys.stdout.write(message)
        print()

    def animate_message(self, message: str = "Hello World!", delay: float = 0.02) -> None:
        """ Display or dump (to file) message """
        if self.is_safe(message) == False:
            message = f"{message}"
        if self.save_to_file == True and self.file_descriptor != None:
            self.file_descriptor.write(f"{message}\n")
        else:
            self.display_animation(message, delay)

    def disp_message_box(self, msg, char) -> None:
        """ Display a message in a box """
        white_spaces = self.create_string(
            int((self.max_whitespace - len(msg))/2),
            " "
        )
        box_wall = self.create_string(self.nb_chr, char)
        self.animate_message(f"{box_wall}")
        title_content = char
        title_content += white_spaces
        title_content += msg
        title_content += white_spaces
        title_content += char
        self.animate_message(f"{title_content}")
        self.animate_message(f"{box_wall}")

    def title(self, title) -> None:
        """ Print a beautified title """
        self.disp_message_box(title, self.title_wall_chr)

    def sub_title(self, sub_title) -> None:
        """ Print a beautified sub title """
        self.disp_message_box(sub_title, self.sub_title_wall_chr)

    def sub_sub_title(self, sub_sub_title) -> None:
        """ Print a beautified sub sub title """
        self.disp_message_box(sub_sub_title, self.sub_sub_title_wall_chr)

    def message(self, message) -> None:
        """ Print a beautified message """
        self.animate_message(
            f"{self.message_char}{self.message_char} {message} {self.message_char}{self.message_char}",
            self.message_animation_delay
        )

    def error_message(self, message: str) -> None:
        """ Print a beautified error message """
        self.animate_message(
            f"{self.message_error_char}{self.message_error_char} Error: {message} {self.message_error_char}{self.message_error_char}",
            self.message_animation_delay
        )

    def success_message(self, message: str) -> None:
        """ Print a beautified error message """
        self.animate_message(
            f"{self.message_success_char}{self.message_success_char} Success: {message} {self.message_success_char}{self.message_success_char}",
            self.message_animation_delay
        )

    def warning_message(self, message: str) -> None:
        """ Print a beautified warning message """
        self.animate_message(
            f"{self.message_warning_char}{self.message_warning_char} Warning: {message} {self.message_warning_char}{self.message_warning_char}",
            self.message_animation_delay
        )

    def inform_message(self, message: list) -> None:
        """ Print a beautified information message """
        if isinstance(message, list) is True:
            for msg in message:
                self.animate_message(
                    f"{self.message_inform_char}{self.message_inform_char} {msg} {self.message_inform_char}{self.message_inform_char}",
                    self.message_animation_delay
                )
        else:
            self.animate_message(
                f"{self.message_inform_char}{self.message_inform_char} {message} {self.message_inform_char}{self.message_inform_char}",
                self.message_animation_delay
            )

    def tree_node(self, line, offset: int, index: int, max_lenght: int) -> None:
        """ Display a line of the tree """
        processed_line = str()
        i = 0
        while i < offset:
            processed_line += f"{self.tree_column_seperator_char}   "
            i += 1
        if index == max_lenght:
            processed_line += f"{self.tree_node_end_char}{self.tree_line_seperator_char}{self.tree_line_seperator_char}{self.tree_line_seperator_char}"
        else:
            processed_line += f"{self.tree_node_char}{self.tree_line_seperator_char}{self.tree_line_seperator_char}{self.tree_line_seperator_char}"
        if self.is_safe(line) == False:
            line = f"{line}"
        processed_line += line
        self.animate_message(processed_line, self.message_animation_delay)

    def tree(self, title: str, data: list[str], offset: int = 0) -> None:
        """ Print a list under the form of a beautified tree """
        if (offset == 0):
            self.animate_message(f"{title}", self.message_animation_delay)
        length = len(data) - 1

        for line in enumerate(data):
            if isinstance(data, list) and isinstance(line[1], (list, dict)):
                self.tree_node(
                    "<list instance>",
                    offset,
                    line[0],
                    length
                )
                self.tree(line[0], line[1], offset + 1)
                continue
            if isinstance(data, dict) and isinstance(data[line[1]], (list, dict)):
                self.tree_node(
                    line[1],
                    offset,
                    line[0],
                    length
                )
                self.tree(line[0], data[line[1]], offset + 1)
                continue
            if isinstance(data, dict) and isinstance(data[line[1]], dict) is False:
                self.tree_node(
                    f"{line[1]}: {data[line[1]]}",
                    offset,
                    line[0],
                    length
                )
            else:
                self.tree_node(
                    line[1],
                    offset,
                    line[0],
                    length
                )

    def append_run_date(self) -> None:
        """ Add the date and time at which the program was launched """
        self.title(f"Run date: {time.strftime('%d/%m/%Y %H:%M:%S')}")


if __name__ == "__main__":
    TOML_CONF = {
        'SHOW_IMAGE_AFTER_RENDER': False,
        'PRETTIFY_OUTPUT': True,
        'PRETTY_OUTPUT_IN_BLOCS': True,
        'MESSAGE_CHARACTER': '@',
        'MESSAGE_ERROR_CHARACTER': '#',
        'MESSAGE_INFORM_CHARACTER': '!',
        'MESSAGE_QUESTION_CHARACTER': '?',
        'MESSAGE_SUCCESS_CHARACTER': '/',
        'MESSAGE_WARNING_CHARACTER': '?',
        'SUB_SUB_TITLE_WALL_CHARACTER': '*',
        'SUB_TITLE_WALL_CHARACTER': '@',
        'TITLE_WALL_CHARACTER': '#',
        'TREE_COLUMN_SEPERATOR_CHAR': '│',
        'TREE_LINE_SEPERATOR_CHAR': '─',
        'TREE_NODE_CHAR': '├',
        'TREE_NODE_END_CHAR': '└',
        'MESSAGE_ANIMATION_DELAY_BLOCKY': 0.01,
        'MESSAGE_ANIMATION_DELAY': 0.01
    }
    TEST_DATA = {
        "a": "l",
        "b": "o",
        "c": [
            "cl",
            "cp",
            "cq",
            "cl",
            "cm"
        ],
        "d": "e",
        "e": {
            "ea": "oo",
            "eb": "on",
            "ec": "ol",
            "ed": "om"
        },
        "f": [
            {
                "fa": "ef",
                "fb": "rf"
            },
            [
                "fc",
                "fd",
                "fe",
                "fg"
            ]
        ],
        "g": {
            "ga": {
                "gaa": "gae",
                "gab": "gar"
            },
            "gb": [
                "gba",
                "gbb",
                "gbc",
                "gbd",
                "gbe"
            ]
        }
    }
    DI = Disp(
        TOML_CONF,
        True,
        "test_run.tmp"
    )
    DI.animate_message("Test Message !", 0.01)
    DI.error_message("Test Error !")
    DI.inform_message("Test Inform !")
    DI.success_message("Test Success !")
    DI.warning_message("Test Warning !")
    DI.title("Test title")
    DI.sub_title("Test sub title")
    DI.sub_sub_title("Test sub sub title")
    DI.tree("Test data", TEST_DATA)
    DI.close_file()
