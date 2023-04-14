import json
import os

from cmlibs.zinc.context import Context
from cmlibs.zinc.result import RESULT_OK


def is_argon_file(filename):
    if not os.path.isfile(filename):
        return False

    try:
        with open(filename, 'r') as f:
            state = f.read()
    except UnicodeDecodeError:
        return False

    try:
        d = json.loads(state)
    except json.JSONDecodeError:
        return False

    # continue to read legacy OpenCMISS-Argon document
    if '-Argon Version' not in d:
        return False

    return True


def is_exf_file(filename):
    if not os.path.isfile(filename):
        return False

    context = Context('exf_file')
    region = context.getDefaultRegion()
    return region.readFile(filename) == RESULT_OK
