# Color codes & quick access to error, and warning message prefixes
from sre_constants import SUCCESS


class Text:
    # Colors
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GRAY = '\033[37m'
    # Formatting + Reset all
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    # Prefixes
    ERROR = f'{GRAY}[{RED}!!{GRAY}]{RESET} '
    WARN = f'{GRAY}[{YELLOW}!{GRAY}]{RESET} '
    INFO = f'{GRAY}[{BLUE}*{GRAY}]{RESET} '
    SUCCESS = f'{GRAY}[{GREEN}*{GRAY}]{RESET} '