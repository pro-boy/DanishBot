"""CC- @refundisillegal\nSyntax:-\n.get var NAME\n.del var NAME\n.set var NAME"""

# Copyright (C) 2020 Adek Maulana.
# All rights reserved.
"""
   Heroku manager for your userbot
"""

import heroku3
import asyncio
import os
import requests
import math
from userbot.events import register
from userbot.utils import admin_cmd
from userbot import CMD_HELP
from userbot.uniborgConfig import Config

# ================= 

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY

Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"


@borg.on(admin_cmd(pattern="(set|get|del) var(?: |$)(.*)(?: |$)([\s\S]*)", outgoing=True))
async def variable(var):
    """
        Manage most of ConfigVars setting, set new var, get current var,
        or delete var...
    """
    if Var.HEROKU_APP_NAME is not None:
        app = Heroku.app(Var.HEROKU_APP_NAME)
    else:
        return await var.edit("`[HEROKU]:"
                              "\nPlease setup your` **HEROKU_APP_NAME**")
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        await var.edit("`Getting information...`")
        await asyncio.sleep(1)
        try:
            variable = var.pattern_match.group(2).split()[0]
            if variable in heroku_var:
                return await var.edit("**ConfigVars**:"
                                      f"\n\n`{variable} = {heroku_var[variable]}`\n")
            else:
                return await var.edit("**ConfigVars**:"
                                      f"\n\n`Error:\n-> {variable} don't exists`")
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await var.client.send_file(
                        var.chat_id,
                        "configs.json",
                        reply_to=var.id,
                        caption="`Output too large, sending it as a file`",
                    )
                else:
                    await var.edit("`[HEROKU]` ConfigVars:\n\n"
                                   "================================"
                                   f"\n```{result}```\n"
                                   "================================"
                                   )
            os.remove("configs.json")
            return
    elif exe == "set":
        await var.edit("`Setting information...weit ser`")
        variable = var.pattern_match.group(2)
        if not variable:
            return await var.edit(">`.set var <ConfigVars-name> <value>`")
        value = var.pattern_match.group(3)
        if not value:
            variable = variable.split()[0]
            try:
                value = var.pattern_match.group(2).split()[1]
            except IndexError:
                return await var.edit(">`.set var <ConfigVars-name> <value>`")
        await asyncio.sleep(1)
        if variable in heroku_var:
            await var.edit(f"**{variable}**  `successfully changed to`  ->  **{value}**")
        else:
            await var.edit(f"**{variable}**  `successfully added with value`  ->  **{value}**")
        heroku_var[variable] = value
    elif exe == "del":
        await var.edit("`Getting information to deleting variable...`")
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await var.edit("`Please specify ConfigVars you want to delete`")
        await asyncio.sleep(1)
        if variable in heroku_var:
            await var.edit(f"**{variable}**  `successfully deleted`")
            del heroku_var[variable]
        else:
            return await var.edit(f"**{variable}**  `is not exists`")

@register(outgoing=True, pattern="^\!shutdown$")

async def _(dyno):        

        try:

             Heroku = heroku3.from_key(HEROKU_API_KEY)                         

             app = Heroku.app(HEROKU_APP_NAME)

        except:

  	       return await dyno.reply(" `Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var` please check https://telegra.ph/RkPavi-06-09-6")

        app.scale_formation_process("worker", 0)

        text = f"`Turning Off Dynos` "

        sleep = 1

        dot = "."

        while (sleep <= 3):

            await dyno.edit(text + f"`{dot}`")

            await asyncio.sleep(1)

            dot += "."

            sleep += 1

        await dyno.respond(f"turned off...`")

        return await dyno.delete()

@register(outgoing=True, pattern="^\!restart$")

async def _(dyno):        

        try:

             Heroku = heroku3.from_key(HEROKU_API_KEY)                         

             app = Heroku.app(HEROKU_APP_NAME)

        except:

  	       return await dyno.reply(" `Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var` please check https://telegra.ph/RkPavi-06-09-6")

        try:           

            Dyno = app.dynos()[0]

        except IndexError:

            return await dyno.respond(f"**{HEROKU_APP_NAME}** `is not on...`")

        else:

            text = f"`Restarted Dynos....`"

            Dyno.restart()

            sleep = 1

            dot = "."

            await dyno.edit(text)

            while (sleep <= 24):

                await dyno.edit(text + f"`{dot}`")

                await asyncio.sleep(1)

                if len(dot) == 3:

                    dot = "."

                else:

                    dot += "."

                sleep += 1

            state = Dyno.state

            if state == "up":

                await dyno.respond(f"**{HEROKU_APP_NAME}** `restarted...`")

            elif state == "crashed":

                await dyno.respond(f"**{HEROKU_APP_NAME}** `crashed...`")

            return await dyno.delete()

            


