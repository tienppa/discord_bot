import discord
from discord.ext import commands
import config
from utils import wakeup_scheduler
from utils import telegram_scheduler
from cogs.greetings import GreetingsCog
from cogs.birthday import BirthdayCog
from cogs.quotes import QuotesCog 

intents = discord.Intents.default()
intents.members = True
intents.presences = True 
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Load cogs
bot.add_cog(GreetingsCog(bot))
bot.add_cog(BirthdayCog(bot))
bot.add_cog(QuotesCog(bot))

@bot.event
async def on_ready():
    await bot.sync_commands()
    
    print(f'{bot.user} has connected to Discord!')

wakeup_scheduler.schedule_wakeup_task(bot, config.CHANNEL_ID)  
telegram_scheduler.schedule_telegram_task(bot, config.TELEGRAM_BOT_TOKEN, config.TELEGRAM_CHAT_ID)

bot.run(config.DISCORD_TOKEN)
