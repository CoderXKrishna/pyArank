# Arank - UserBot
# Copyright (C) 2021-2022 Mr_Mrs_Krishna
#
# This file is a part of < https://github.com/Mr_Mrs_Krishna/Arank/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/CoderXKrishna/pyArank/blob/main/LICENSE>.
from .. import udB


def get_stuff():
    return udB.get_key("GBLACKLISTS") or []


def add_gblacklist(id):
    ok = get_stuff()
    if id not in ok:
        ok.append(id)
        return udB.set_key("GBLACKLISTS", ok)


def rem_gblacklist(id):
    ok = get_stuff()
    if id in ok:
        ok.remove(id)
        return udB.set_key("GBLACKLISTS", ok)


def is_gblacklisted(id):
    return id in get_stuff()
