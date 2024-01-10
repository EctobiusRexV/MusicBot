import discord
from discord.ext import commands
import settings
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests


def run():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix = '!', intents = intents)
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=settings.spotify_client_id,
                                                   client_secret=settings.spotify_client_secret,
                                                   redirect_uri="http://localhost:8080",
                                                   scope="user-read-currently-playing"))

    @bot.command(name = 'play')
    async def play(ctx, *url):
        try:
            voiceChannel = ctx.author.voice.channel
            voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
            if voice == None:
                await voiceChannel.connect()
                await ctx.send(f"Joined **{voiceChannel}**")
            elif voice.channel != voiceChannel:
                await voice.move_to(voiceChannel)
                await ctx.send(f"Joined **{voiceChannel}**")
        except AttributeError:
            await ctx.send("You're not in a VC")

        song = ' '.join(word for word in url)

        results = sp.search(q=song, type='track', limit=1)

        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            song = results['tracks']['items'][0]['name']
            artist = results['tracks']['items'][0]['artists'][0]['name']
            track_uri = track['uri']
            await ctx.send(f"Playing **{song}** by **{artist}**")
            sp.start_playback(uris=[track_uri])

        # await ctx.send('Playing ' + song + '...')

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
        await ctx.send('Queue:')

    @bot.command(name = 'join')
    async def join(ctx):
        try:
            voiceChannel = ctx.author.voice.channel
            voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
            if voice == None:
                await voiceChannel.connect()
                await ctx.send(f"Joined **{voiceChannel}**")
            elif voice.channel != voiceChannel:
                await voice.move_to(voiceChannel)
                await ctx.send(f"Joined **{voiceChannel}**")
            else:
                await ctx.send("I'm already in a VC")
                print(voice.channel)
        except AttributeError:
            await ctx.send("You're not in a VC")

    @bot.command(name = 'leave')
    async def leave(ctx):
        await ctx.send('Leaving voice channel...')
        await ctx.voice_client.disconnect()
    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')

    bot.run(settings.discord_token)


if __name__ == '__main__':
    run()