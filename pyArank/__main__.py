# Arank - UserBot
# Copyright (C) 2021-2022 Mr_Mrs_Krishna
#
# This file is a part of < https://github.com/CoderXKrishna/Arank/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/CoderXKrishna/pyArank/blob/main/LICENSE>.

from . import *


def main():
    import os
    import sys
    import time

    from .functions.helper import time_formatter, updater
    from .startup.funcs import (
        WasItRestart,
        autopilot,
        customize,
        plug,
        ready,
        startup_stuff,
    )
    from .startup.loader import load_other_plugins

    # Option to Auto Update On Restarts..
    if (
        udB.get_key("UPDATE_ON_RESTART")
        and os.path.exists(".git")
        and Arank_bot.run_in_loop(updater())
    ):
        os.system(
            "git pull -f -q && pip3 install --no-cache-dir -U -q -r requirements.txt"
        )

        os.execl(sys.executable, "python3", "-m", "pyArank")

    startup_stuff()

    Arank_bot.me.phone = None
    Arank_bot.first_name = Arank_bot.me.first_name

    if not Arank_bot.me.bot:
        udB.set_key("OWNER_ID", Arank_bot.uid)

    LOGS.info("Initialising...")

    Arank_bot.run_in_loop(autopilot())

    pmbot = udB.get_key("PMBOT")
    manager = udB.get_key("MANAGER")
    addons = udB.get_key("ADDONS") or Var.ADDONS
    vcbot = udB.get_key("VCBOT") or Var.VCBOT
    if HOSTED_ON == "okteto":
        vcbot = False

    if HOSTED_ON == "termux" and udB.get_key("EXCLUDE_OFFICIAL") is None:
        _plugins = "autocorrect autopic compressor forcesubscribe gdrive glitch instagram nsfwfilter nightmode pdftools writer youtube"
        udB.set_key("EXCLUDE_OFFICIAL", _plugins)

    load_other_plugins(addons=addons, pmbot=pmbot, manager=manager, vcbot=vcbot)

    suc_msg = """
            ----------------------------------------------------------------------
                Arank has been deployed! Visit @Carding_Chronicle for updates!!
            ----------------------------------------------------------------------
    """

    # for channel plugins
    plugin_channels = udB.get_key("PLUGIN_CHANNEL")

    # Customize Arank Assistant...
    Arank_bot.run_in_loop(customize())

    # Load Addons from Plugin Channels.
    if plugin_channels:
        Arank_bot.run_in_loop(plug(plugin_channels))

    # Send/Ignore Deploy Message..
    if not udB.get_key("LOG_OFF"):
        Arank_bot.run_in_loop(ready())

    # Edit Restarting Message (if It's restarting)
    Arank_bot.run_in_loop(WasItRestart(udB))

    try:
        cleanup_cache()
    except BaseException:
        pass

    LOGS.info(
        f"Took {time_formatter((time.time() - start_time)*1000)} to start •Arank•"
    )
    LOGS.info(suc_msg)


if __name__ == "__main__":
    main()

    asst.run()