@borg.on(admin_cmd(pattern="usage(?: |$)", outgoing=True))
async def dyno_usage(dyno):
    """
        Get your account Dyno Usage
    """
    await dyno.edit("`Processing...`")
    useragent = ('Mozilla/5.0 (Linux; Android 10; SM-G975F) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/80.0.3987.149 Mobile Safari/537.36'
                 )
    user_id = Heroku.account().id
    headers = {
     'User-Agent': useragent,
     'Authorization': f'Bearer {Var.HEROKU_API_KEY}',
     'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("`Error: something bad happened`\n\n"
                               f">.`{r.reason}`\n")
    result = r.json()
    quota = result['account_quota']
    quota_used = result['quota_used']

    """ - Used - """
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)

    """ - Current - """
    App = result['apps']
    try:
        App[0]['quota_used']
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]['quota_used'] / 60
        AppPercentage = math.floor(App[0]['quota_used'] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)

    await asyncio.sleep(1)

    return await dyno.edit("**Dyno Usage**:\n\n"
                           f" -> `Dyno usage for`  **{Var.HEROKU_APP_NAME}**:\n"
                           f"     •  `{AppHours}`**h**  `{AppMinutes}`**m**  "
                           f"**|**  [`{AppPercentage}`**%**]"
                           "\n\n"
                           " -> `Dyno hours quota remaining this month`:\n"
                           f"     •  `{hours}`**h**  `{minutes}`**m**  "
                           f"**|**  [`{percentage}`**%**]"
                           )

@borg.on(admin_cmd(pattern="logs$", outgoing=True))
async def _(dyno):        
        try:
             Heroku = heroku3.from_key(HEROKU_API_KEY)                         
             app = Heroku.app(HEROKU_APP_NAME)
        except:
  	       return await dyno.reply(" Please make sure your Heroku API Key, Your App name are configured correctly in the heroku")
        await dyno.edit("Getting Logs....")
        with open('logs.txt', 'w') as log:
            log.write(app.get_log())
        await dyno.edit("Got the logs wait a sec")    
        await dyno.client.send_file(
            dyno.chat_id,
            "logs.txt",
            reply_to=dyno.id,
            caption="logs of 100+ lines",
        )
        
        await asyncio.sleep(5)
        await dyno.delete()
        return os.remove('logs.txt')
    
def prettyjson(obj, indent=2, maxlinelength=80):
    """Renders JSON content with indentation and line splits/concatenations to fit maxlinelength.
    Only dicts, lists and basic types are supported"""

    items, _ = getsubitems(obj, itemkey="", islast=True, maxlinelength=maxlinelength - indent, indent=indent)
    return indentitems(items, indent, level=0)

@borg.on(admin_cmd(pattern=r"send (?P<shortname>\w+)$", outgoing=True))
async def send(event):
    if event.fwd_from:
        return
    reply_to_id = None
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    input_str = event.pattern_match["shortname"]
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        start = datetime.now()
        plug = await event.client.send_file(  # pylint:disable=E0602
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            thumb=thumb,
        )
        end = datetime.now()
        ms = (end - start).seconds
        await event.delete()
        await plug.edit(
            f"__**➥ Plugin Name:- {input_str} .**__\n__**➥ Uploaded in {ms} seconds.**__\n__**➥ Uploaded by :-**__ {DEFAULTUSER}"
        )
    else:
        await edit_or_reply(event, "404: File Not Found")



CMD_HELP.update({
  "heroku":
  "Info for Module to Manage Heroku:**\n\n`.usage`\nUsage:__Check your heroku dyno hours status.__\n\n`.set var <NEW VAR> <VALUE>`\nUsage: __add new variable or update existing value variable__\n**!!! WARNING !!!, after setting a variable the bot will restart.**\n\n`.get var or .get var <VAR>`\nUsage: __get your existing varibles, use it only on your private group!__\n**This returns all of your private information, please be cautious...**\n\n`.del var <VAR>`\nUsage: __delete existing variable__\n**!!! WARNING !!!, after deleting variable the bot will restarted**\n\n`.herokulogs`\nUsage:sends you recent 100 lines of logs in heroku"
})    
