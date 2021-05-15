import discord
from discord.ext import commands
from discord.utils import get

TOKEN = #TOKEN

bot = commands.Bot(command_prefix = "hoy ")

# ===================== BASIC COMMANDS ================ #
@bot.event
async def on_ready():
	print("Ready!")

@bot.command()
async def babsify(ctx):
	await ctx.send("Pakyo!")

@bot.command()
async def grr(ctx):
    await ctx.send("grr")

@bot.command()
async def simp(ctx):
    await ctx.send("fcking simp")

@bot.command()
async def sadboi(ctx):
    await ctx.send("tanginang sadboi")

@bot.command(aliases=['unsa_imo_ikasulti'])
async def sure_baps(ctx):
    await ctx.send("edi wow")

@bot.command()
async def bye(ctx):
    await ctx.send("bye fcker")

@bot.command()
async def salamat(ctx):
    await ctx.send("salamat badi")

@bot.command()
async def appreciate(ctx):
    await ctx.send("thanks boang")

@bot.command(aliases=['plus'])
async def add(ctx, a: float, b: float):
	await ctx.send("ang answer kay:")
	await ctx.send(a+b)

@bot.command()
async def remove(ctx, amount = 2):
	await ctx.channel.purge(limit = amount)


bot.run(TOKEN)
