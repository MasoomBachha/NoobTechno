import random
from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "HOW CAN I PROTECT MYSELF FROM CORONAVIRUS?",
    "🧼WASH YOUR HANDS FREQUENTLY",
    "🚴‍♂️EXCERCISE AND PROPER SLEEP🛌 WILL BOLSTER THE IMMUNE SYSTEM",
    "🛀MAINTAIN GOOD HYGIENE HABHITS AT ALL TIMES",
    "👬AVOID CONTACT WITH OTHERS",
    "😷WEAR A FACE MASK WHEN DEALING WITH INFECTED PATIENT'S",
    "🧻USE TISSUES WHEN COUGHING OR BLOWING NOSE",
    "🍎WASH AND PREPARE FOODS CAREFULLY",
    "STAY HOME STAY SAFE",
  )

@run_async
def corona(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /corona  😷.
"""

__mod_name__ = "Be SAFE FROM CORONA"

CRNA_HANDLER = DisableAbleCommandHandler("corona", corona)

dispatcher.add_handler(CRNA_HANDLER)
