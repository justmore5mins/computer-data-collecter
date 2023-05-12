# This file is generated by objective.metadata
#
# Last update: Sat Feb 18 13:01:27 2023
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$$"""
enums = """$$"""
misc.update({})
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"eventDidFail:withError:",
        {
            "required": True,
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": "r^{AEDesc=I^^{OpaqueAEDataStorageType}}"},
                3: {"type": b"@"},
            },
        },
    )
    r(b"SBApplication", b"isRunning", {"retval": {"type": "Z"}})
    r(
        b"SBElementArray",
        b"arrayByApplyingSelector:",
        {"arguments": {2: {"sel_of_type": b"@@:"}}},
    )
    r(
        b"SBElementArray",
        b"arrayByApplyingSelector:withObject:",
        {"arguments": {2: {"sel_of_type": b"@@:@"}}},
    )
    r(b"SBObject", b"sendEvent:id:parameters:", {"variadic": True})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
