from nextcord.ext import commands
import random

TORN_GUILD_ID = 963172420963938325

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_message(message):
    print("I'm Ready!!!!!")

@bot.slash_command(description="Random Number Picker", guild_ids=[TORN_GUILD_ID])
async def randonumber(interaction: nextcord.Interaction):
    number = random.choice(1, 10)
    await interaction.send(f"{number}")

@bot.slash_command(description="Trade Receipt Storing System", guild_ids[TORN_GUILD_ID])
async def tradelog(interaction: nextcord.Interaction, id=None, message=None):
    #database connection
    for x in message:

@bot.slash_command(description="Item Price Lookup", guild_ids=[TORN_GUILD_ID])
async def price(interaction: nextcord.Interaction, item_name=None, optional: item_id=None):


bot.run('qeDR3fcptraQWQi5Z9gCg27wndSAhnnN')