# Arank - UserBot
# Copyright (C) 2021-2022 Mr_Mrs_Krishna
#
# This file is a part of < https://github.com/Mr_Mrs_Krishna/Arank/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/CoderXKrishna/pyArank/blob/main/LICENSE>.

from .. import udB


def get_channels():  # Returns List
    return udB.get_key("BROADCAST") or []


def is_channel_added(id_):
    return id_ in get_channels()


def add_channel(id_):
    channels = get_channels()
    if id_ not in channels:
        channels.append(id_)
        udB.set_key("BROADCAST", channels)
    return True


def rem_channel(id_):
    channels = get_channels()
    if id_ in channels:
        channels.remove(id_)
        udB.set_key("BROADCAST", channels)
        return True
    return False
