
"""
The file in charge of managing the beautified output on the terminal
"""

import sys
import time
import logging
import colorlog
from typing import List, Dict

OUT_TTY = "tty"
OUT_STRING = "string"
OUT_FILE = "file"
OUT_DEFAULT = ''

# OUTPUT modes
KEY_OUTPUT_MODE = "OUTPUT_MODE"
KEY_PRETTIFY_OUTPUT = "PRETTIFY_OUTPUT"
KEY_PRETTIFY_OUTPUT_IN_BLOCKS = "PRETTY_OUTPUT_IN_BLOCS"

# Animation delays
KEY_ANIMATION_DELAY = 'MESSAGE_ANIMATION_DELAY'
KEY_ANIMATION_DELAY_BLOCKY = 'MESSAGE_ANIMATION_DELAY_BLOCKY'

TOML_CONF = {
    KEY_OUTPUT_MODE: OUT_TTY,
    KEY_PRETTIFY_OUTPUT: True,
    KEY_PRETTIFY_OUTPUT_IN_BLOCKS: True,
    KEY_ANIMATION_DELAY: 0.01,
    KEY_ANIMATION_DELAY_BLOCKY: 0.01,
    'MESSAGE_CHARACTER': '@',
    'MESSAGE_ERROR_CHARACTER': '#',
    'MESSAGE_INFORM_CHARACTER': 'i',
    'MESSAGE_QUESTION_CHARACTER': '?',
    'MESSAGE_SUCCESS_CHARACTER': '/',
    'MESSAGE_WARNING_CHARACTER': '!',
    'SUB_SUB_TITLE_WALL_CHARACTER': '*',
    'SUB_TITLE_WALL_CHARACTER': '@',
    'TITLE_WALL_CHARACTER': '#',
    'TREE_COLUMN_SEPERATOR_CHAR': '│',
    'TREE_LINE_SEPERATOR_CHAR': '─',
    'TREE_NODE_CHAR': '├',
    'TREE_NODE_END_CHAR': '└',
    'BOX_NO_VERTICAL': '#',
    'BOX_VERTICAL_NO_HORIZONTAL': '#',
    'ROUND_BOX_CORNER_LEFT': '╔',
    'ROUND_BOX_CORNER_RIGHT': '╗',
    'ROUND_BOX_CORNER_BOTTOM_LEFT': '╚',
    'ROUND_BOX_CORNER_BOTTOM_RIGHT': '╝',
    'ROUND_BOX_HORIZONTAL': '═',
    'ROUND_BOX_VERTICAL': '║',
    'DIFF_BORDER_LINE_CHARACTER_BOX': '-',
    'DIFF_SIDE_LINE_CHARACTER_BOX': '|',
}


