# Arank - UserBot
# Copyright (C) 2021-2022 Mr_Mrs_Krishna
#
# This file is a part of < https://github.com/CoderXKrishna/Arank/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/CoderXKrishna/pyArank/blob/main/LICENSE>.

import sys

from .version import __version__

run_as_module = False

if sys.argv[0] == "-m":
    run_as_module = True

    import time

    from .configs import Var
    from .startup import *
    from .startup._database import ArankDB
    from .startup.BaseClient import ArankClient
    from .startup.connections import session_file, vc_connection
    from .startup.funcs import _version_changes, autobot, enable_inline, update_envs
    from .version import Arank_version

    start_time = time.time()
    _ult_cache = {}

    udB = ArankDB()
    update_envs()

    LOGS.info(f"Connecting to {udB.name}...")
    if udB.ping():
        LOGS.info(f"Connected to {udB.name} Successfully!")

    BOT_MODE = udB.get_key("BOTMODE")
    DUAL_MODE = udB.get_key("DUAL_MODE")

    if BOT_MODE:
        if DUAL_MODE:
            udB.del_key("DUAL_MODE")
            DUAL_MODE = False
        Arank_bot = None
    else:
        Arank_bot = ArankClient(
            session_file(LOGS),
            udB=udB,
            app_version=Arank_version,
            device_model="Arank",
            proxy=udB.get_key("TG_PROXY"),
        )

    if not BOT_MODE:
        Arank_bot.run_in_loop(autobot())
    else:
        if not udB.get_key("BOT_TOKEN"):
            LOGS.critical(
                '"BOT_TOKEN" not Found! Please add it, in order to use "BOTMODE"'
            )

            sys.exit()

    asst = ArankClient(None, bot_token=udB.get_key("BOT_TOKEN"), udB=udB)

    if BOT_MODE:
        Arank_bot = asst
        if udB.get_key("OWNER_ID"):
            try:
                Arank_bot.me = Arank_bot.run_in_loop(
                    Arank_bot.get_entity(udB.get_key("OWNER_ID"))
                )
            except Exception as er:
                LOGS.exception(er)
    elif not asst.me.bot_inline_placeholder:
        Arank_bot.run_in_loop(enable_inline(Arank_bot, asst.me.username))

    vcClient = vc_connection(udB, Arank_bot)

    _version_changes(udB)

    HNDLR = udB.get_key("HNDLR") or "."
    DUAL_HNDLR = udB.get_key("DUAL_HNDLR") or "/"
    SUDO_HNDLR = udB.get_key("SUDO_HNDLR") or HNDLR
else:
    print("pyArank 2022 © Mr_Mrs_Krishna")

    from logging import getLogger

    LOGS = getLogger("pyArank")

    Arank_bot = asst = udB = vcClient = None
