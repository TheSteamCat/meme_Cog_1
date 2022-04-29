from redbot.core import commands


class MegaCog(commands.Cog):
    """This is a package of my first tests"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def baked(self, ctx):
        """soon, he will be baked"""
        await ctx.send("https://cdn.discordapp.com/attachments/381591651145220101/966509608329936966/unknown.png")
    
    @commands.command()
    async def troll(self, ctx):
        """we do a miniscule amount of trolling"""
        await ctx.send("https://i.imgur.com/cYCXzU0.png")

    @commands.command()
    async def embedFail(self, ctx):
        """embed failure, laugh at this user"""
        await ctx.send("https://tenor.com/view/epic-embed-fail-star-citizen-embed-fail-star-citizen-epic-embed-fail-star-citizen-ballista-gif-21467633")

    @commands.command()
    async def ratStare(self, ctx):
        """she watchin"""
        await ctx.send("https://cdn.discordapp.com/attachments/950399917304729651/969125925595779082/nynturn-1.gif")

    @commands.command()
    async def duck(self, ctx):
        """For when you feel like quacking up!"""
        await ctx.send("Quack!")
    
    @commands.command()
    async def balls(self, ctx):
        """cock"""
        await ctx.send("balls")

    @commands.command()
    async def embedFailLonger(self, ctx):
        """for particularly bad embed fails"""
        await ctx.send("https://tenor.com/view/epic-embed-fail-embed-fail-embed-discord-embed-gif-embed-gif-21924703")
    
    @commands.command()
    async def skillIssue(self, ctx):
        """skill issue"""
        await ctx.send("https://tenor.com/view/doge-difference-in-skill-meme-dog-gif-22631267")