# Arank - UserBot
# Copyright (C) 2021-2022 Mr_Mrs_Krishna
#
# This file is a part of < https://github.com/Mr_Mrs_Krishna/Arank/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/CoderXKrishna/pyArank/blob/main/LICENSE>.

from .. import udB


def get_approved():
    return udB.get_key("PMPERMIT") or []


def approve_user(id):
    ok = get_approved()
    if id in ok:
        return True
    ok.append(id)
    return udB.set_key("PMPERMIT", ok)


def disapprove_user(id):
    ok = get_approved()
    if id in ok:
        ok.remove(id)
        return udB.set_key("PMPERMIT", ok)


def is_approved(id):
    return id in get_approved()
