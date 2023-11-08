import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f'menyimpan gambar ke ./{attachment.filename}')
            hasil = get_class('keras_model.h5', "labels.txt",f'./{attachment.filename}')
            #inference
            if hasil[0] == 'Celebrities 1' and hasil[1] >= 0.65:
                await ctx.send (f'Gambar yang kamu kirim adalah {hasil[0]}')
                await ctx.send ('Ohh actor ini ada didalam class celebrities 1')
            elif hasil[0] == 'Celebrities 2' and hasil[1] >= 0.65:
                await ctx.send(f'Gambar yang kamu kirim adalah {hasil[0]}')
                await ctx.send('Oalah, Actor termasuk didalam class celebrities 2')
            else:
                await ctx.send('GAMBAR ANDA KEMUNGKINAN: salah format/blur/corrupt')
                await ctx.send('KIRIM GAMBAR YANG BARU :D')
    else:
        await ctx.send('KAMU TIDAK MENGIRIM GAMBAR APAPUN')
bot.run("MTExMDU1MTEzNjE1MjM0MjYwOA.GPJGMq.lxy6e2SdbCNBm--uIh8VUAWu5G-JaiGrWeav9o")