
from .my_disp import Disp
from .constants import TOML_CONF, SAVE_TO_FILE, FILE_NAME

TMP = None  # linter bypass for a false positive of statement has no effect

"""
@var IDISP
@brief Initialised instance of the Disp class with default configuration.
"""
IDISP = Disp(
    TOML_CONF,
    SAVE_TO_FILE,
    FILE_NAME,
)

"""
@var IDISPLAY
@brief Alias for IDISP.
"""
IDISPLAY = IDISP

"""
@var IDISPTTY
@brief Alias for IDISP.
"""
IDISPTTY = IDISP

"""
@var IDTTY
@brief Alias for IDISP.
"""
IDTTY = IDISP
