import enum


class MusicLabel(enum.Enum):
    note = 0
    chord = 1000
    rest = 2000
    tempo = 3000
    TimeSignature = 4000
    KeySignature = 5000
    other = 6000
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
