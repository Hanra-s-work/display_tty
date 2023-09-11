"""
File in charge of helping the output of the program
"""

from disp import Disp
import constants as CONST

IDISP = Disp(
    CONST.TOML_CONF,
    CONST.SAVE_TO_FILE,
    CONST.FILE_NAME,
)
