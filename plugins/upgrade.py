"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 30  🇮🇳  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 40  🇮🇳  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 60 🇮🇳 per Month
	
	
	Pay Using Upi I'd ```sunrisesharsha467@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin @SUNRISES_24"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/SUNRISES_24")], 
        			[InlineKeyboardButton("SUPPORT 💖",url = "https://t.me/SH24_AdminBot"),
        			InlineKeyboardButton("Paytm",url = "https://paytm.com/")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 30  🇮🇳  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 40  🇮🇳  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 60  🇮🇳  per Month
	
	
	Pay Using Upi I'd ```sunrisesharsha467@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin @SUNRISES_24"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/SUNRISES_24")], 
        			[InlineKeyboardButton("SUPPORT 💖",url = "https://t.me/SH24_AdminBot"),
        			InlineKeyboardButton("Paytm",url = "https://paytm.com/")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
