import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="=", intents=discord.Intents.all())
oil_coins = {}

client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord. Activity(type=discord.ActivityType.listening, name='eagle screeches!'))
    print(f'We have logged in as {client.user}')
    for guild in client.guilds:
        for member in guild.members:
            oil_coins[member.id] = 500




@client.event
async def on_message(message):
    i = 0
    await client.process_commands(message)
    
    if message.author == client.user:
        return

    if "oil" in message.content.lower():
        await message.channel.send(f'OIL UP! {message.author.mention} :oil:')
    if "freedom" in message.content.lower():
        await message.channel.send('DID SOMEBODY SAY FREEDOM!')
    if "democracy" in message.content.lower():
        await message.channel.send('I think we have to resort to democracy.')
    if "knock knock" in message.content.lower():
        await message.channel.send('KNOCK KNOCK MOTHERFUCKERS THIS IS THE UNITED STATES OF AMERICA AND IVE HEARD YOU HAVE OIL WHICH ISNT IN OUR POSSESION, SO NOW TURN OFF THE STOVE AND RETURN THE OIL, OR ELSE WE HAVE TO RESORT TO DEMOCRACY! :eagle: :flag_us: :eagle: :flag_us: :eagle: :flag_us: :eagle: :flag_us: :eagle: :flag_us: :eagle: :flag_us: :eagle: :flag_us: *eagle screeches and gunshots*')
    if "america ya" in message.content.lower():
        while i < 5:                                                    
            await message.channel.send('HALLO :D *slight gunshots in the background*')
            i += 1
    if "informatik ya" in message.content.lower():
        while i < 10:
            await message.channel.send('YAP')
            i += 1
    if "martin ya" in message.content.lower():
        await message.channel.send('IDEAr')
        await message.channel.send('SHHHHHHHHHHHedule')
        await message.channel.send('i might have to invade for some oil!')
        await message.channel.send('learning = studying')
        await message.channel.send('yap')
        await message.channel.send('stoned when you are high on drags.')
        await message.channel.send('olreight')
        await message.channel.send('write AN good essay')
    if "polska ya" in message.content.lower():
        while i < 5:
            await message.channel.send('KURWA BOBER YA! :flag_pl:')
            await message.channel.send('POLSKA GUROM YA! :flag_pl:')
            i += 1
    if "afghanistan ya" in message.content.lower():
        while i < 10: 
            await message.channel.send('KABOOM :boom:')
            i += 1
    if "kevin" in message.content.lower():
        await message.channel.send('Never gonna give you up, never gonna let you down, never gonna run around here, to search you. Never gonna make you cry, never gonna say goodbye.')       
    if "liberty" in message.content.lower():
        await message.channel.send('how about a nice cup of LIBER-TEA!')


specific_user_id = 551168048183377940

@client.command()
async def help(ctx):
    documentation_link = "You can find the entire **Freedom Bot** Documentation by clicking the following link! https://docs.google.com/document/d/1F784zT8Q2FblQ-5xssbVXEHRvp_uBXHXViz1kZUU0EE"
    await ctx.send(documentation_link)

@client.command()
async def robby(ctx):
    user = client.get_user(specific_user_id)
    if user:
        await ctx.send(f"OIL UP! <@{user.id}> :oil:")
    else:
        await ctx.send("User not found.")

@client.command(aliases=['quote', 'Quote', 'qUote', 'quOte', 'quoTe', 'quotE', 'QUote', 'qUOte', 'quOTe', 'quoTE', 'QUOte', 'qUOTe', 'quOTE', 'QUOTe', 'qUOTE', 'QUOTE', 'kwote'])
async def randomquote(ctx, *, question=None):
        if question is None:
            with open('C:/Users/Sestik/Desktop/PythonProjects/FreedomBot/quotes.txt', 'r', encoding='utf-8') as f:
                random_responses = f.readlines()
                response = random.choice(random_responses)
            
            await ctx.send(response)

@client.command()
async def gamble(ctx, amount: int):
    # Check if user has enough freedom credits to gamble
    if amount <= 0 or amount > oil_coins.get(ctx.author.id, 0):
        await ctx.send("brokey you don't have that many OIL COINS")
        return
    # Simulate gambling with a 50/50 chance
    win = random.choice([True, False])

    if win:
        win_amount = amount * 2 - amount
        await ctx.send(f"congrats fam you won {win_amount} OIL COINS!")
    else:
        await ctx.send("womp womp get good kid")

    # Update user's freedom credits
    oil_coins[ctx.author.id] -= amount if not win else -win_amount

@client.command(aliases=['credits'])
async def check_credits(ctx):
    coins = oil_coins.get(ctx.author.id, 0)
    if coins > 0:
        await ctx.send(f"You are in possesion of {coins} OIL COINS!")
    else:
        await ctx.send(f"You're literally broke no money womp womp get good kid.")


SPECIFIC_USER_ID2 = 540843411784204289

@client.command()
async def grant_credits(ctx, member: discord.Member, amount: int):
    # Check if the user invoking the command matches the specific user ID
    if ctx.author.id != SPECIFIC_USER_ID2:
        await ctx.send("keine rechte")
        return
    
    # Grant credits to the specified user
    if member.id not in oil_coins:
        oil_coins[member.id] = amount
    else:
        oil_coins[member.id] += amount
    
    await ctx.send(f"{amount} freedom creditos given to --> {member.mention}.")

@client.command()
async def play_audio(ctx, file_name):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        await ctx.send("kurwa u have to be in voice channel for this command to work")
        return
    
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        vc = await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)
        vc = ctx.voice_client
    
    # Check if the bot is already playing something
    if vc.is_playing():
        vc.stop()
    
    # Load and play the audio file
    source = discord.FFmpegPCMAudio(file_name)
    vc.play(source)

@client.command()
async def leave(ctx):
    # Check if the bot is connected to a voice channel
    if ctx.voice_client is not None:
        # Disconnect the bot from the voice channel
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I am not connected to a voice channel.")

@client.command(aliases=['eagle'])
async def play(ctx):
    await play_audio(ctx, 'usa.mp3')

@client.command()
async def kilometer(ctx):
    await play_audio(ctx, 'kilometer.mp3')

@client.command()
async def slavery(ctx):
    await play_audio(ctx, 'slavery.mp3')

# client.run('sike, you thought :)')
