# This file is generated by objective.metadata
#
# Last update: Sat Feb 18 13:01:48 2023
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
        b"STScreenTimeConfiguration",
        b"enforcesChildRestrictions",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"STWebHistory",
        b"initWithBundleIdentifier:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(b"STWebpageController", b"URLIsBlocked", {"retval": {"type": b"Z"}})
    r(b"STWebpageController", b"URLIsPictureInPicture", {"retval": {"type": b"Z"}})
    r(b"STWebpageController", b"URLIsPlayingVideo", {"retval": {"type": b"Z"}})
    r(
        b"STWebpageController",
        b"setBundleIdentifier:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"STWebpageController",
        b"setSuppressUsageRecording:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"STWebpageController",
        b"setURLIsPictureInPicture:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"STWebpageController",
        b"setURLIsPlayingVideo:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"STWebpageController", b"suppressUsageRecording", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
