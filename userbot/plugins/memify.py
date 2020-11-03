# Copyright (C) 2020 MoveAngel and MinaProject
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Multifunction memes
#
# Based code + improve from AdekMaulana and aidilaryanto

import asyncio
from asyncio.exceptions import TimeoutError
import re
import random
from telethon import events
import os
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import (MessageMediaPhoto)
from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.events import register


THUMB_IMAGE_PATH = "./thumb_image.jpg"

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+")


@register(outgoing=True, pattern="^.edt(?: |$)(.*)")
async def mim(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Syntax: reply to an image with .mmf` 'text on top' ; 'text on bottom' ")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("```reply to a image/sticker/gif```")
        return
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    else:
        await event.edit("```Transfiguration Time! Mwahaha Memifying this image! (」ﾟﾛﾟ)｣ ```")
        await asyncio.sleep(5)

    try:
        async with bot.conversation("@MemeAutobot") as bot_conv:
            chat = "@MemeAutobot"
            try:
                memeVar = event.pattern_match.group(1)
                await silently_send_message(bot_conv, "/start")
                await asyncio.sleep(1)
                await silently_send_message(bot_conv, memeVar)
                await bot.send_file(chat, reply_message.media)
                response = await bot_conv.get_response()
            except YouBlockedUserError:
                await event.reply("```Please unblock @MemeAutobot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good, Nibba?```")
            if "Okay..." in response.text:
                await event.edit("```🛑 🤨 NANI?! This is not an image! This will take sum tym to convert to image... UwU 🧐 🛑```")
                thumb = None
                if os.path.exists(THUMB_IMAGE_PATH):
                    thumb = THUMB_IMAGE_PATH
                input_str = event.pattern_match.group(1)
                if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
                    os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
                if event.reply_to_msg_id:
                    file_name = "meme.png"
                    reply_message = await event.get_reply_message()
                    to_download_directory = TEMP_DOWNLOAD_DIRECTORY
                    downloaded_file_name = os.path.join(
                        to_download_directory, file_name)
                    downloaded_file_name = await bot.download_media(
                        reply_message,
                        downloaded_file_name,
                    )
                    if os.path.exists(downloaded_file_name):
                        await bot.send_file(
                            chat,
                            downloaded_file_name,
                            force_document=False,
                            supports_streaming=False,
                            allow_cache=False,
                            thumb=thumb,
                        )
                        os.remove(downloaded_file_name)
                    else:
                        await event.edit("File Not Found {}".format(input_str))
                response = await bot_conv.get_response()
                the_download_directory = TEMP_DOWNLOAD_DIRECTORY
                files_name = "memes.webp"
                download_file_name = os.path.join(
                    the_download_directory, files_name)
                await bot.download_media(
                    response.media,
                    download_file_name,
                )
                requires_file_name = TEMP_DOWNLOAD_DIRECTORY + "memes.webp"
                await bot.send_file(  # pylint:disable=E0602
                    event.chat_id,
                    requires_file_name,
                    supports_streaming=False,
                    caption="Memifyed",
                )
                await event.delete()
                # await bot.send_message(event.chat_id, "`☠️☠️Ah Shit... Here we go
                # Again!🔥🔥`")
            elif not is_message_image(reply_message):
                await event.edit("Invalid message type. Plz choose right message type u NIBBA.")
                return
            else:
                await bot.send_file(event.chat_id, response.media)
    except TimeoutError:
        await event.edit("`Error: `@MemeAutobot` is not responding!.`")


def is_message_image(message):
    if message.media:
        if isinstance(message.media, MessageMediaPhoto):
            return True
        return bool(
            message.media.document
            and message.media.document.mime_type.split("/")[0] == "image"
        )

    return False


async def silently_send_message(conv, text):
    await conv.send_message(text)
    response = await conv.get_response()
    await conv.mark_read(message=response)
    return response




@register(outgoing=True, pattern=r'^.hz(:? |$)(.*)?')
async def hazz(hazmat):
    await hazmat.edit("`Sending information...`")
    level = hazmat.pattern_match.group(2)
    if hazmat.fwd_from:
        return
    if not hazmat.reply_to_msg_id:
        await hazmat.edit("`WoWoWo Capt!, we are not going suit a ghost!...`")
        return
    reply_message = await hazmat.get_reply_message()
    if not reply_message.media:
        await hazmat.edit("`Word can destroy anything Capt!...`")
        return
    if reply_message.sender.bot:
        await hazmat.edit("`Reply to actual user...`")
        return
    chat = "@hazmat_suit_bot"
    await hazmat.edit("```Suit Up Capt!, We are going to purge some virus...```")
    message_id_to_reply = hazmat.message.reply_to_msg_id
    msg_reply = None
    async with hazmat.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(reply_message)
            if level:
                m = f"/hazmat {level}"
                msg_reply = await conv.send_message(
                    m,
                    reply_to=msg.id)
                r = await conv.get_response()
                response = await conv.get_response()
            elif reply_message.gif:
                m = "/hazmat"
                msg_reply = await conv.send_message(
                    m,
                    reply_to=msg.id)
                r = await conv.get_response()
                response = await conv.get_response()
            else:
                response = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await hazmat.reply("`Please unblock` @hazmat_suit_bot`...`")
            return
        if response.text.startswith("I can't"):
            await hazmat.edit("`Can't handle this GIF...`")
            await hazmat.client.delete_messages(
                conv.chat_id,
                [msg.id, response.id, r.id, msg_reply.id])
            return
        else:
            downloaded_file_name = await hazmat.client.download_media(
                response.media,
                TEMP_DOWNLOAD_DIRECTORY
            )
            await hazmat.client.send_file(
                hazmat.chat_id,
                downloaded_file_name,
                force_document=False,
                reply_to=message_id_to_reply
            )
            """ - cleanup chat after completed - """
            if msg_reply is not None:
                await hazmat.client.delete_messages(
                    conv.chat_id,
                    [msg.id, msg_reply.id, r.id, response.id])
            else:
                await hazmat.client.delete_messages(conv.chat_id,
                                                    [msg.id, response.id])
    await hazmat.delete()
    return os.remove(downloaded_file_name)





@register(outgoing=True, pattern="^.waifu(?: |$)(.*)")
async def waifu(animu):
    text = animu.pattern_match.group(1)
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            await animu.answer("`No text given, hence the waifu ran away.`")
            return
    animus = [20, 32, 33, 40, 41, 42, 58]
    sticcers = await bot.inline_query(
        "stickerizerbot", f"#{random.choice(animus)}{(deEmojify(text))}")
    await sticcers[0].click(animu.chat_id,
                            reply_to=animu.reply_to_msg_id,
                            silent=bool(animu.is_reply),
                            hide_via=True)
    await animu.delete()


def deEmojify(inputString: str) -> str:
    return re.sub(EMOJI_PATTERN, '', inputString)


CMD_HELP.update({
    "memify":
    ".mmf <text_top> ; <textbottom>"
    "\nUsage: Reply a sticker/image/gif and send with cmd."
})

CMD_HELP.update({
    "hazmat":
    ".hz or .hz [flip, x2, rotate (degree), background (number), black]"
    "\nUsage: Reply to a image / sticker to suit up!"
    "\n@hazmat_suit_bot"
})



CMD_HELP.update({
    "waifu":
    ".waifu"
    "\nUsage: Enchance your text with beautiful anime girl templates."
    "\n@StickerizerBot"
})
