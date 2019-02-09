import discord
from discord.ext import commands
from cogs.cogfuncs import prawImage
from cogs.cogfuncs import prawCredentials

class Dankmeme:
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def dankmeme(self):
        textReturn = await prawImage.prawImgFind(prawCredentials)
        if textReturn == 1:
            textReturn = "`Invalid subreddit!`"
        elif textReturn == 2:
            textReturn = "`No images could be found.`"
        await self.client.say(textReturn)


def setup(client):
    client.add_cog(Dankmeme(client))