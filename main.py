import discord
from discord.ext import commands
import settings


def run():
    intents = discord.Intents.default()
    bot = commands.Bot(command_prefix = '!', intents = intents)
    bot.run(settings.discord_token)

    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')

if __name__ == '__main__':
    run()