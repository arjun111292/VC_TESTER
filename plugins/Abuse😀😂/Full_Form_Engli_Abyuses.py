#created by by @Arjun_La_Lis_A - tg
#use with proper credits

import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.neededshits.cust_p_filters import f_onw_fliter


THEABUSE_STRINGS = (
    "Shut your mouth, U Fucking Bitch",
    "Keep it in your Ass Hole",
    "Keep your tiny dick Safe in dyper..",
    "Fuck you Ass Hole",
    "Whatsup Mother F#cker..",
    "Kiss Me, Klose Yuvar Eyes And Fck Me..",
    "The Whole Country Is Just A Bo#ty Garden",
    "Come lick my pu##y",
    "Dont c#m on your bed",
    "East or west?, F#ck is the best",
    "Monkey - I Found A Dragon, Hooman - I Fried A Dragon, Dragon - I Loved A Dragon, Horse - I kIssed A Dragon, DONKEY - I F#cked A Dragon",
    "Wrap Me In PLastic And F#Ck Me Hard",
    "F*ck you",
    "u are getting an award for being the best D#ck head of 2022",
    "Son of a b*tch, F*kcked like an ostrich..",
    "I thing u are a perfect Wa#ker",
    "C*nt",
    "U r the only Scu%bag i know",
)


@Client.on_message(
    filters.command("englishabuses", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def englishabuses(_, message):
    """ /englishabuses strings """
    effective_string = random.choice(THEABUSE)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
