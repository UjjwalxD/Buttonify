import discord 
from discord.ext import commands 
from function.buttons import Buttonify
from config import token


bot = commands.Bot(command_prefix="?", intents = discord.Intents.all())



@bot.event
async def on_ready():
    print("im ready oky")
    

# Example to use Buttonify Function:
@bot.command()
async def test(ctx):
    # Creating a custom red button with label "idk",  emoji "🚀", and disabled set to True
    red_disabled_button_view = Buttonify(label="idk", emoji="🚀", disabled=True, style="red_button")
    # Creating a custom green button with label "meow", emoji "🚀", and disabled set to False (default)
    green_button_view = Buttonify(label="meow", emoji="🚀", style="green_button")
    # Creating a custom primary (gray) button with label "hello", emoji "👋", and disabled set to False (default)
    primary_button_view = Buttonify(label="hello", emoji="👋", style="primary_button")
    # Creating a custom secondary (gray) button with label "bye", emoji "👋", and disabled set to False (default)
    secondary_button_view = Buttonify(label="bye", emoji="👋", style="secondary_button")
    await ctx.send("Here are the buttons:", view=red_disabled_button_view)
    await ctx.send("Here's another button:", view=green_button_view)
    await ctx.send("Here's a primary button:", view=primary_button_view)
    await ctx.send("Here's a secondary button:", view=secondary_button_view)
# Example ends!


bot.run(token)