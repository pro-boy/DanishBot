import asyncio
import os
import sys
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot.helpers import catmemes


R = (
    "██╗░░██╗██╗\n"
    "██║░░██║██║\n"
    "███████║██║\n"
    "██╔══██║██║\n"
    "██║░░██║██║\n"
    "╚═╝░░╚═╝╚═╝\n"
)

S = (
    "..... (¯`v´¯)♥️\n"
    ".......•.¸.•´\n"
    "....¸.•´  🅷🅸\n"
    "... (   BABYy\n"
    "☻/ \n"
    "/▌✿🌷✿\n"
    "/ \     \|/\n"
)


U = (
    "🌙.     *       ☄️      \n"
    "🌟   .  *       .         \n"
    "                       *   .      🛰     .        ✨      *\n"
    "  .     *   SLEEP WELL        🚀     \n"
    "      .              . . SWEET DREAMS 🌙\n"
    ". *       🌏 GOOD NIGHT         *\n"
    "                     🌙.     *       ☄️      \n"
    "🌟   .  *       .         \n"
    "                       *   .      🛰     .        ✨      *\n"
)

V = (
    "▃▃▃▃▃▃▃▃▃▃▃\n"
    "┊ ┊ ┊ ┊ ┊ ┊\n"
    "┊ ┊ ┊ ┊ ˚✩ ⋆｡˚ ✩\n"
    "┊ ┊ ┊ ✫\n"
    "┊ ┊ ✧🎂🍰🍫🍭\n"
    "┊ ┊ ✯\n"
    "┊ . ˚ ˚✩\n"
    "........♥️♥️..........♥️♥️_\n"
    ".....♥️........♥️..♥️........♥️_\n"
    "...♥️.............♥️............♥️\n"
    "......♥️.....Happy.......♥️__\n"
    "...........♥️..............♥️__\n"
    "................♥️.....♥️__\n"
    "......................♥️__\n"
    "...............♥️........♥️__\n"
    "..........♥️...............♥️__\n"
    ".......♥️..Birthday....♥️_\n"
    ".....♥️..........♥️...........♥️__\n"
    ".....♥️.......♥️_♥️.....♥️__\n"
    ".........♥️♥️........♥️♥️.....\n"
    ".............................................\n"
    "..... (¯`v´¯)♥️\n"
    ".......•.¸.•´STAY BLESSED\n"
    "....¸.•´      LOVE&FUN\n"
    "... (   YOU DESERVE\n"
    "☻/ THEM A LOT\n"
    "/▌✿🌷✿\n"
    r"/ \     \|/\n"
    "▃▃▃▃▃▃▃▃▃▃▃\n"
)

W = (
    "G🌷o🍃o🌷D\n"
    "M🍃o🌷r🍃N🌷i🍃N🌷g\n"
    "            \n"
    "No matter how good or \n"
    "bad your life is,\n"
    "wake up each morning\n"
    "and be thankful.\n"
    "You still have a new day.\n"
    "        \n"
    "🌞   \n"
    "         \n"
    "╱◥████◣\n"
    "│田│▓ ∩ │◥███◣\n"
    "╱◥◣ ◥████◣田∩田│\n"
    "│╱◥█◣║∩∩∩ 田∩田│\n"
    "║◥███◣∩田∩ 田∩田│\n"
    "│∩│ ▓ ║∩田│║▓田▓\n"
    "🌹🌷🌹🌷🌹🍃🌷🌹🌷🌹\n"
)

X = (
    ".......🦋🦋........🦋🦋\n"
    "...🦋.........🦋🦋.......🦋\n"
    "...🦋............💙..........🦋\n"
    ".....🦋🅣🅗🅐🅝🅚🅢 🦋\n"
    "....... 🦋.................🦋\n"
    "..............🦋......🦋\n"
    "...................💙\n"
)


@bot.on(admin_cmd(pattern=r"hy$"))
async def bluedevilhy(hy):
    await hy.edit(R)


