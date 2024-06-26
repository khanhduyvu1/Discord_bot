import discord
from discord.ext import commands
from info.champ_info import champion_response, champion_image, get_champion_data

class getChamp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def champ(self, ctx, *, champion_name: str):
        champion_data = get_champion_data(champion_name)

        if champion_data:
            image_embed = champion_image(champion_name)
            response_embed = champion_response(champion_name)
            image_embed.description = response_embed.description
            await ctx.send(embed=image_embed)
        else:
            await ctx.send(f"Champion '{champion_name}' not found.")
               
        
async def setup(bot):
    await bot.add_cog(getChamp(bot))