import discord
from rateme import Connect
from discord.ext import commands
from anime import finder
from manga import finderm
from bigtext import bigtest
from coronacases import corona, total
import random
from release import release
from link_lists import safe, kona
import yaml 

with open('config.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

prefix = data["setup"]["prefix"]
channels = data["setup"]["channels"]
valid_users = data["setup"]["valid_users"]
bot_activity = data["setup"]["bot_activity"]
token =  data["setup"]["token"]
role_message_id = data["setup"]['role_message_id']
client = commands.Bot(command_prefix=prefix)  # command prefix
client.remove_command('help')

download_image1 = safe()
download_image3 = kona()

text = bigtest()
text.bigtest()

@client.event
async def on_ready():
    print(f""" 
{text.big}
    """)
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name=bot_activity))  # status and description


# ? KNOW THE PING
@client.command()
async def ping(ctx):
    if str(ctx.channel) in channels:
        await ctx.send(f"Pong! {round(client.latency * 1000)} ms")

# ? PURGES THE CHAT MESSAGES
@client.command()
async def purge(ctx, *args):
    if str(ctx.author) in valid_users:
        no = ('{} {}'.format('', ' '.join(args)))
        no = int(no)
        await ctx.channel.purge(limit=no)

# ? RATES YOU
@client.command()
async def rateme(ctx):
    if str(ctx.channel) in channels:
        rating = Connect()
        rating.output()
        await ctx.send(rating.x)

@client.command()
async def say(ctx, *args):
    await ctx.channel.purge(limit=1)
    await ctx.send('{} {}'.format('', ' '.join(args)))

@client.command()
async def reverse(ctx, *args):
    reversed_test = ('{} {}'.format('', ' '.join(args)))
    await ctx.send(reversed_test[::-1])

@client.command()
async def cases(ctx, *args):
    if str(ctx.channel) in channels:
        args = ('{} {}'.format('', ' '.join(args)))
        args = str(args)
        args = args.replace(' ','')
        try:
            await ctx.send(corona(str(args)))
        except Exception:
            await ctx.send(total())

@client.command()
async def anime(ctx, *args):
    if str(ctx.channel) in channels:
        try:
            rating = finder()
            rating.finder('{} {}'.format('', ''.join(args)))
            embed = discord.Embed(title='anime info', value='The anime you wanted')
            embed.add_field(name='----------------------', value=rating.result)
            embed.set_thumbnail(url=rating.result2)
            await ctx.send(embed=embed)
        except:
            await ctx.send("anime not found")

@client.command()
async def manga(ctx, *args):
    try:
        ratingm = finderm()
        ratingm.finderm('{} {}'.format('', ''.join(args)))
        embed = discord.Embed(title='managa info', value='The manga you wanted')
        embed.add_field(name='----------------------', value=ratingm.resultm)
        embed.set_thumbnail(url=ratingm.result2m)
        await ctx.send(embed=embed)
    except:
        await ctx.send("manga not found")

@client.command()
async def releases(ctx, *args):
    try:
        anime_result = release()
        anime_result.release('{} {}'.format('', ''.join(args)))
        embed = discord.Embed(title='release time', value='airing time')
        embed.add_field(name='----------------------', value=anime_result.airing)
        embed.set_thumbnail(url=anime_result.cover)
        await ctx.send(embed=embed)
    except:
        await ctx.send("anime not found")

@client.command()
async def ratemyd(ctx):
    if str(ctx.author) in valid_users:
        ran = random.randrange(0,10)
        d = ('='*ran)
        await ctx.send(f'8{d}D')
        
@client.command()
async def safebooru(ctx, *args):
    try:
        range = random.randrange(1,300)
        args = ('{} {}'.format('', ' '.join(args)))
        args = str(args)
        args = args.replace(' ','+')
        download_image1.safe(range, str(args))
        image_link = download_image1.link
        await ctx.send(image_link)
    except Exception:
        await ctx.send("tag not found try using other booru")

@client.command()
async def konachan(ctx, *args):
    try:
        range = random.randrange(1,300)
        args = ('{} {}'.format('', ' '.join(args)))
        args = str(args)
        args = args.replace(' ','+')
        download_image3.kona(range, str(args))
        image_link = download_image3.link
        await ctx.send(image_link)
    except Exception:
        await ctx.send("tag not found try using other booru")

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    if str(ctx.channel) in channels:
        member = ctx.author if not member else member
        roles = [role for role in member.roles]

        embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

        embed.set_author(name=f'User Info = {member}')
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
        
        embed.add_field(name='ID:', value=member.id)
        embed.add_field(name='Guild name:', value=member.display_name)

        embed.add_field(name='Created at:', value=member.created_at.strftime('%a, %#d, %B, %Y, %I:%M %p UTC'))
        embed.add_field(name='Joined at:', value=member.joined_at.strftime('%a, %#d, %B, %Y, %I:%M %p UTC'))

        embed.add_field(name=f'Roles ({len(roles)})', value=''.join([role.mention for role in roles]))
        embed.add_field(name='Top role:', value=member.top_role.mention)

        embed.add_field(name='Is bot?', value=member.bot)

        await ctx.send(embed=embed)

@client.command()
async def info(ctx):
    if str(ctx.channel) in channels:
        embed = discord.Embed(title="Made by\nMysteriousCurry")
        embed.add_field(name='website', value="https://thisiscurry.github.io")
        await ctx.send(content=None, embed=embed)

@client.command()
async def help(ctx):
    if str(ctx.channel) in channels:
        embed = discord.Embed(title="Help has arrived")
        embed.add_field(name='ping', value="Know the ping")
        embed.add_field(
            name='rateme', value="I will rate you and be sure to give you beautiful rating")
        embed.add_field(
            name='say <text>', value="Let the bot say mean things you wanted to say to someone")
        embed.add_field(name='reverse <text>', value='Reverse the text')
        embed.add_field(name='releases <anime name>', value='find release day and date of anime')
        embed.add_field(name='purge <value>',
                        value="Will remove messages and can be used by only selected members")
        embed.add_field(name='userinfo <mention>', value='Info about users :p')
        embed.add_field(name='anime/manga <animename>', value='Get your anime/manga info')
        embed.add_field(name='ratemyd', value='self explanatory')
        embed.add_field(name='cases <countryname>', value='Get corona cases')
        embed.add_field(name='safebooru/konachan <tags>', value='browse booru | seperate tags by space and double name by _')
        await ctx.send(content=None, embed=embed)

client.run(token)
