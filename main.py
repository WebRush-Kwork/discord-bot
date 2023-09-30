import discord
import os
from discord.ext import commands
from bot_token import bot_token
from model import get_classes

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def check_image(ctx):
    if len(ctx.message.attachments) > 0:
        if not os.path.exists('images'):
            os.makedirs('images')
        for attachment in ctx.message.attachments:
            image_filename = attachment.filename
            await attachment.save(f'images/{image_filename}')
            await ctx.send(f'Изображение успешно сохранено как {image_filename}')
            await ctx.send(get_classes(f'images/{image_filename}'))
    else:
        await ctx.send('Изображение не найдено, прикрепите изображение и повторите попытку')

bot.run(bot_token)
