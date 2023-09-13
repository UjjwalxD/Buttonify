import discord 
from discord.ext import commands



custom_styles = {
    "red_button": discord.ButtonStyle.red,
    "green_button": discord.ButtonStyle.green,
    "primary_button": discord.ButtonStyle.primary,
    "secondary_button": discord.ButtonStyle.secondary
}

def Buttonify(label, emoji, disabled=False, style=None):
    view = discord.ui.View()
    if style and style in custom_styles:
        button_style = custom_styles[style]
    else:
        button_style = discord.ButtonStyle.red  
    button = discord.ui.Button(label=label, style=button_style, emoji=emoji, disabled=disabled)
    view.add_item(button)
    return view
