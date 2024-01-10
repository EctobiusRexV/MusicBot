import discord
from discord.ext import commands
import settings


def run():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix = '!', intents = intents)

    @bot.command(name = 'play')
    async def play(ctx, url):
        await ctx.send(f'Playing {url}...')

    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')

    bot.run(settings.discord_token)

if __name__ == '__main__':
    run()