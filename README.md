# ask_question

## Description

This is a python package I created in order to simplify the boiling process when asking the user a question via TTY.

## Table of Content

1. [ask_question](#askquestion)
2. [Description](#description)
3. [Table of Content](#table-of-content)
4. [Installation](#installation)
    1. [Using pip](#using-pip)
    2. [Using python](#using-python)
5. [Usage](#usage)
    1. [Impoting](#importing)
    2. [Initialising](#initialising)
    3. [Calling the pause function](#calling-the-pause-function)
    4. [Asking a question](#asking-a-question)
        1. [Where do you live ?](#where-do-you-live)
        2. [How old are you ?](#how-old-are-you)
        3. [Do you like sugar ?](#do-you-like-sugar)
6. [Available boiling](#available-boiling)
7. [Change the initialisation content](#change-the-initialisation-content)
    1. [Changing the forbidden characters](#changing-the-forbidden-characters)
    2. [Changing the description](#changing-the-descriptions)
    3. [Changing both](#changing-both)
8. [Author](#author)
9. [Version](#version)

## Installation

### Using pip

```sh
pip install -U ask-question
```

### Using python

Under windows:

```bat
py -m pip install -U ask-question
```

Under Linux/Mac OS:

```sh
python3 -m pip install -U ask-question
```

## Usage

### Importing

```py
import ask_question as aq
```

### Initialising

The generic class is: `AskQuestion(human_type:dict={}, illegal_characters_nb:str="")`

```py
AQI = aq.AskQuestion()
```

### Calling the pause function

The generic function is:

```py
pause(self, pause_message:str="Press enter to continue...")
```

The output is: None

```py
AQI.pause("Press enter to continue ...")
```

### Asking a Question

The generic function to ask a question is:

```py
ask_question(self, question:str, answer_type:str)
```

The outputs of this functions can be:

* str   = a string
* int   = a whole number
* float = a floating number

#### Where do you live ?

```py
answer = AQI.ask_question("Where are you from? ", "str")
print(f"You live in {answer}!")
```

#### How old are you ?

```py
answer = AQI.ask_question("How old are you?", "uint")
ADD_S = ""
if answer > 1:
    ADD_S = "s"
print(f"You are {answer} year{ADD_S} old !")
```

#### Do you like sugar ?

```py
answer = AQI.ask_question("Do you like sugar? [(Y)es/(n)o]: ", "bool")
if answer == True:
    print("You like sugar !")
else:
    print("You do not like sugar.")
```

## Available boiling

Here are all the available boiling options and their explanation:

* int = whole number (-1, 0, 1, 2, 3, etc...)
* float = floating number (-1.2, 0.1, 1.2, etc...)
* uint = whole positive number (0, 1, 2, etc...)
* ufloat = whole positive floating number (0.1, 1.2, etc ...)
* num = numeric (numbers from 0 onwards)
* alnum = alphanumeric (only numbers and the alphabet)
* isalpha = alphabet (from a to z and A to Z)
* char = alphabet (from a to z and A to Z)
* ascii = ascii Table
* str = string (any character you can type)
* version = version (numbers seperated by '.' characters)
* ver = version (numbers seperated by '.' characters)
* bool = boolean (yes/True/1 or no/False/0 answer type)

## Change the initialisation content

When initialising the class it is possible to change the forbidden characters and/or the descriptions of the available types.

### changing the forbidden characters

```py
import ask_question as aq
illegal_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \\t\\n\\r\\x0b\\x0c"
illegal_characters = illegal_characters.replace("0123456789","")
AQI = aq.AskQuestion(dict(), illegal_characters)
```

This initialisation has changed the characters that will be allowed for the number conversion in the 'int' and 'float' options.

### Changing the descriptions

```py
import ask_question as aq
human_type = {
    "int":"whole number (-1, 0, 1, 2, 3, etc...)",
    "float":"floating number (-1.2, 0.1, 1.2, etc...)",
    "uint":"whole positive number (0, 1, 2, etc...)",
    "ufloat":"whole positive floating number (0.1, 1.2, etc ...)",
    "num":"numeric (numbers from 0 onwards)",
    "alnum":"alphanumeric (only numbers and the alphabet)",
    "isalpha":"alphabet (from a to z and A to Z)",
    "char":"alphabet (from a to z and A to Z)",
    "ascii":"ascii Table",
    "str":"string (any character you can type)",
    "version":"version (numbers seperated by '.' characters)",
    "ver":"version (numbers seperated by '.' characters)",
    "bool":"boolean (yes/True/1 or no/False/0 answer type)",
}
AQI = aq.AskQuestion(human_type)
```

This initialisation has changed the descriptions for the types.
When the user will enter a wrong answer, the description displayed for the type you were expecting will be taken from the human_type dictionnary you have entered.

### Changing both

```py
import ask_question as aq
illegal_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \\t\\n\\r\\x0b\\x0c"
illegal_characters = illegal_characters.replace("0123456789","")
human_type = {
    "int":"whole number (-1, 0, 1, 2, 3, etc...)",
    "float":"floating number (-1.2, 0.1, 1.2, etc...)",
    "uint":"whole positive number (0, 1, 2, etc...)",
    "ufloat":"whole positive floating number (0.1, 1.2, etc ...)",
    "num":"numeric (numbers from 0 onwards)",
    "alnum":"alphanumeric (only numbers and the alphabet)",
    "isalpha":"alphabet (from a to z and A to Z)",
    "char":"alphabet (from a to z and A to Z)",
    "ascii":"ascii Table",
    "str":"string (any character you can type)",
    "version":"version (numbers seperated by '.' characters)",
    "ver":"version (numbers seperated by '.' characters)",
    "bool":"boolean (yes/True/1 or no/False/0 answer type)",
}
AQI = aq.AskQuestion(human_type)
```

You have now impacted the int and float typing as well as the 'type' descriptions.

## Author

This module was written by (c) Henry Letellier
Attributions are appreciated.

Quick way (I assume you have already initialised the class):

```py
print(f"AskQuestion is written by {AQI.author}")
```

## Version

The current version is 1.0.0

An easy way to display the version is:

```py
import ask_question as aq
print(f"Version : {aq.__Version__}")
```
