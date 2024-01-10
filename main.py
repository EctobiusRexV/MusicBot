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

    @bot.command(name = 'pause')
    async def pause(ctx):
        await ctx.send('Pausing...')

    @bot.command(name = 'resume')
    async def resume(ctx):
        await ctx.send('Resuming...')

    @bot.command(name = 'skip')
    async def skip(ctx):
        await ctx.send('Skipping...')

    @bot.command(name = 'queue')
    async def queue(ctx):
        await ctx.send('Queueing...')

    @bot.command(name = 'join')
    async def join(ctx):
        await ctx.send('Joining voice channel...')

    @bot.command(name = 'leave')
    async def leave(ctx):
        await ctx.send('Leaving voice channel...')

    @bot.command(name = 'help')
    async def help(ctx):
        await ctx.send('')
    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')

    bot.run(settings.discord_token)


if __name__ == '__main__':
    run()