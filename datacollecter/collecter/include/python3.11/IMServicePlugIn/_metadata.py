# This file is generated by objective.metadata
#
# Last update: Sun Feb 20 18:51:53 2022
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
        "IMServicePlugInMessageInternal": objc.createStructType(
            "IMServicePlugIn.IMServicePlugInMessageInternal",
            b"{_IMServicePlugInMessageInternal=}",
            [],
        )
    }
)
constants = """$IMAccountSettingLoginHandle$IMAccountSettingPassword$IMAccountSettingServerHost$IMAccountSettingServerPort$IMAccountSettingUsesSSL$IMAttributeBackgroundColor$IMAttributeBaseWritingDirection$IMAttributeBold$IMAttributeFontFamily$IMAttributeFontSize$IMAttributeForegroundColor$IMAttributeItalic$IMAttributeLink$IMAttributeMessageBackgroundColor$IMAttributePreformatted$IMAttributeStrikethrough$IMAttributeUnderline$IMGroupListDefaultGroup$IMGroupListHandlesKey$IMGroupListNameKey$IMGroupListPermissionsKey$IMHandleCapabilityChatRoom$IMHandleCapabilityFileTransfer$IMHandleCapabilityHandlePicture$IMHandleCapabilityMessaging$IMHandleCapabilityOfflineMessaging$IMHandlePropertyAlias$IMHandlePropertyAuthorizationStatus$IMHandlePropertyAvailability$IMHandlePropertyCapabilities$IMHandlePropertyEmailAddress$IMHandlePropertyFirstName$IMHandlePropertyIdleDate$IMHandlePropertyLastName$IMHandlePropertyPictureData$IMHandlePropertyPictureIdentifier$IMHandlePropertyStatusMessage$IMSessionPropertyAvailability$IMSessionPropertyIdleDate$IMSessionPropertyIsInvisible$IMSessionPropertyPictureData$IMSessionPropertyStatusMessage$"""
enums = """$IMGroupListCanAddNewMembers@4$IMGroupListCanRemoveMembers@8$IMGroupListCanRenameGroup@2$IMGroupListCanReorderGroup@1$IMGroupListCanReorderMembers@16$IMHandleAuthorizationStatusAccepted@0$IMHandleAuthorizationStatusDeclined@2$IMHandleAuthorizationStatusPending@1$IMHandleAvailabilityAvailable@1$IMHandleAvailabilityAway@0$IMHandleAvailabilityOffline@-1$IMHandleAvailabilityUnknown@-2$IMSessionAvailabilityAvailable@1$IMSessionAvailabilityAway@0$"""
misc.update(
    {
        "IMHandleAvailability": NewType("IMHandleAvailability", int),
        "IMGroupListPermissions": NewType("IMGroupListPermissions", int),
        "IMSessionAvailability": NewType("IMSessionAvailability", int),
        "IMHandleAuthorizationStatus": NewType("IMHandleAuthorizationStatus", int),
    }
)
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"acceptAuthorizationRequestFromHandle:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"addGroups:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"addHandles:toGroup:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"declineAuthorizationRequestFromHandle:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"declineChatRoomInvitation:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"handleDidStartTyping:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"handleDidStopTyping:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"handles:didJoinChatRoom:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"handles:didLeaveChatRoom:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"initWithServiceApplication:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"inviteHandles:toChatRoom:withMessage:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"joinChatRoom:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"leaveChatRoom:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"login", {"required": True, "retval": {"type": b"v"}})
    r(b"NSObject", b"logout", {"required": True, "retval": {"type": b"v"}})
    r(
        b"NSObject",
        b"plugInDidFailToAuthenticate",
        {"required": True, "retval": {"type": b"v"}},
    )
    r(
        b"NSObject",
        b"plugInDidJoinChatRoom:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"plugInDidLeaveChatRoom:error:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(b"NSObject", b"plugInDidLogIn", {"required": True, "retval": {"type": b"v"}})
    r(
        b"NSObject",
        b"plugInDidLogOutWithError:reconnect:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "Z"}},
        },
    )
    r(
        b"NSObject",
        b"plugInDidReceiveAuthorizationRequestFromHandle:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"plugInDidReceiveInvitation:forChatRoom:fromHandle:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"plugInDidReceiveMessage:forChatRoom:fromHandle:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"plugInDidReceiveMessage:fromHandle:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"plugInDidReceiveNotice:forChatRoom:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"plugInDidSendMessage:toChatRoom:error:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"plugInDidSendMessage:toHandle:error:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"plugInDidUpdateGroupList:error:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"plugInDidUpdateProperties:ofHandle:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"removeGroups:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"removeHandles:fromGroup:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"renameGroup:toGroup:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"reorderGroups:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"reorderHandles:inGroup:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(b"NSObject", b"requestGroupList", {"required": True, "retval": {"type": b"v"}})
    r(
        b"NSObject",
        b"requestPictureForHandle:withIdentifier:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"sendAuthorizationRequestToHandle:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"sendMessage:toChatRoom:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"sendMessage:toHandle:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"updateAccountSettings:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"updateSessionProperties:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"userDidStartTypingToHandle:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"userDidStopTypingToHandle:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