@bot.on(admin_cmd(pattern=r"baby$"))
async def bluedevilbaby(baby):
    await baby.edit(S)


@bot.on(admin_cmd(pattern=r"hbd$"))
async def bluedevilhbd(hbd):
    await hbd.edit(V)


@bot.on(admin_cmd(pattern=r"thanks$"))
async def bluedeviltnk(tnk):
    await tnk.edit(X)

@bot.on(admin_cmd(pattern="gmg2$"))
async def gm(event):
    await event.edit(
        "♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n╔══╗────╔╗──────────╔╗\n║╔═╬═╦═╦╝║╔══╦═╦╦╦═╦╬╬═╦╦═╗\n║╚╗║╬║╬║╬║║║║║╬║╔╣║║║║║║║╬║\n╚══╩═╩═╩═╝╚╩╩╩═╩╝╚╩═╩╩╩═╬╗║\n────────────────────────╚═╝\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･",
    )


# by @turquoise-giggle
@bot.on(admin_cmd(pattern="gnt2$"))
async def gn(event):
    await event.edit(
        "♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n╔══╗────╔╗╔═╦╦╗─╔╗╔╗\n║╔═╬═╦═╦╝║║║║╠╬═╣╚╣╚╗\n║╚╗║╬║╬║╬║║║║║║╬║║║╔╣\n╚══╩═╩═╩═╝╚╩═╩╬╗╠╩╩═╝\n──────────────╚═╝\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･",
    )


@bot.on(admin_cmd(pattern=r"gmg3$"))
async def bluedevilgoodm(goodm):
    await goodw.edit(W)


@bot.on(admin_cmd(pattern=r"gnt3$"))
async def bluedevilgoodn(goodn):
    await goodn.edit(U)



@bot.on(admin_cmd(pattern=f"gn$", outgoing=True))
async def night(night):
    txt = random.choice(catmemes.GDNIGHT)
    await night.edit(txt)


@bot.on(admin_cmd(pattern=f"gm$", outgoing=True))
async def morning(morning):
    txt = random.choice(catmemes.GDMORNING)
    await morning.edit(txt)


@bot.on(admin_cmd(pattern="gnoon$", outgoing=True))
async def noon(noon):
    txt = random.choice(catmemes.GDNOON)
    await noon.edit(txt)


@bot.on(admin_cmd(pattern="gnt$"))
async def gn(event):
    await event.edit(
        "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･\n╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮\n╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫\n┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯\n╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥° ♥｡･ﾟ♡ﾟ･",
    )


@bot.on(admin_cmd(pattern="gmg$"))
async def gm(event):
    await event.edit(
        "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･\n╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮\n╭━┳━┳━┳╯┃╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n┣╮┣━┻━┻━╯╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･",
    )

@borg.on(admin_cmd(pattern=r"lmoon"))
async def test(event):
    if event.fwd_from:
        return 
    await event.edit("🌕🌕🌕🌕🌕🌕🌕🌕\n🌕🌕🌖🌔🌖🌔🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌖🌓🌗🌔🌕🌕\n🌕🌕🌗🌑🌑🌓🌕🌕\n🌕🌕🌗👀🌑🌓🌕🌕\n🌕🌕🌘👄🌑🌓🌕🌕\n🌕🌕🌗🌑🌑🌒🌕🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌕🌘🌑🌑🌑🌑🌒🌕\n🌖🌑🌑🌑🌑🌑🌑🌔\n🌕🤜🏻🌑🌑🌑🌑🤛🏻🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌘🌑🌑🌑🌑🌑🌑🌒\n🌕🌕🌕🌕🌕🌕🌕🌕")

@borg.on(admin_cmd(pattern=r"city"))
async def test(event):
    if event.fwd_from:
        return 
    await event.edit("""☁☁🌞      ☁           ☁
       ☁  ✈         ☁    🚁    ☁    ☁        ☁          ☁     ☁   ☁

🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/  🚘 l  🏃 \🌴 👬                       👬  🌴/            l  🚔    \🌲
      🌲/   🚖     l               \
   🌳/🚶           |   🚍         \ 🌴🚴🚴
🌴/                    |                     \🌲""")


