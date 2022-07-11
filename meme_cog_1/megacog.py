from redbot.core import commands
import random as rand

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
    
    @commands.command()
    async def giraffe(self, ctx):
        """gives giraffe"""
        length = 4 #5
        # sends a random giraffe image
        x = rand.randint(0, length)
        # await ctx.send(x) i used this for testing the random system to make sure it works
        if x == 0:
            await ctx.send("https://images.ctfassets.net/81iqaqpfd8fy/3r4flvP8Z26WmkMwAEWEco/870554ed7577541c5f3bc04942a47b95/78745131.jpg?w=1200&h=1200&fm=jpg&fit=fill")
        elif x == 1:
            await ctx.send("https://api.time.com/wp-content/uploads/2015/09/giraffe.jpg?quality=85&w=800")
        elif x == 2:
            await ctx.send("https://worldbirds.com/wp-content/uploads/2020/05/giraffe6.jpg")
        elif x == 3: 
            await ctx.send("https://www.publicdomainpictures.net/pictures/270000/nahled/giraffe-1530247467LEm.jpg")
        elif x == 4:
            await ctx.send("https://scx2.b-cdn.net/gfx/news/hires/2022/bush-encroaching-sickl.jpg")
    
    @commands.command()
    async def beep(self, ctx):
        """I am a robot!"""
        await ctx.send("boop")
    
    @commands.command()
    async def hugprice(self, ctx):
        """send help"""
        await ctx.send("https://cdn.discordapp.com/attachments/222078231040229376/970495419094286346/sUaKBaj.jpeg")
        
    @commands.command()
    async def jas(self, ctx):
        """hehehehehehehe"""
        await ctx.send("sheesh")
    
    @commands.command()
    async def a(self, ctx):
        """a"""
        await ctx.send("https://media.discordapp.net/attachments/992477336479993907/996169319518052423/755679374031847494.gif")
    
    
    
    
