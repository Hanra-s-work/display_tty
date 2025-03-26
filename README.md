# Display tty

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/display_tty)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/display_tty)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/display_tty)
![PyPI - Version](https://img.shields.io/pypi/v/display_tty?label=pypi%20package:%20display_tty)
![PyPI - Downloads](https://img.shields.io/pypi/dm/display_tty)
![PyPI - License](https://img.shields.io/pypi/l/display_tty)
![Execution status](https://github.com/Hanra-s-work/display_tty/actions/workflows/run_unit_tests.yaml/badge.svg)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/Hanra-s-work/display_tty/run_unit_tests.yaml)
![GitHub repo size](https://img.shields.io/github/repo-size/Hanra-s-work/display_tty)
![GitHub Repo stars](https://img.shields.io/github/stars/Hanra-s-work/display_tty)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/m/Hanra-s-work/display_tty)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/Hanra-s-work/display_tty/main)

[![Static Badge](https://img.shields.io/badge/Buy_me_a_tea-Hanra-%235F7FFF?style=flat-square&logo=buymeacoffee&label=Buy%20me%20a%20coffee&labelColor=%235F7FFF&color=%23FFDD00&link=https%3A%2F%2Fwww.buymeacoffee.com%2Fhanra)](https://www.buymeacoffee.com/hanra)

## Description

This is a python package I created in order to simplify the boiling process for displaying text in a geometrical shape drawn using characters.

## Disclaimer

The package was originally named `disp` but had to be changed to `display_tty` because the names `disp` and `display` were already taken by other packages.

The class will still remain `Disp` but bindings named `Display`, `DispTTY` and `DisplayTTY` are available.

The Preloaded version exists under: `IDISP`, `IDISPLAY`, `IDTTY` and `IDISPTTY`

## Table of Content

1. [Display tty](#display-tty)
2. [Description](#description)
3. [Disclaimer](#disclaimer)
4. [Table of Content](#table-of-content)
5. [Installation](#installation)
    1. [Using pip](#using-pip)
    2. [Using python](#using-python)
6. [Usage](#usage)
    1. [Importing](#importing)
    2. [Initialising](#initialising)
    3. [Calling the tree function](#calling-the-tree-function)
    4. [Displaying a beautified Hello World](#displaying-a-beautified-hello-world)
        1. [Hello World as a title](#hello-world-as-a-title)
        2. [Hello World as a sub title](#hello-world-as-a-sub-title)
        3. [Hello World as a sub sub title](#hello-world-as-a-sub-sub-title)
        4. [Hello World as a message with adjustable delay per call](#hello-world-as-a-message-with-adjustable-delay-per-call)
        5. [Hello World as a message](#hello-world-as-a-message)
        6. [Hello World as a question message](#hello-world-as-a-question-message)
        7. [Hello World as an error message](#hello-world-as-an-error-message)
        8. [Hello World as a success message](#hello-world-as-a-success-message)
        9. [Hello World as a warning message](#hello-world-as-a-warning-message)
        10. [Hello World as an inform message](#hello-world-as-an-inform-message)
7. [Change the initialisation content](#change-the-initialisation-content)
    1. [TOML configuration breakdown](#toml-configuration-breakdown)
        1. [line 1](#line-1)
        2. [line 2](#line-2)
        3. [line 3](#line-3)
        4. [line 4](#line-4)
        5. [line 5](#line-5)
        6. [line 6](#line-6)
        7. [line 7](#line-7)
        8. [line 8](#line-8)
        9. [line 9](#line-9)
        10. [line 10](#line-10)
        11. [line 11](#line-11)
        12. [line 12](#line-12)
        13. [line 13](#line-13)
        14. [line 14](#line-14)
        15. [line 15](#line-15)
        16. [line 16](#line-16)
        17. [line 17](#line-17)
    2. [Update the configuration of an initialised class](#update-the-configuration-of-an-initialised-class)
8. [Author](#author)
9. [Version](#version)

## Installation

### Using pip

```sh
pip install -U disp
```

### Using python

Under Windows:

```bat
py -m pip install -U display_tty
```

Under Linux/Mac OS:

```sh
python3 -m pip install -U display_tty
```

## Usage

### Importing

```py
from display_tty import IDTTY
```

### Initialising

The generic class is: `Disp(toml_content: dict, save_to_file: bool = False, file_name: str = "text_output_run.txt", file_descriptor: any = None)`

For your convenience, you can use the `IDTTY` variable which is an initialised version of the class.

```py
IDTTY.title("Hello World")
```

Otherwise, if you wish to initialise the class with your own parameters, you can do so like this:

```py
from display_tty import DisplayTTY
TOML_CONF = {
    'PRETTIFY_OUTPUT': True,
    'PRETTY_OUTPUT_IN_BLOCS': True,
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
    'MESSAGE_ANIMATION_DELAY_BLOCKY': 0.01,
    'MESSAGE_ANIMATION_DELAY': 0.01
}

SAVE_TO_FILE = False
FILE_NAME = "run_results.txt"
FILE_DESCRIPTOR = None


IDTTY = DisplayTTY(
    TOML_CONF,
    SAVE_TO_FILE,
    FILE_NAME,
)
```

### Calling the tree function

The generic function is:

```py
tree(self, title: str, data: list[str], offset: int = 0)
```

The output is: None

```py
TEST_DATA = {
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

IDTTY.tree("This is a test tree", TEST_DATA, 0)
```

### Displaying a beautified Hello World

#### Hello World as a title

The generic function to display `Hello World!` as a title is:

```py
title(self, title)
```

The outputs is: None

```py
IDTTY.title("Hello World !")
```

#### Hello World as a sub title

The generic function to display `Hello World!` as a sub title is:

```py
sub_title(self, sub_title)
```

The outputs is: None

```py
IDTTY.sub_title("Hello World !")
```

#### Hello World as a sub sub title

The generic function to display `Hello World!` as a sub sub  title is:

```py
sub_sub_title(self, sub_sub_title)
```

The outputs is: None

```py
IDTTY.sub_sub_title("Hello World !")
```

#### Hello World as a message with adjustable delay per call

The generic function to display `Hello World!` as a message is:

```py
animate_message(self, message: str = "Hello World!", delay: float = 0.02)
```

The outputs is: None

```py
IDTTY.animate_message("Hello World !", 0.01)
```

#### Hello World as a message

The generic function to display `Hello World!` as a message is:

```py
message(self, message:str)
```

The outputs is: None

```py
IDTTY.message("Hello World !")
```

#### Hello World as a question message

The generic function to display `Hello World!` as a question message is:

```py
question_message(self, message: str)
```

The outputs is: None

```py
IDTTY.question_message("Hello World !")
```

#### Hello World as an error message

The generic function to display `Hello World!` as an error message is:

```py
error_message(self, message: str)
```

The outputs is: None

```py
IDTTY.error_message("Hello World !")
```

#### Hello World as a success message

The generic function to display `Hello World!` as a success message is:

```py
success_message(self, message: str)
```

The outputs is: None

```py
IDTTY.success_message("Hello World !")
```

#### Hello World as a warning message

The generic function to display `Hello World!` as a warning message is:

```py
warning_message(self, message: str)
```

The outputs is: None

```py
IDTTY.warning_message("Hello World !")
```

#### Hello World as an inform message

The generic function to display `Hello World!` as an inform message is:

```py
append_run_date(self)
```

The outputs is: None

```py
IDTTY.append_run_date()
```

### Displaying the current date

The generic function to display the current date as a title is:

```py
inform_message(self, message: list)
```

The outputs is: None

```py
IDTTY.inform_message("Hello World !")
```

## Change the initialisation content

When initialising the class it is possible to change the animation behaviour by editing the `TOML_CONF` that you must provide when initialising the class.

During the initialisation it is also possible to redirect the output to a file instead of displaying it on the terminal. For this, please set the `save_to_file` to `True` and either:

* provide a file name in `file_name`

* provide a file descriptor in `file_descriptor`

If you provided a `file_name`, the file will automatically be opened
However, in both cases, you will need to close the file by calling the function `close_file` (i.e. at the end of your program)

### TOML configuration breakdown

This is the arguments that are required in the `TOML` file:

```txt #toml
1  | PRETTIFY_OUTPUT: True,
2  | PRETTY_OUTPUT_IN_BLOCS: True,
3  | MESSAGE_CHARACTER: '@',
4  | MESSAGE_ERROR_CHARACTER: '#',
5  | MESSAGE_INFORM_CHARACTER: '!',
6  | MESSAGE_QUESTION_CHARACTER: '?',
7  | MESSAGE_SUCCESS_CHARACTER: '/',
8  | MESSAGE_WARNING_CHARACTER: '?',
9  | SUB_SUB_TITLE_WALL_CHARACTER: '*',
10 | SUB_TITLE_WALL_CHARACTER: '@',
11 | TITLE_WALL_CHARACTER: '#',
12 | TREE_COLUMN_SEPERATOR_CHAR: '│',
13 | TREE_LINE_SEPERATOR_CHAR: '─',
14 | TREE_NODE_CHAR: '├',
15 | TREE_NODE_END_CHAR: '└',
16 | MESSAGE_ANIMATION_DELAY_BLOCKY: 0.01,
17 | MESSAGE_ANIMATION_DELAY: 0.01
```

PS: I've added line numbers `<number> |` to help you track the analysis of the file, these are generally added automatically by your code editor.

Thats a big file, lets break it down together:

#### line 1

```txt #toml
PRETTIFY_OUTPUT: True
```

This option is a crucial pivot for the program.

If:

* `True`: The program will output the content letter by letter while waiting a specified delay
* `False`: It will print out all of your messages at once without waiting any delay

#### line 2

```txt #toml
PRETTY_OUTPUT_IN_BLOCS: True
```

This option is an optimisation for the program.

If:

* `True`: The program will:
  * Extract the words from the input
  * output the content word by word while waiting a specified delay and respecting spacing
* `False`: It will print out all of your messages at once without waiting any delay

#### line 3

```txt #toml
MESSAGE_CHARACTER: '@'
```

This is a customisation, it allows you to specify the characther to use when displaying a message.

#### line 4

```txt #toml
MESSAGE_ERROR_CHARACTER: '#'
```

This is a customisation, it allows you to specify the characther to use when displaying an error message.

#### line 5

```txt #toml
MESSAGE_INFORM_CHARACTER: '!'
```

This is a customisation, it allows you to specify the characther to use when displaying an inform message.

#### line 6

```txt #toml
MESSAGE_QUESTION_CHARACTER: '?'
```

This is a customisation, it allows you to specify the characther to use when displaying a question message.

#### line 7

```txt #toml
MESSAGE_SUCCESS_CHARACTER: '/'
```

This is a customisation, it allows you to specify the characther to use when displaying a success message.

#### line 8

```txt #toml
MESSAGE_WARNING_CHARACTER: '?'
```

This is a customisation, it allows you to specify the characther to use when displaying a warning message.

#### line 9

```txt #toml
SUB_SUB_TITLE_WALL_CHARACTER: '*'
```

This is a customisation, it allows you to specify the characther to use when displaying a sub sub title.

#### line 10

```txt #toml
SUB_TITLE_WALL_CHARACTER: '@'
```

This is a customisation, it allows you to specify the characther to use when displaying a sub title.

#### line 11

```txt #toml
TITLE_WALL_CHARACTER: '#'
```

This is a customisation, it allows you to specify the characther to use when displaying a title.

#### line 12

```txt #toml
TREE_COLUMN_SEPERATOR_CHAR: '│'
```

This is the character used by the tree function to indicate the indentation level

i.e:

```txt
│   ├─── my_file
```

#### line 13

```txt #toml
TREE_LINE_SEPERATOR_CHAR: '─'
```

This is the character used by the tree function to indicate the file/folder of the current line

i.e:

```txt
├─── my_file
```

#### line 14

```txt #toml
TREE_NODE_CHAR: '├'
```

This is the character used by the tree function to indicate the directory level to wich the file/directory is linked but that this is not the last file/directory.

i.e:

```txt
├─── my_file
```

#### line 15

```txt #toml
TREE_NODE_END_CHAR: '└'
```

This is the character used by the tree function to indicate the directory level to wich the file/directory is linked but that this is the last file/directory.

i.e:

```txt
└─── my_file
```

#### line 16

```txt #toml
MESSAGE_ANIMATION_DELAY_BLOCKY: 0.01
```

Specify the delay between each word placement. (min: 0)

PS: if you enter 0, this is like setting `PRETTY_OUTPUT_IN_BLOCS` to `False`

#### line 17

```txt #toml
MESSAGE_ANIMATION_DELAY: 0.01
```

This variable is a pivot point for the program.

Specify the delay between each word placement. (min: 0)

PS: if you enter 0, this is like setting `PRETTY_OUTPUT_IN_BLOCS` to `False`

### Update the configuration of an initialised class

If the default initialisation, or the class you previously initialised has some elements you would like to update, you can do so by calling the inner variables.

Here are the variables you might be interested in:

```py
from display_tty import IDTTY
IDTTY.title_wall_chr # string (length 1): i.e.: '#'
IDTTY.sub_title_wall_chr # string (length 1): i.e.: '@'
IDTTY.sub_sub_title_wall_chr # string (length 1): i.e.: '*'
IDTTY.message_char # string (length 1): i.e.: '@'
IDTTY.message_error_char # string (length 1): i.e.: '#'
IDTTY.message_success_char # string (length 1): i.e.: '/'
IDTTY.message_inform_char # string (length 1): i.e.: 'i'
IDTTY.message_warning_char # string (length 1): i.e.: '!'
IDTTY.message_question_char # string (length 1): i.e.: '?'
IDTTY.message_animation_delay # float: i.e.: # 0.01
IDTTY.tree_node_char # string (length 1): i.e.: '├'
IDTTY.tree_node_end_char # string (length 1): i.e.: '└'
IDTTY.tree_line_seperator_char # string (length 1): i.e.: '─'
IDTTY.tree_column_seperator_char # string (length 1): i.e.: '│'
IDTTY.save_to_file # True or False
IDTTY.toml_content["PRETTIFY_OUTPUT"] # True of False
IDTTY.toml_content["PRETTY_OUTPUT_IN_BLOCS"] # True of False
```

To update a variable, simply assing it a new value, like in this example: `IDTTY.title_wall_chr = "&"`

PS: These changes only apply to the class you loaded, any others will not be touched.

## Author

This module was written by (c) Henry Letellier
Attributions are appreciated.

Quick way:

```py
print(f"AskQuestion is written by {IDTTY.author}")
```

## Version

The current version is 1.0.0

An easy way to display the version is:

```py
import display_tty as IDTTY
print(f"Version : {IDTTY.__Version__}")
```
