import os
import logging
from pathlib import Path

import sys

# Adding root dir to sys.path to avoid "module not found" when pytest is run from any sub directory of
# the root directory example
# (vts_auto)  C:\PycharmProjects\vts_auto\tests\temp_test> pytest

PROJECT_NAME = "vts_auto"

# To suppress selenium-wire logs
logging.getLogger("seleniumwire.proxy.handler").setLevel(logging.WARNING)

p = Path(os.getcwd())
if str(p).endswith(PROJECT_NAME):  # when pytest is run from root directory
    sys.path.insert(0, str(p))
else:  # when pytest is run from roots subdirectories
    for path in p.parents:
        if str(path).endswith(PROJECT_NAME):
            sys.path.insert(0, str(path))
            break
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<XXXXXX>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
for line in sys.path:
    print(line)
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<XXXXXX>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")