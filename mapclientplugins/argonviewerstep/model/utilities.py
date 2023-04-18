import os

from cmlibs.zinc.context import Context
from cmlibs.zinc.result import RESULT_OK


def is_exf_file(filename):
    if not os.path.isfile(filename):
        return False

    context = Context('exf_file')
    region = context.getDefaultRegion()
    return region.readFile(filename) == RESULT_OK
