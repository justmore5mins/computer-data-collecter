# This file is generated by objective.metadata
#
# Last update: Sun Feb 20 18:49:06 2022
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
misc.update(
    {
        "DRBurnSessionProgressDialogOptions": objc.createStructType(
            "DiscRecordingUI.DRBurnSessionProgressDialogOptions",
            b"{DRBurnSessionProgressDialogOptions=II^{__CFString=}}",
            ["version", "dialogOptionFlags", "description"],
        ),
        "DREraseSessionSetupDialogOptions": objc.createStructType(
            "DiscRecordingUI.DREraseSessionSetupDialogOptions",
            b"{DREraseSessionSetupDialogOptions=II}",
            ["version", "dialogOptionFlags"],
        ),
        "DREraseSessionProgressDialogOptions": objc.createStructType(
            "DiscRecordingUI.DREraseSessionProgressDialogOptions",
            b"{DREraseSessionProgressDialogOptions=II^{__CFString=}}",
            ["version", "dialogOptionFlags", "description"],
        ),
        "DRBurnSessionSetupDialogOptions": objc.createStructType(
            "DiscRecordingUI.DRBurnSessionSetupDialogOptions",
            b"{DRBurnSessionSetupDialogOptions=II^{__CFString=}}",
            ["version", "dialogOptionFlags", "defaultButtonTitle"],
        ),
    }
)
constants = """$DRBurnIcon$DRBurnProgressPanelDidFinishNotification$DRBurnProgressPanelWillBeginNotification$DRBurnSetupPanelDefaultButtonDefaultTitle$DREraseIcon$DREraseProgressPanelDidFinishNotification$DREraseProgressPanelWillBeginNotification$DRSetupPanelDeviceSelectionChangedNotification$DRSetupPanelSelectedDeviceKey$"""
enums = """$kBurnSessionProgressDialogDefaultOptions@0$kBurnSessionProgressDialogDisplayVerboseProgress@1$kBurnSessionProgressDialogOptionsCurrentVersion@1$kBurnSessionSetupDialogAllowTestBurns@2147483652$kBurnSessionSetupDialogDefaultOptions@0$kBurnSessionSetupDialogDontHandleReservations@2$kBurnSessionSetupDialogForceClosedDiscs@1$kBurnSessionSetupDialogOptionsCurrentVersion@1$kDRBurnProgressSetupCallbacksCurrentVersion@1$kDRBurnSessionCancel@0$kDRBurnSessionOK@1$kDRBurnSessionSetupCallbacksCurrentVersion@1$kDREraseProgressSetupCallbacksCurrentVersion@1$kDREraseSessionCancel@0$kDREraseSessionOK@1$kDREraseSessionSetupCallbacksCurrentVersion@1$kEraseSessionProgressDialogDefaultOptions@0$kEraseSessionProgressDialogOptionsCurrentVersion@1$kEraseSessionSetupDialogDefaultOptions@0$kEraseSessionSetupDialogDontHandleReservations@1$kEraseSessionSetupDialogOptionsCurrentVersion@1$"""
misc.update({})
misc.update({})
functions = {
    "DRBurnSessionSetBurn": (b"v^{__DRBurnSession=}^{__DRBurn=}",),
    "DRBurnSessionCreate": (
        b"^{__DRBurnSession=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DREraseSessionSetupDialog": (
        b"c^{__DREraseSession=}^{DREraseSessionSetupDialogOptions=II}^{DREraseSessionSetupCallbacks=I^?^?^?}",
        "",
        {"arguments": {1: {"type_modifier": "n"}, 2: {"type_modifier": "n"}}},
    ),
    "DRBurnSessionGetTypeID": (b"Q",),
    "DREraseSessionCreate": (
        b"^{__DREraseSession=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DREraseSessionGetTypeID": (b"Q",),
    "DRBurnSessionSetupDialog": (
        b"c^{__DRBurnSession=}^{DRBurnSessionSetupDialogOptions=II^{__CFString=}}^{DRBurnSessionSetupCallbacks=I^?^?^?}",
        "",
        {"arguments": {1: {"type_modifier": "n"}, 2: {"type_modifier": "n"}}},
    ),
    "DRBurnSessionGetBurn": (b"^{__DRBurn=}^{__DRBurnSession=}",),
    "DREraseSessionGetErase": (b"^{__DRErase=}^{__DREraseSession=}",),
    "DREraseSessionBeginProgressDialog": (
        b"v^{__DREraseSession=}^{DREraseSessionProgressDialogOptions=II^{__CFString=}}^{DREraseSessionProgressCallbacks=I^?^?^?}",
        "",
        {"arguments": {1: {"type_modifier": "n"}, 2: {"type_modifier": "n"}}},
    ),
    "DREraseSessionSetErase": (b"v^{__DREraseSession=}^{__DRErase=}",),
    "DRBurnSessionBeginProgressDialog": (
        b"v^{__DRBurnSession=}@^{DRBurnSessionProgressDialogOptions=II^{__CFString=}}^{DRBurnSessionProgressCallbacks=I^?^?^?}",
        "",
        {"arguments": {2: {"type_modifier": "n"}, 3: {"type_modifier": "n"}}},
    ),
}
cftypes = [
    ("DRBurnSessionRef", b"^{__DRBurnSession=}", None, None),
    ("DREraseSessionRef", b"^{__DREraseSession=}", None, None),
]
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"DRBurnProgressPanel",
        b"setVerboseProgressStatus:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"DRBurnProgressPanel", b"verboseProgressStatus", {"retval": {"type": b"Z"}})
    r(
        b"DRBurnSetupPanel",
        b"setCanSelectAppendableMedia:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"DRBurnSetupPanel", b"setCanSelectTestBurn:", {"arguments": {2: {"type": b"Z"}}})
    r(b"DRSetupPanel", b"mediaStateChanged:", {"retval": {"type": b"Z"}})
    r(
        b"NSObject",
        b"burnProgressPanel:burnDidFinish:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"burnProgressPanelDidFinish:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"burnProgressPanelWillBegin:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"eraseProgressPanel:eraseDidFinish:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"eraseProgressPanelDidFinish:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"eraseProgressPanelWillBegin:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setupPanel:determineBestDeviceOfA:orB:",
        {
            "retval": {"type": b"@"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"setupPanel:deviceContainsSuitableMedia:promptString:",
        {
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"^@"}},
        },
    )
    r(
        b"NSObject",
        b"setupPanel:deviceCouldBeTarget:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setupPanelDeviceSelectionChanged:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setupPanelShouldHandleMediaReservations:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"null", b"burnProgressPanel:burnDidFinish:", {"retval": {"type": b"Z"}})
    r(b"null", b"eraseProgressPanel:eraseDidFinish:", {"retval": {"type": b"Z"}})
    r(
        b"null",
        b"setupPanel:deviceContainsSuitableMedia:promptString:",
        {"retval": {"type": b"Z"}},
    )
    r(b"null", b"setupPanel:deviceCouldBeTarget:", {"retval": {"type": b"Z"}})
    r(b"null", b"setupPanelShouldHandleMediaReservations:", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)
protocols = {
    "DRBurnProgressPanelDelegateMethods": objc.informal_protocol(
        "DRBurnProgressPanelDelegateMethods",
        [
            objc.selector(
                None, b"burnProgressPanelDidFinish:", b"v@:@", isRequired=False
            ),
            objc.selector(
                None, b"burnProgressPanelWillBegin:", b"v@:@", isRequired=False
            ),
            objc.selector(
                None, b"burnProgressPanel:burnDidFinish:", b"Z@:@@", isRequired=False
            ),
        ],
    ),
    "DRSetupPanelDelegate": objc.informal_protocol(
        "DRSetupPanelDelegate",
        [
            objc.selector(
                None,
                b"setupPanel:deviceContainsSuitableMedia:promptString:",
                b"Z@:@@^@",
                isRequired=False,
            ),
            objc.selector(
                None, b"setupPanel:deviceCouldBeTarget:", b"Z@:@@", isRequired=False
            ),
            objc.selector(
                None,
                b"setupPanelShouldHandleMediaReservations:",
                b"Z@:@",
                isRequired=False,
            ),
            objc.selector(
                None, b"setupPanelDeviceSelectionChanged:", b"v@:@", isRequired=False
            ),
            objc.selector(
                None,
                b"setupPanel:determineBestDeviceOfA:orB:",
                b"@@:@@@",
                isRequired=False,
            ),
        ],
    ),
    "DREraseProgressPanelDelegateMethods": objc.informal_protocol(
        "DREraseProgressPanelDelegateMethods",
        [
            objc.selector(
                None, b"eraseProgressPanelWillBegin:", b"v@:@", isRequired=False
            ),
            objc.selector(
                None, b"eraseProgressPanel:eraseDidFinish:", b"Z@:@@", isRequired=False
            ),
            objc.selector(
                None, b"eraseProgressPanelDidFinish:", b"v@:@", isRequired=False
            ),
        ],
    ),
}
expressions = {}

# END OF FILE