@borg.on(admin_cmd("hi"))
async def hi(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0,5)
    giveVar = event.text
    a = giveVar[4]
    if not a:
        a = "🌺"
    b = giveVar[5]
    if not b:
        b = "✨"
    await event.edit("Hoi")
    animation_chars = [f"{a}{b}{b}{a}{b}{a}{a}{a}\n{a}{b}{b}{a}{b}{b}{a}{b}\n{a}{a}{a}{a}{b}{b}{a}{b}\n{a}{b}{b}{a}{b}{b}{a}{b}\n{a}{b}{b}{a}{b}{a}{a}{a}\n☁☁☁☁☁☁☁☁",f"{b}{a}{b}{b}{a}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{b}{b}\n{b}{a}{a}{a}{a}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}",f"{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{a}{a}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{a}{a}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{a}{a}{a}{b}{a}{a}{a}{a}{b}",f"{a}{b}{b}{a}{a}{b}{a}{a}{a}{b}{a}{b}{b}{b}{a}\n{a}{b}{a}{b}{a}{a}{b}{a}{b}{a}{a}{b}{a}{a}{a}\n{a}{b}{b}{a}{a}{a}{a}{b}{a}{a}{a}{b}{b}{a}{a}\n{a}{b}{a}{b}{a}{a}{a}{b}{a}{a}{a}{b}{a}{a}{a}\n{a}{b}{b}{a}{a}{a}{a}{b}{a}{a}{a}{b}{b}{b}{a}"]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])

@borg.on(admin_cmd(pattern=r"cheer"))
async def cheer(event):
    if event.fwd_from:
        return
    await event.edit("💐💐😉😊💐💐\n☕ Cheer Up  🍵\n🍂 ✨ )) ✨  🍂\n🍂┃ (( * ┣┓ 🍂\n🍂┃*💗 ┣┛ 🍂 \n🍂┗━━┛  🍂🎂 For YOU  🍰\n💐💐😌😚💐💐")

@borg.on(admin_cmd(pattern=r"getwell"))
async def getwell(event):
    if event.fwd_from:
        return
    await event.edit("🌹🌹🌹🌹🌹🌹🌹🌹 \n🌹😷😢😓😷😢💨🌹\n🌹💝💉🍵💊💐💝🌹\n🌹 GetBetter Soon! 🌹\n🌹🌹🌹🌹🌹🌹🌹🌹")

@borg.on(admin_cmd(pattern=r"luck"))
async def luck(event):
    if event.fwd_from:
        return
    await event.edit("💚~🍀🍀🍀🍀🍀\n🍀╔╗╔╗╔╗╦╗✨🍀\n🍀║╦║║║║║║👍🍀\n🍀╚╝╚╝╚╝╩╝。 🍀\n🍀・・ⓁⓊⒸⓀ🍀\n🍀🍀🍀 to you💚")

@borg.on(admin_cmd(pattern=r"sprinkle"))
async def sprinkle(event):
    if event.fwd_from:
        return
    await event.edit("✨.•*¨*.¸.•*¨*.¸¸.•*¨*• ƸӜƷ\n🌸🌺🌸🌺🌸🌺🌸🌺\n Sprinkled with love❤\n🌷🌻🌷🌻🌷🌻🌷🌻\n ¨*.¸.•*¨*. ¸.•*¨*.¸¸.•*¨`*•.✨\n🌹🍀🌹🍀🌹🍀🌹🍀")

@borg.on(admin_cmd("evil"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0,8)
    await event.edit("☠️EVIL IS WAKE UP...HA...HA...HA ...👽‼️👾")
    animation_chars = [
            "😈",
            "👿",
            "🎃",
            "💀",
            "👻",
            "🧟‍♀",
            "🧛",
                  ]

    for i in animation_ttl:
         
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 7])


