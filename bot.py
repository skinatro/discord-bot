from discord.flags import MessageFlags
from duckpy import AsyncClient
import discord
import logging
import random
from discord.ext import commands
from modules.covid import covid_data
from modules.amazon import amazon_search
from modules.discord_emote import emote_convert, fallback_emote
client = commands.Bot(command_prefix='b.')
client.remove_command('help')
logging.basicConfig(level=logging.INFO)



@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.command()
async def leave(ctx):
    toleave = client.get_guild("727744472674467941")
    await to_leave.leave()
    


@client.command()
async def whois(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.blue(),
                          title="whois {}".format(member))
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Name", value=member.display_name)
    embed.add_field(name="Created Account On",
                    value=member.created_at.strftime("%a, %#d %B %Y"))
    embed.add_field(name="Joined Server On",
                    value=member.joined_at.strftime("%a, %#d %B %Y"))
    await ctx.send(embed=embed)


@client.command()
async def amazon(ctx, *search_term):
    search_term = " ".join(search_term)
    results = await amazon_search(search_term)
    names = results[0][0:5]
    prices = results[1][0:5]
    output = ""
    for name, price in zip(names, prices):
        output += f'''```diff
{name}\n+{price} INR\n
```'''
    await ctx.send(output)


@client.command()
async def ddg(ctx, *search_term):
    client = AsyncClient()
    search_term = " ".join(search_term)
    results = await client.search(search_term)
    results = results[0].get("description")
    await ctx.send(results)


@client.command()
async def covid(ctx):
    added, total = await covid_data()
    embed = discord.Embed(colour=discord.Colour.blue(),
                          title="Covid-19 [India]")
    icon = "https://i.ibb.co/CVJW8B9/62393982.jpg"
    embed.set_thumbnail(url=icon)
    fields = ["confirmed", "deceased", "recovered"]
    for field in fields:
        string = f"{total[field]} (+{added[field]})"
        embed.add_field(name=field.title(), value=string)
    await ctx.send(embed=embed)


@client.command()
async def copypasta(ctx):
    pasta_1 = "So 🧐 there's a lot ⬆️  more to 👈  assuming 🖥️ things about 👨people. By you 🤔 assuming things about 🤹‍♂️ someone they feel 😔 judged, and nobody ❌ wants to feel 😔 judged. Especially ❗ when they can be 😵 badly judged 👿because they're ❎ not of the same 👦🏿 color, cast, and more. It's almost ✅ always easy to assume nothing, and just ❓ ask. People here assume so many things about me, and it gets so 😠annoying. And 🤬 irritating. Now imagine 🤔 if everyone 👪did that daily 📆 to you. 😵"
    pasta_2 = "We 👪 give nice things, people 👨 abuse ❌ it, we remove it, and people are shocked 😱. Yes it wasn't your 👇 fault that it happened. But it happened 😔, and it wasn't one 1️⃣  time. You can't have nice things, because other 😡 people abuse it. Live with it. 🤠"
    await ctx.send(random.choice([pasta_1, pasta_2]))


@client.command()
async def react(ctx, count, *args):
    count = int(count) + 1
    args = "".join(args).lower()
    used_emotes = []
    emotes = emote_convert(args)
    async for message in ctx.channel.history(limit=count):
        message = message
    for emote in emotes:
        if emote in used_emotes:
            emote = fallback_emote(emote)
        await message.add_reaction(emote[1])
        used_emotes.append(emote)


@client.command()
async def poll(ctx, title, *args):
    choices = args
    count = 0
    values = []
    numbers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    for number, choice in zip(numbers, choices):
        string = "{} {}".format(number, choice)
        values.append(string)
        count += 1
    embed = discord.Embed(colour=discord.Colour.blue(),
                          title=title, description="\n".join(values))
    embed.set_footer(text="By {}".format(ctx.author.name))
    if count > 1:
        message = await ctx.send(embed=embed)
        count_ = 0
        for reaction in numbers:
            count_ += 1
            if count_ <= count:
                await message.add_reaction(str(reaction))
    else:
        message = await ctx.send("Must provide atleast 2 choices for poll")


@client.command()
async def ban(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    if member == ctx.message.author:
        await ctx.send("You cant ban yourself")
    else:
        await ctx.send("{} has been banned".format(member))
        
        
@client.command()
async def unban(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    if member == ctx.message.author:
        await ctx.send("You cant unban yourself")
    else:
        await ctx.send("{} has been unbanned".format(member))


@client.command()
async def emote(ctx, *args):
    args = " ".join(args)
    await ctx.send(emote_convert(args))


@client.command()
async def choose(ctx, *args):
    await ctx.send(random.choice(args))

@client.command()
async def help(ctx):
    await ctx.send("work in progress, Creator of this  bot, if any issues contact Mirage#6308")




@client.command()
async def halal(ctx):
    
    photo1 = "https://cdn.discordapp.com/attachments/369429848155881486/764821721110675466/Screenshot_20201011-172454_Discord.png"
      
    photo2 = " https://media.discordapp.net/attachments/727744472674467945/765467830124019734/unknown-6-1.png"
    await ctx.send(random.choice([photo1,photo2 ]))

@client.command()
async def shino(ctx):
    await ctx.send("")

@client.command()
async def skia(ctx):
    await ctx.send("")

@client.command()
async def danny(ctx):
    await ctx.send("")
    
@client.command()
async def kyuu(ctx):
    await ctx.send("")
    
@client.command()
async def rorisubereta(ctx):
    link = ""
    await ctx.send(link)

@client.command()
async def dusk(ctx):
    await ctx.send("")

@client.command()
async def ultra(ctx):
    await ctx.send("")

@client.command()
async def empty(ctx):
    await ctx.send("** **")

@client.command()
async def getsu(ctx):
    await ctx.send(" <a:s1:743700629838495775> ")

@client.command()
async def genshin(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/727744472674467945/765560757910765618/4h3zbm.png")

@client.command()
async def kakashi(ctx):
    await ctx.send(" ")


@client.command()
async def lulu(ctx):
    await ctx.send("")

@client.command()
async def poojaroom(ctx):
    await ctx.send("")

@client.command()
async def berry(ctx):
    await ctx.send("")

@client.command()
async def mamidi(ctx):
    await ctx.send("")
 
@client.command()
async def crick(ctx):
    await ctx.send(" <:love:765811820405325864>")
    
@client.command()
async def invite(ctx):
    await ctx.send(" https://discord.com/oauth2/authorize?client_id=765187097882918912&scope=bot&permissions=8")

@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '369428799273566209':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)

@client.listen("on_message")
async def reply(message):
    content = message.content.lower()
    
    if content == "catkiss":
         output = "https://cdn.discordapp.com/emojis/763296172776751144.gif?size=4096"

    elif content == "arararagi":
          output = "araragi da"

    elif content == "kajuma":
          output = "hai kazuma desu" 
    
    elif content == "lol": 
          output =  "hahahahaha"
    
    elif content == "yes":
          output = "Yeeessss!"
    
    elif content == "loli":
          output = "No loli!"
    
    elif content == "no":
          output = "Aww...why?"

    await message.channel.send(output)


token = "" #bot token 
client.run(token)


#DONT TOUCH
#token = "UserToken"
#client.run(token , bot=False)





