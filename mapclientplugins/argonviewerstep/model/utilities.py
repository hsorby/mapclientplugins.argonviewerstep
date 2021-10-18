import json
import os

from opencmiss.zinc.context import Context
from opencmiss.zinc.result import RESULT_OK


def is_argon_file(filename):
    if not os.path.isfile(filename):
        return False

    with open(filename, 'r') as f:
        state = f.read()

    try:
        d = json.loads(state)
    except json.JSONDecodeError:
        return False

    if 'OpenCMISS-Argon Version' not in d:
        return False

    return True


def is_exf_file(filename):
    if not os.path.isfile(filename):
        return False

    context = Context('exf_file')
    region = context.getDefaultRegion()
    return region.readFile(filename) == RESULT_OK