class Disp:
    """ The class in charge of Displaying messages """

    def __init__(self, toml_content: Dict[str, any], save_to_file: bool = False, file_name: str = "text_output_run.txt", file_descriptor: any = None, debug: bool = False, logger: logging = None) -> None:
        self.__version__ = "1.0.0"
        self.toml_content = toml_content
        self.author = "(c) Created by Henry Letellier"
        self.nb_chr = 40
        self.debug = debug
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
        self.message_question_char = self.toml_content["MESSAGE_QUESTION_CHARACTER"]
        if self.toml_content[KEY_PRETTIFY_OUTPUT_IN_BLOCKS] is True:
            self.message_animation_delay = self.toml_content[KEY_ANIMATION_DELAY_BLOCKY]
        else:
            self.message_animation_delay = self.toml_content[KEY_ANIMATION_DELAY]
        self.tree_node_char = self.toml_content["TREE_NODE_CHAR"]
        self.tree_node_end_char = self.toml_content["TREE_NODE_END_CHAR"]
        self.tree_line_seperator_char = self.toml_content["TREE_LINE_SEPERATOR_CHAR"]
        self.tree_column_seperator_char = self.toml_content["TREE_COLUMN_SEPERATOR_CHAR"]
        self.file_name = file_name
        self.save_to_file = save_to_file
        if self.toml_content[KEY_OUTPUT_MODE] == OUT_FILE:
            self.save_to_file = True
        self.file_descriptor = file_descriptor
        self.generated_content = ""
        if self.toml_content[KEY_OUTPUT_MODE] not in (OUT_FILE, OUT_STRING, OUT_TTY, OUT_DEFAULT):
            raise ValueError(
                f"Invalid output mode. Must be one of '{OUT_FILE}', '{OUT_STRING}', '{OUT_TTY}', '{OUT_DEFAULT}"
            )
        if self.toml_content[KEY_OUTPUT_MODE] == OUT_FILE:
            self._open_file()
        # ---- Logging data ----
        if callable(logger) and hasattr(logger, "debug"):
            self.logger = logger
        else:
            self.logger = logging.getLogger(self.__class__.__name__)
            if not self.logger.hasHandlers():
                handler = colorlog.StreamHandler()
                formatter = colorlog.ColoredFormatter(
                    '[%(asctime)s] %(log_color)s%(levelname)s%(reset)s %(name)s: \'%(message)s\'',
                    datefmt=None,
                    reset=True,
                    log_colors={
                        'DEBUG':    'cyan',
                        'INFO':     'green',
                        'WARNING':  'yellow',
                        'ERROR':    'red',
                        'CRITICAL': 'bold_red',
                    }
                )
                handler.setFormatter(formatter)
                self.logger.addHandler(handler)
            self.logger.setLevel(logger.DEBUG)

    def _disp_print_debug(self, string: str = "") -> None:
        """ Print a debug message """
        if self.debug is True:
            self.logger.debug("(Disp) %s", string)

    def close_file(self) -> None:
        """ Close the log file if it was opened """
        if self.toml_content[KEY_OUTPUT_MODE] != OUT_FILE:
            return
        if self.file_descriptor is not None:
            self.file_descriptor.close()

    def get_generated_content(self) -> str:
        """ Return the generated string """
        data = self.generated_content
        self.generated_content = ""
        return data

    def _calculate_required_spaces(self, string_length: int) -> str:
        """_summary_
            This is a function that will generate the required amount of spaces for the padding of the shape.
        Args:
            string_length (int): _description_: The length of the provided string

        Returns:
            str: _description_: The number of spaces required for the padding
        """
        if string_length >= self.max_whitespace:
            white_spaces = " "
        else:
            calculated_length = int(
                (self.max_whitespace - string_length)/2
            )
            if calculated_length % 2 == 1 and calculated_length != 0:
                calculated_length += 1
            white_spaces = self.create_string(
                calculated_length,
                " "
            )
        return white_spaces

    def _open_file(self) -> None:
        """ Open the file if required and add the current date and time """
        if self.save_to_file is True and self.file_descriptor is None:
            self.file_descriptor = open(
                self.file_name,
                "a",
                encoding="utf-8",
                newline="\n"
            )
        if self.file_descriptor is not None:
            self.append_run_date()

    def _is_safe(self, content: any) -> bool:
        """ Check if an item is safe to write or not """
        if isinstance(content, (str, int, float, tuple, complex, bytes, bytearray, memoryview)) is False:
            return False
        return True

    def create_string(self, length, character) -> str:
        """ Create a string based of a character and a length """
        line = [character for i in range(0, length)]
        string = "".join(line)
        return string

    def display_animation(self, message: str = "Hello World!", delay: float = 0.02) -> None:
        """ Print the message letter by letter while applying a provided delay """
        if " " in message and self.toml_content[KEY_PRETTIFY_OUTPUT] is True and self.toml_content[KEY_PRETTIFY_OUTPUT_IN_BLOCKS] is True:
            for letter in message.split(" "):
                sys.stdout.write(letter)
                sys.stdout.flush()
                sys.stdout.write(" ")
                time.sleep(delay)
        elif self.toml_content[KEY_PRETTIFY_OUTPUT] is True:
            for letter in message:
                sys.stdout.write(letter)
                sys.stdout.flush()
                time.sleep(delay)
        else:
            sys.stdout.write(message)
        print()

    def animate_message(self, message: str = "Hello World!", delay: float = 0.02) -> None:
        """ Display or dump (to file) message """
        if self._is_safe(message) is False:
            message = f"{message}"
        if self.save_to_file is True and self.file_descriptor is not None:
            self.file_descriptor.write(f"{message}\n")
        elif self.toml_content[KEY_OUTPUT_MODE] == OUT_STRING:
            self.generated_content = f"{message}\n"
        else:
            self.display_animation(message, delay)

    def disp_message_box(self, msg: str, char: str = "#") -> None:
        """
        Display a message in a box \n
        The text is displayed in the center of the box, it is just difficult to show that in a function comment\n
        This is a sample box (characters and dimensions depend on the provided configuration):\n
        #############################\n
        \#        Sample text        #\n
        #############################
        """

        box_wall = self.create_string(self.nb_chr, char)

        title_content = ""
        if "\n" in msg:
            lines = msg.split("\n")
            for i in lines:
                string_length = len(i)
                white_spaces = self._calculate_required_spaces(string_length)
                title_content += char
                title_content += white_spaces
                title_content += i
                if string_length % 2 == 1 and string_length != 0:
                    white_spaces = white_spaces[:-1]
                title_content += white_spaces
                title_content += char
                title_content += '\n'
        else:
            string_length = len(msg)
            white_spaces = self._calculate_required_spaces(string_length)
            box_wall = self.create_string(self.nb_chr, char)
            title_content += char
            title_content += white_spaces
            title_content += msg
            if string_length % 2 == 1 and string_length != 0:
                white_spaces = white_spaces[:-1]
            title_content += white_spaces
            title_content += char
            title_content += "\n"

        generated_content = f"{box_wall}\n"
        generated_content += f"{title_content}"
        generated_content += f"{box_wall}"
        self.animate_message(
            f"{generated_content}",
            self.message_animation_delay
        )

    def disp_round_message_box(self, msg: str = "Sample text") -> None:
        """
        Display a message in a box \n
        The text is displayed in the center of the box, it is just difficult to show that in a function comment\n
        This is a sample box (characters and dimensions depend on the provided configuration):\n
        ╔══════════════════════╗\n
        ║      Sample Text     ║\n
        ╚══════════════════════╝
        """

        offset_reset = 2

        # Generate the top line
        top_wall = ""
        if 'ROUND_BOX_CORNER_LEFT' in self.toml_content:
            top_wall += self.toml_content['ROUND_BOX_CORNER_LEFT']
        else:
            top_wall += "╔"
        if 'ROUND_BOX_HORIZONTAL' in self.toml_content:
            top_wall += self.create_string(
                self.nb_chr - offset_reset,
                self.toml_content['ROUND_BOX_HORIZONTAL']
            )
        else:
            top_wall += self.create_string(
                self.nb_chr-offset_reset,
                "═"
            )
        if 'ROUND_BOX_CORNER_RIGHT' in self.toml_content:
            top_wall += self.toml_content['ROUND_BOX_CORNER_RIGHT']
        else:
            top_wall += "╗"

        # Generate the bottom line
        bottom_wall = ""
        if 'ROUND_BOX_CORNER_BOTTOM_LEFT' in self.toml_content:
            bottom_wall += self.toml_content['ROUND_BOX_CORNER_BOTTOM_LEFT']
        else:
            bottom_wall += "╚"

        if 'ROUND_BOX_HORIZONTAL' in self.toml_content:
            bottom_wall += self.create_string(
                self.nb_chr-offset_reset,
                self.toml_content['ROUND_BOX_HORIZONTAL']
            )
        else:
            bottom_wall += self.create_string(
                self.nb_chr-offset_reset,
                "═"
            )
        if 'ROUND_BOX_CORNER_BOTTOM_RIGHT' in self.toml_content:
            bottom_wall += self.toml_content['ROUND_BOX_CORNER_BOTTOM_RIGHT']
        else:
            bottom_wall += "╝"

        border_character = ""
        if 'ROUND_BOX_VERTICAL' in self.toml_content:
            border_character = self.toml_content['ROUND_BOX_VERTICAL']
        else:
            border_character = "║"

        center_content = ""
        if "\n" in msg:
            lines = msg.split("\n")
            for i in lines:
                string_length = len(i)
                white_spaces = self._calculate_required_spaces(string_length)
                center_content += border_character
                center_content += white_spaces
                center_content += i
                if string_length % 2 == 1 and string_length != 0:
                    white_spaces = white_spaces[:-1]
                center_content += white_spaces
                center_content += border_character
                center_content += '\n'
        else:
            string_length = len(msg)
            white_spaces = self._calculate_required_spaces(string_length)
            center_content += border_character
            center_content += white_spaces
            center_content += msg
            if string_length % 2 == 1 and string_length != 0:
                white_spaces = white_spaces[:-1]
            center_content += white_spaces
            center_content += border_character
            center_content += "\n"

        generated_content = f"{top_wall}\n"
        generated_content += f"{center_content}"
        generated_content += f"{bottom_wall}"
        self.animate_message(
            f"{generated_content}",
            self.message_animation_delay
        )

    def disp_diff_side_and_top_message_box(self, msg: str) -> None:
        """
        Display a message in a box \n
        The text is displayed in the center of the box, it is just difficult to show that in a function comment\n
        This is a sample box (characters and dimensions depend on the provided configuration):\n
        _____________________________\n
        |        Sample text        |\n
        _____________________________
        """

        ceiling_boxes = ""
        if 'DIFF_BORDER_LINE_CHARACTER_BOX' in self.toml_content:
            ceiling_boxes = self.toml_content['DIFF_BORDER_LINE_CHARACTER_BOX']
        else:
            ceiling_boxes = "-"

        border_character = ""
        if 'DIFF_SIDE_LINE_CHARACTER_BOX' in self.toml_content:
            border_character = self.toml_content['DIFF_SIDE_LINE_CHARACTER_BOX']
        else:
            border_character = "|"

        box_wall = self.create_string(self.nb_chr, ceiling_boxes)

        title_content = ""
        if "\n" in msg:
            lines = msg.split("\n")
            for i in lines:
                string_length = len(i)
                white_spaces = self._calculate_required_spaces(string_length)
                title_content += border_character
                title_content += white_spaces
                title_content += i
                if string_length % 2 == 1 and string_length != 0:
                    white_spaces = white_spaces[:-1]
                title_content += white_spaces
                title_content += border_character
                title_content += '\n'
        else:
            string_length = len(msg)
            white_spaces = self._calculate_required_spaces(string_length)
            title_content += border_character
            title_content += white_spaces
            title_content += msg
            if string_length % 2 == 1 and string_length != 0:
                white_spaces = white_spaces[:-1]
            title_content += white_spaces
            title_content += border_character
            title_content += "\n"

        generated_content = f"{box_wall}\n"
        generated_content += f"{title_content}"
        generated_content += f"{box_wall}"
        self.animate_message(
            f"{generated_content}",
            self.message_animation_delay
        )

    def disp_box_no_vertical(self, message: str, character: str = "@") -> None:
        """
        Print another box format, this time without the internal bars\n
        The text is displayed in the center of the box, it is just difficult to show that in a function comment\n
        Here is a sample box:\n
        #############################\n
                Sample text\n
        #############################
        """

        if 'BOX_NO_VERTICAL' in self.toml_content:
            char = self.toml_content['BOX_NO_VERTICAL']
        else:
            char = character

        box_wall = self.create_string(self.nb_chr, char)

        title_content = ""
        if "\n" in message:
            lines = message.split("\n")
            for i in lines:
                string_length = len(i)
                white_spaces = self._calculate_required_spaces(string_length)
                title_content += white_spaces
                title_content += i
                if string_length % 2 == 1 and string_length != 0:
                    white_spaces = white_spaces[:-1]
                title_content += white_spaces
                title_content += '\n'
        else:
            string_length = len(message)
            white_spaces = self._calculate_required_spaces(string_length)
            title_content += white_spaces
            title_content += message
            if string_length % 2 == 1 and string_length != 0:
                white_spaces = white_spaces[:-1]
            title_content += white_spaces
            title_content += "\n"

        generated_content = f"{box_wall}\n"
        generated_content += f"{title_content}"
        generated_content += f"{box_wall}"
        self.animate_message(
            f"{generated_content}",
            self.message_animation_delay
        )

    def disp_vertical_message_box(self, msg: str, character: str = '') -> None:
        """
        Display a message in a box \n
        The text is displayed in the center of the box, it is just difficult to show that in a function comment\n
        The '#' characters a aligned to the first and last '#' character on each line\n
        But due to the code editor's rendering, it removes spaces, thus, if you want an accurate view, look at the raw comment of the function\n
        This is a sample box (characters and dimensions depend on the provided configuration):\n
        \###############\n
        \#             #\n
        \#             #\n
        \#             #\n
        \# Sample text #\n
        \#             #\n
        \#             #\n
        \#             #\n
        \###############
        """

        if 'BOX_NO_VERTICAL' in self.toml_content:
            character = self.toml_content['BOX_NO_VERTICAL']
        elif character == '':
            character = "#"

        box_wall = self.create_string(self.nb_chr, character)

        title_content = ""
        if "\n" in msg:
            lines = msg.split("\n")
            for i in lines:
                string_length = len(i)
                white_spaces = self._calculate_required_spaces(string_length)
                title_content += character
                title_content += white_spaces
                title_content += i
                if string_length % 2 == 1 and string_length != 0:
                    white_spaces = white_spaces[:-1]
                title_content += white_spaces
                title_content += character
                title_content += "\n"
            msg = lines
        else:
            string_length = len(msg)
            white_spaces = self._calculate_required_spaces(string_length)
            title_content += character
            title_content += white_spaces
            title_content += msg
            if string_length % 2 == 1 and string_length != 0:
                white_spaces = white_spaces[:-1]
            title_content += white_spaces
            title_content += character
            title_content += "\n"

        inner_length = int(self.max_whitespace)
        inner_line = self.create_string(
            inner_length,
            " "
        )
        inner_line = f"{character}{inner_line}{character}"

        generated_content = f"{box_wall}\n"
        if "\n" in msg:
            max_height = (inner_length / 4) - len(msg)
            if max_height <= 2:
                max_height = 2
        else:
            max_height = 2
        i = 0
        while i < max_height:
            generated_content += f"{inner_line}\n"
            i += 1
        generated_content += f"{title_content}"
        i = 0
        while i < max_height:
            generated_content += f"{inner_line}\n"
            i += 1

        generated_content += f"{box_wall}"

        self.animate_message(
            f"{generated_content}",
            self.message_animation_delay
        )

    def box_vertical_no_horizontal(self, message: str, character: str = "") -> None:
        """
        Print another box format, this time without the internal bars\n
        But due to the code editor's rendering, it removes spaces, thus, if you want an accurate view, look at the raw comment of the function\n
        The text is displayed in the center of the box, it is just difficult to show that in a function comment\n
        Here is a sample box:\n
        \#                            #\n
        \#                            #\n
        \#                            #\n
        \#                            #\n
        \#                            #\n
        \#       Sample text          #\n
        \#                            #\n
        \#                            #\n
        \#                            #\n
        \#                            #\n
        \#                            #\n
        """

        if 'BOX_VERTICAL_NO_HORIZONTAL' in self.toml_content:
            character = self.toml_content['BOX_VERTICAL_NO_HORIZONTAL']
        elif character == '':
            character = "#"

        title_content = ""
        if "\n" in message:
            lines = message.split("\n")
            for i in lines:
                string_length = len(i)
                white_spaces = self._calculate_required_spaces(string_length)
                title_content += character
                title_content += white_spaces
                title_content += i
                if string_length % 2 == 1 and string_length != 0:
                    white_spaces = white_spaces[:-1]
                title_content += white_spaces
                title_content += character
                title_content += "\n"
            message = lines
        else:
            string_length = len(message)
            white_spaces = self._calculate_required_spaces(string_length)
            title_content += character
            title_content += white_spaces
            title_content += message
            if string_length % 2 == 1 and string_length != 0:
                white_spaces = white_spaces[:-1]
            title_content += white_spaces
            title_content += character
            title_content += "\n"
        inner_length = int(self.max_whitespace)
        if len(message) > self.max_whitespace:
            inner_length = self.max_whitespace
        inner_line = self.create_string(
            inner_length,
            " "
        )
        inner_line = f"{character}{inner_line}{character}"

        generated_content = ""
        if "\n" in message:
            max_height = (inner_length / 4) - len(message)
            if max_height <= 2:
                max_height = 2
        else:
            max_height = 2
        i = 0
        while i < max_height:
            generated_content += f"{inner_line}\n"
            i += 1
        generated_content += f"{title_content}"
        i = 0
        while i < max_height:
            if i+1 >= max_height:
                generated_content += f"{inner_line}"
            else:
                generated_content += f"{inner_line}\n"
            i += 1

        self.animate_message(
            f"{generated_content}",
            self.message_animation_delay
        )

    def title(self, title: str) -> None:
        """ 
        Print a beautified title \n
        This function calls the disp_message_box using the title parameters
        """
        self.disp_message_box(title, self.title_wall_chr)

    def sub_title(self, sub_title: str) -> None:
        """ 
        Print a beautified sub title\n
        This function calls the disp_message_box using the sub_title parameters
        """
        self.disp_message_box(sub_title, self.sub_title_wall_chr)

    def sub_sub_title(self, sub_sub_title: str) -> None:
        """
        Print a beautified sub sub title\n
        This function calls the disp_message_box using the sub_sub_title parameters
        """
        self.disp_message_box(sub_sub_title, self.sub_sub_title_wall_chr)

    def message(self, message: str) -> None:
        """
        Print a beautified message\n
        This function displays the provided message using the 'MESSAGE_CHARACTER' key in the toml configuration\n
        Here is an example for the output (This is determined by the key repeated twice)\n
        @@ This is an example message @@
        """
        self.animate_message(
            f"{self.message_char}{self.message_char} {message} {self.message_char}{self.message_char}",
            self.message_animation_delay
        )

    def error_message(self, message: str) -> None:
        """
        Print a beautified error message\n
        This function displays the provided message using the 'MESSAGE_ERROR_CHARACTER' key in the toml configuration\n
        Here is an example for the output (This is determined by the key repeated twice)\n
        @@ This is an example message @@
        """
        self.animate_message(
            f"{self.message_error_char}{self.message_error_char} Error: {message} {self.message_error_char}{self.message_error_char}",
            self.message_animation_delay
        )

    def success_message(self, message: str) -> None:
        """
        Print a beautified success message\n
        This function displays the provided message using the 'MESSAGE_SUCCESS_CHARACTER' key in the toml configuration\n
        Here is an example for the output (This is determined by the key repeated twice)\n
        @@ This is an example message @@
        """
        self.animate_message(
            f"{self.message_success_char}{self.message_success_char} Success: {message} {self.message_success_char}{self.message_success_char}",
            self.message_animation_delay
        )

    def warning_message(self, message: str) -> None:
        """
        Print a beautified warning message\n
        This function displays the provided message using the 'MESSAGE_WARNING_CHARACTER' key in the toml configuration\n
        Here is an example for the output (This is determined by the key repeated twice)\n
        @@ This is an example message @@
        """
        self.animate_message(
            f"{self.message_warning_char}{self.message_warning_char} Warning: {message} {self.message_warning_char}{self.message_warning_char}",
            self.message_animation_delay
        )

    def question_message(self, message: str) -> None:
        """
        Print a beautified question message\n
        This function displays the provided message using the 'MESSAGE_QUESTION_CHARACTER' key in the toml configuration\n
        Here is an example for the output (This is determined by the key repeated twice)\n
        @@ This is an example message @@
        """
        self.animate_message(
            f"{self.message_question_char}{self.message_question_char} Question: {message} {self.message_question_char}{self.message_question_char}",
            self.message_animation_delay
        )

    def inform_message(self, message: List) -> None:
        """
        Print a beautified information message\n
        This function displays the provided message using the 'MESSAGE_INFORM_CHARACTER' key in the toml configuration\n
        Here is an example for the output (This is determined by the key repeated twice)\n
        @@ This is an example message @@
        """
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

    def _tree_node(self, line, offset: int, index: int, max_lenght: int) -> str:
        """
        Display a line of the tree\n
        The characters displayed in this tree function is managed by the following keys:\n
        * TREE_NODE_CHAR\n
        * TREE_NODE_END_CHAR\n
        * TREE_LINE_SEPERATOR_CHAR\n
        * TREE_COLUMN_SEPERATOR_CHAR\n
        Here is an example generated by this function:\n
        ├─── data1\n
        └─── data2
        """
        processed_line = str()
        i = 0
        while i < offset:
            processed_line += f"{self.tree_column_seperator_char}   "
            i += 1
        if index is max_lenght:
            processed_line += f"{self.tree_node_end_char}{self.tree_line_seperator_char}{self.tree_line_seperator_char}{self.tree_line_seperator_char}"
        else:
            processed_line += f"{self.tree_node_char}{self.tree_line_seperator_char}{self.tree_line_seperator_char}{self.tree_line_seperator_char}"
        if self._is_safe(line) is False:
            line = f"{line}"
        processed_line += " "
        processed_line += line
        processed_line += '\n'
        return processed_line

    def tree(self, title: str, data: List[str], offset: int = 0) -> None:
        """
        Print a list under the form of a beautified tree\n
        The characters displayed in this tree function is managed by the following keys:\n
        * TREE_NODE_CHAR\n
        * TREE_NODE_END_CHAR\n
        * TREE_LINE_SEPERATOR_CHAR\n
        * TREE_COLUMN_SEPERATOR_CHAR\n
        Here is an example generated by this function:\n
        ├─── data1\n
        └─── data2
        """
        generated_content = ""
        if offset == 0:
            generated_content += f"{title}\n"
        length = len(data) - 1

        for line in enumerate(data):
            if isinstance(data, list) and isinstance(line[1], (list, dict)):
                generated_content += self._tree_node(
                    "<list instance>",
                    offset,
                    line[0],
                    length
                )
                generated_content += self.tree(line[0], line[1], offset + 1)
                continue
            if isinstance(data, dict) and isinstance(data[line[1]], (list, dict)):
                generated_content += self._tree_node(
                    line[1],
                    offset,
                    line[0],
                    length
                )
                generated_content += self.tree(
                    line[0],
                    data[line[1]],
                    offset + 1
                )
                continue
            if isinstance(data, dict) and isinstance(data[line[1]], dict) is False:
                generated_content += self._tree_node(
                    f"{line[1]}: {data[line[1]]}",
                    offset,
                    line[0],
                    length
                )
            else:
                generated_content += self._tree_node(
                    line[1],
                    offset,
                    line[0],
                    length
                )
        if offset == 0:
            self.animate_message(
                f"{generated_content}",
                self.message_animation_delay
            )
        else:
            return generated_content

    def append_run_date(self) -> None:
        """
        Add the date and time at which the program was launched\n
        The text is displayed in the center of the box, it is just difficult to show that in a function comment\n
        This is an example of the output (the design is controlled by the title function):\n
        Example:\n
        ########################################\n
        \#    Run date: 07/06/2024 22:26:10     #\n
        ########################################
        """
        self.title(f"Run date: {time.strftime('%d/%m/%Y %H:%M:%S')} ")

    def test_the_class(self) -> None:
        """
        This is a test function that you can use to have a template of the class\n
        It allows you to make sure all the implemented functions work as expected
        """
        test_data = {
            "test_data1": "test_data1.1",
            "test_data2": "test_data2.1",
            "test_data3": [
                "test_data_list3.1",
                "test_data_list3.2",
                "test_data_list3.3",
                "test_data_list3.4",
                "test_data_list3.5"
            ],
            "test_data4": "test_data4.1",
            "test_data5": {
                "test_data5.1": "test_data5.1.1",
                "test_data5.2": "test_data5.2.1",
                "test_data5.3": "test_data5.3.1",
                "test_data5.4": "test_data5.4.1"
            },
            "test_data6": [
                {
                    "test_data6.1": "test_data6.1.1",
                    "test_data6.2": "test_data6.2.1"
                },
                [
                    "test_data_list6.3.1",
                    "test_data_list6.3.1",
                    "test_data_list6.3.1",
                    "test_data_list6.3.1"
                ]
            ],
            "test_data7": {
                "test_data7.1": {
                    "test_data7.1.1": "test_data7.1.1.1",
                    "test_data7.1.2": "test_data7.1.2.1"
                },
                "test_data7.2": [
                    "test_data7.2.1",
                    "test_data7.2.2",
                    "test_data7.2.3",
                    "test_data7.2.4",
                    "test_data7.2.5"
                ]
            }
        }
        self.append_run_date()
        self.animate_message("Test Message !", 0.01)
        self.question_message("Test Question message !")
        self.error_message("Test Error !")
        self.inform_message("Test Inform !")
        self.success_message("Test Success !")
        self.warning_message("Test Warning !")
        self.title("Test title")
        self.sub_title("Test sub title")
        self.sub_sub_title("Test sub sub title")
        self.disp_box_no_vertical('Test Box no vertical')
        self.disp_round_message_box("Test Disp round message box")
        self.disp_diff_side_and_top_message_box(
            "Test Disp diff side and top message box"
        )
        self.disp_vertical_message_box("Test Disp vertical message box")
        self.box_vertical_no_horizontal("Test Box vertical no horizontal")
        self.tree("Test data", test_data)
        self.close_file()


if __name__ == "__main__":
    DI = Disp(
        toml_content=TOML_CONF,
        save_to_file=False,
        file_name="test_run.tmp",
        file_descriptor=None,
        debug=False
    )
    DI.test_the_class()
