# Kuro Selfbot Im Probably Ganna Sell This And If I Do Dont SkiddRip It Or You Are Gay And A Skid Thx <3
# I Made This 1 File On Purpose Cuz I Wanted To Make a Compact Beatz
# Has Alot Of Tools And Sheet
import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
import aiohttp
from random import choice
import random
import math
import urllib.parse
import re
import logging
import json
import os
import re
import io
import time
import json
import random
import discord
import asyncio
import datetime
import requests
import ctypes
import aiohttp
import colorama
import subprocess
import string
from pymongo import MongoClient
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
colorama.init()
#to delete embed after command
# await beaters.message.delete()

#BeatZ Color Variables


with open('config.json') as f:
	config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')
afk_message = config.get('afk_message')
paypalemail= config.get('paypalemail')
giveaway_sniper = config.get('giveaway_sniper')
slotbot_sniper = config.get('slotbot_sniper')
nitro_sniper = config.get('nitro_sniper')
privnote_sniper = config.get('privnote_sniper')

def Init():
		Beatz.run(token, bot=False, reconnect=True)

def Clear():
    os.system('cls')
Clear()

Beatz = discord.Client()
Beatz = commands.Bot(command_prefix=prefix, self_bot=True)
Beatz.remove_command("help")


@Beatz.event
async def on_message(message):
	await Beatz.process_commands(message)

    ctypes.windll.kernel32.SetConsoleTitleW(f'[Kuro Selfbot] | Version V 1.5 | Logged In As: {Beatz.user}')
    guilds = len(Beatz.guilds)
    print("\033[31m                                          ██\033[97m╗  \033[31m██\033[97m╗\033[31m██\033[97m╗   \033[31m██\033[97m╗\033[31m██████\033[97m╗  \033[31m██████\033[97m╗  ")                         
    print("\033[31m                                          ██\033[97m║ \033[31m██\033[97m╔╝\033[31m\033[31m██\033[97m║   \033[31m██\033[97m║\033[31m██\033[97m╔══\033[31m██\033[97m╗\033[31m██\033[97m╔═══\033[31m██\033[97m╗ ")                         
    print("\033[31m                                          █████\033[97m╔╝ \033[31m██\033[97m║   \033[31m██\033[97m║\033[31m██████\033[97m╔╝\033[31m██\033[97m║   \033[31m██\033[97m║ ")                         
    print("\033[31m                                          ██\033[97m╔═\033[31m██\033[97m╗ \033[31m██\033[97m║   \033[31m██\033[97m║\033[31m██\033[97m╔══\033[31m██\033[97m╗\033[31m██\033[97m║   \033[31m██\033[97m║ ")                         
    print("\033[31m                                          ██\033[97m║  \033[31m██\033[97m╗╚\033[31m██████\033[97m╔╝\033[31m██\033[97m║  \033[31m██\033[97m║╚\033[31m██████\033[97m╔╝\033[31m██\033[97m╗              ")
    print("\033[97m                                          ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝                             ")             
    print(f"                                                  \033[97m Logged In As: \033[31m{Beatz.user.name}               ")                          
    print(f"\033[31m                                          ╔═══════════════════════════════════╗ \033[97m")
    print(f"\033[31m                                          ║ \033[97mPrefix: - [\033[31m{prefix}\033[97m]\033[31m                     ║     ")
    print(f"\033[31m                                          ║ \033[97mServers: - [\033[31m{guilds}\033[97m]\033[31m                   ║     ")
    print(f"\033[31m                                          ║ \033[97mNitro: - [\033[31m{nitro}\033[97m]\033[31m                 ║  ")    
    print(f"\033[31m                                          ║ \033[97mDeveloper: - [\033[31mBeatZ#0001\033[97m]\033[31m         ║") 
    print("\033[31m                                          ╚═══════════════════════════════════╝\033[97m")                                             
    print("")
    print("")
    r = requests.post('https://discordapp.com/api/v6/invite/status')
    if r.status_code == 200:
        return True
    else:
        return False

#BeatZ Terminal Clear Command
@Beatz.command()
async def cls(ctx,):
    await ctx.message.delete()
    guilds = len(Beatz.guilds)
    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"
    Clear() 
    print("\033[31m                                          ██\033[97m╗  \033[31m██\033[97m╗\033[31m██\033[97m╗   \033[31m██\033[97m╗\033[31m██████\033[97m╗  \033[31m██████\033[97m╗  ")                         
    print("\033[31m                                          ██\033[97m║ \033[31m██\033[97m╔╝\033[31m\033[31m██\033[97m║   \033[31m██\033[97m║\033[31m██\033[97m╔══\033[31m██\033[97m╗\033[31m██\033[97m╔═══\033[31m██\033[97m╗ ")                         
    print("\033[31m                                          █████\033[97m╔╝ \033[31m██\033[97m║   \033[31m██\033[97m║\033[31m██████\033[97m╔╝\033[31m██\033[97m║   \033[31m██\033[97m║ ")                         
    print("\033[31m                                          ██\033[97m╔═\033[31m██\033[97m╗ \033[31m██\033[97m║   \033[31m██\033[97m║\033[31m██\033[97m╔══\033[31m██\033[97m╗\033[31m██\033[97m║   \033[31m██\033[97m║ ")                         
    print("\033[31m                                          ██\033[97m║  \033[31m██\033[97m╗╚\033[31m██████\033[97m╔╝\033[31m██\033[97m║  \033[31m██\033[97m║╚\033[31m██████\033[97m╔╝\033[31m██\033[97m╗              ")
    print("\033[97m                                          ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝                             ")             
    print(f"                                                  \033[97m Logged In As: \033[31m{Beatz.user.name}               ")                          
    print(f"\033[31m                                          ╔═══════════════════════════════════╗ \033[97m")
    print(f"\033[31m                                          ║ \033[97mPrefix: - [\033[31m{prefix}\033[97m]\033[31m                     ║     ")
    print(f"\033[31m                                          ║ \033[97mServers: - [\033[31m{guilds}\033[97m]\033[31m                   ║     ")
    print(f"\033[31m                                          ║ \033[97mNitro: - [\033[31m{nitro}\033[97m]\033[31m                 ║  ")    
    print(f"\033[31m                                          ║ \033[97mDeveloper: - [\033[31mBeatZ#0001\033[97m]\033[31m         ║") 
    print("\033[31m                                          ╚═══════════════════════════════════╝\033[97m")                                             
    print("")
    print("")

#BeatZ Help Command Embed
@Beatz.command(pass_context=True)
async def iugeuhfijsefhgi(beaters):
        embed = discord.Embed(title="Kuro Selfbot <3", description="", color=0x000000)
        embed.add_field(name="`geo`", value="**Geo Lookups An IP.**.", inline=True)
        embed.add_field(name="`cfres`", value="**Resolves CloudFlare Domain.**", inline=True)
        embed.add_field(name="`pscan`", value="**PortScans An IP.**", inline=True) 
        embed.add_field(name="`toxic`", value="**Makes Chat Blank.**", inline=True)
        embed.add_field(name="`clear [Amonut]`", value="**Clears An Amount Of Messages.**", inline=True) 
        embed.add_field(name="`clearall`", value="**Clears All Messages.**", inline=True)     
        embed.add_field(name="`info`", value="**Gives Info Of User.**", inline=True)
        embed.add_field(name="`bw`", value="**Gives You Some BubbleWrap.**", inline=True)
        embed.add_field(name="`hug`", value="**Hugs Mentioned User.**", inline=True)
        embed.add_field(name="`kiss`", value="**Kisses Mentioned User.**", inline=True)
        embed.add_field(name="`slap`", value="**Slaps Mentioned User.**", inline=True)
        embed.add_field(name="`spam [Amount]`", value="**Spams Messages.**", inline=True)  
        embed.add_field(name="`dmlogger`", value="**Turns DM Logger On And Off.**", inline=True)
        embed.add_field(name="`afk`", value="**Turns AFK Mode On And Off.**", inline=True)
        embed.add_field(name="`leavegroups`", value="**Leaves All Groupchats.**", inline=True)
        embed.add_field(name="`ascii`", value="**Turns Text Into Ascii**", inline=True)
        embed.add_field(name="`slots`", value="**Gambles Slots.**", inline=True)
        embed.add_field(name="`magic8ball [Question]`", value="**Asks 8ball A Question.**", inline=True)   
        embed.add_field(name="`paypal [Amount]`", value="**Rquests An Amount Of Money.**", inline=True) 
        embed.add_field(name="`dick`", value="**Shows Mentioned Users Dick Size.**", inline=True)   
        embed.add_field(name="`hypesquad [House]`", value="**Changes Your Hypesquad To What You Choose.**", inline=True)
        embed.add_field(name="`kickall/banall`", value="**Bans Everyone In Server Or Kicks Everyone In Server.**", inline=True)
        embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
        await beaters.send(embed=embed)
        await beaters.message.delete()

#BeatZ Bubble Wrap Lel
@Beatz.command(pass_context=True)
async def bw(beaters):
    await beaters.send("\n".join(["Heres Some Bubble Wrap :heart:\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r"]))
    await beaters.message.delete()

#BeatZ VPN Shits
@Beatz.command(pass_context=True)
async def vpn(beaters):
        embed = discord.Embed(title="KuroSec VPN Plans", description="```KuroSec Is A VPN Company That Cares Fully About Your Privacy We Are Here To Stop DDoS Attack With Our Anti-DDoS Protection And Our Custom Firewalls, We Provide A No Log Policy We Provide Locations That Fit You Best For Gaming Or Web Surfing, We Are Constantly Updating Our Firewalls To Block New DDoS Attack Methods.```", color=0x000000)
        embed.add_field(name="__Prices__", value="``Contact Me Or Kills For Special Plan``",inline=False)       
        embed.add_field(name="`1 Month`", value="**$10.**", inline=False)
        embed.add_field(name="`3 Months`", value="**$25.**", inline=False)
        embed.add_field(name="`Reseller`", value="**$35. Split Money 50/50**", inline=False) 
        embed.add_field(name="`Lifetime`", value="**$100.**", inline=False)
        embed.add_field(name="__Payment Options__", value="``We Accept, Paypal,Cashapp,Venmo.``", inline=False)   
        embed.set_footer(text="Copyright © BeatZ#0001 ", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
        await beaters.send(embed=embed)
        await beaters.message.delete()

#BeatZ Ipinfo.io Geo Lookup Embed
@Beatz.command(pass_context=True)
async def geo(beaters,ip):
    iplookupurl = ("https://ipinfo.io/"+ip)
    response = requests.get(iplookupurl)
    resolve = response.json()
    ipaddy = resolve["ip"]
    city = resolve["city"]
    region = resolve["region"]
    country = resolve["country"]
    org = resolve["org"]
    post = resolve["postal"]
    embed = discord.Embed(title="IP Lookup <3", description="IP: %s\n CITY: %s\nREGION: %s\nCOUNTRY: %s\nISP: %s\nPOSTAL: %s\n"%(ipaddy,city,region,country,org,post), color=0x000000)
    embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
    await beaters.send(embed=embed)
    await beaters.message.delete()

#BeatZ About Embed
@Beatz.command()
async def about(beaters):
    embed = discord.Embed(title="About Kuro Selfbot :heart:", description="Developer: BeatZ#0001\nWebsite: https://beatz.pw/\nLanguage: Python\nVersion: 1.4", color=0x000000)
    embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
    await beaters.send(embed=embed)
    await beaters.message.delete()   
    

#BeatZ CloudFlare Resolver Embed
@Beatz.command(pass_context=True)
async def cfres(beaters,domain):
        cfpage=("https://webresolver.nl/api.php?key=HV3WS-KA7N9-WNASK-ZFUYL&html=0&action=cloudflare&string="+domain)
        resp = requests.get(cfpage)
        embed = discord.Embed(title="CloudFlare Resolver", description=f"{resp.text}", color=0x000000)
        embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
        await beaters.send(embed=embed)
        await beaters.message.delete()

@Beatz.command()
async def perk(beaters):
    embed= discord.Embed(title="Perk Beatz Commands", description="**.ping**     -> Shows Beatz Ping.\r**.kick**      -> Kicks A User.\r**.userinfo** -> Shows Info Of User.\r**.users**    -> Shows Amount Of Users In Server.\r**.clear**    -> Clears Messages.\r**.mute**     -> Mutes A User.", color=0xDC143C, timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Here is my invite link", value="[https://discordapp.com/api/oauth2/authorize?Beatz_id=705902641787437056&permissions=0&scope=Beatz]", inline = False)
    embed.set_footer(text=f"Requested By> {beaters.author.name}")
    await beaters.message.delete()
    await beaters.send(embed=embed)        

#BeatZ Whois Embed
@Beatz.command()
async def whois(beaters,ip):
        whoiscanurl = ("https://api.hackertarget.com/whois/?q="+ip)
        response = requests.get(whoiscanurl)
        embed = discord.Embed(title="Whois <3", description="%s"%(response.text), color=discord.Color.green())
        embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
        await beaters.send(embed=embed)  
        await beaters.message.delete()

#BeatZ Port Scan Embed
@Beatz.command(pass_context=True)
async def pscan(beaters,ip):
        portscanurl = ("https://api.hackertarget.com/nmap/?q="+ip)
        response = requests.get(portscanurl)
        embed = discord.Embed(title="Port Scan <3", description="%s"%(response.text), color=0x000000)
        embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
        await beaters.send(embed=embed)
        await beaters.message.delete()

#BeatZ Close Function
@Beatz.command(pass_context=True)
async def close(beaters):
    await beaters.message.delete()
    print("\033[31mShutting Down Selfbot")
    await Beatz.close()        
 
#BeatZ Tits Embed
@Beatz.command()
async def tits(message, member: discord.Member = None):
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json() 
    embed = discord.Embed(title=f"{message.author.name} Gives {member.name} Titties :heart:", color=0x000000)
    embed.set_image(url=res['url'])
    embed.set_footer(text="Titties <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
    await message.send(embed=embed)
    await message.message.delete()

#BeatZ Hug Embed
@Beatz.command()
async def hug(message, member: discord.Member = None):
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json() 
    embed = discord.Embed(title=f"{message.author.name} Hugs {member.name} :heart:", color=0x000000)
    embed.set_image(url=res['url'])
    embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
    await message.send(embed=embed)
    await message.message.delete()

#BeatZ Pat Embed
@Beatz.command()
async def pat(message, member: discord.Member = None):
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json() 
    embed = discord.Embed(title=f"{message.author.name} Pats {member.name} :heart:", color=0x000000)
    embed.set_image(url=res['url'])
    embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
    await message.send(embed=embed)
    await message.message.delete()   

#BeatZ Dog Embed
@Beatz.command()
async def dog(beaters, url):
    r = requests.get("https://dog.ceo/api/breeds/image/random")
    res = r.json() 
    embed = discord.Embed(title=f"Heres A Doggy :heart:", color=0x000000)
    embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
    embed.set_image(url=res['url'])
    await beaters.send(embed=embed)
    await beaters.message.delete()
    
#BeatZ kiss Embed
@Beatz.command()
async def kiss(message, member: discord.Member = None):
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json() 
    embed = discord.Embed(title=f"{message.author.name} Kisses {member.name} :heart:", color=0x000000)
    embed.set_image(url=res['url'])
    embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
    await message.send(embed=embed)
    await message.message.delete()

#BeatZ slap Embed
@Beatz.command()
async def slap(message, member: discord.Member = None):
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json() 
    embed = discord.Embed(title=f"{message.author.name} Slaps TF Outa {member.name} :heart:", color=0x000000)
    embed.set_image(url=res['url'])
    embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
    await message.send(embed=embed)
    await message.message.delete()

#BeatZ BlowJob Embed
@Beatz.command()
async def blowjob(message):
    await message.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    embed = discord.Embed()
    embed = discord.Embed(title=f" Heres A BlowJob :heart:", color=0x000000)
    embed.set_image(url=res['url'])
    embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")    
    await message.send(embed=embed)
    await message.message.delete()
    
#BeatZ Anal Embed
#BeatZ BlowJob Embed
@Beatz.command()
async def anal(message):
    await message.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    embed = discord.Embed()
    embed = discord.Embed(title=f" Heres Some Anal :heart:", color=0x000000)
    embed.set_image(url=res['url'])
    embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")    
    await message.send(embed=embed)
    await message.message.delete()

#BeatZ Fucking Your Mom embed
@Beatz.command(pass_context=True)
async def fuck(beaters, member: discord.Member = None):
        member = beaters.author if not member else member
        embed = discord.Embed(title=f"BeatZ Fucking The Shit Outa {member} Mom :kissing_heart:", description="", color=0x000000)
        embed.set_image(url="https://thumb-p4.xhcdn.com/a/R292lF5ESNf4icujFKO4Aw/000/116/650/774_450.gif"),
        embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
        await beaters.send(embed=embed)
        await beaters.message.delete()


#BeatZ Penis Embed
@Beatz.command()
async def dick(ctx, *, user: discord.Member = None): 
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    embed = discord.Embed(title=f"{user.name}'s Dick Size :heart:", description=f"8{dong}D", color=0x000000)
    embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
    await ctx.send(embed=embed)

#BeatZ user Info Embed
@Beatz.command(pass_context=True)
async def info(beaters, member: discord.Member = None):
        embed = discord.Embed(title=f"User Info <3", color=0x000000)
        embed.add_field(name="`User ID:`", value=member.id, inline=False)
        embed.add_field(name="`Name:`", value=member.display_name, inline=False)
        embed.add_field(name="`Creation Date:`", value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p"), inline=False)
        embed.add_field(name="`Bot Check`", value=member.bot, inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
        await beaters.send(embed=embed)
        await beaters.message.delete()

#BeatZ Server Info Embed
@Beatz.command()
async def serverinfo(ctx):
        await ctx.message.delete()
        embed = discord.Embed(title="Server Info :heart:", color=0x000000)
        embed.add_field(name="`Server ID:`", value=ctx.guild.id, inline=False)
        embed.add_field(name="`Server Name:`", value=ctx.guild.name, inline=False)
        embed.add_field(name="`Server Owner:`", value=ctx.guild.owner.display_name, inline=False)
        embed.add_field(name="`Creation Date:`", value=ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p"), inline=False)
        embed.add_field(name="`Members:`", value=len(ctx.guild.members), inline=False)
        embed.add_field(name="`Roles:`", value=len(ctx.guild.roles), inline=False)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
        await ctx.send(embed=embed)        

#BeatZ user Info Embed
@Beatz.command(pass_context=True)
async def paypal(beaters, amount: int):
        embed = discord.Embed(title=f"Paypal :heart:", color=0x000000)
        embed.add_field(name="`Email:`", value=f"{paypalemail}", inline=False)
        embed.add_field(name="`Amount:`", value=(amount), inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/678697731786670101/707231627897733120/1Pdw2RE.png")
        embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
        await beaters.send(embed=embed)
        await beaters.message.delete()

#BeatZ Read Unread Commands
@Beatz.command()
async def read(ctx):
    await ctx.message.delete()
    for d, in Beatz.private_channels:
      await dm.ack()    

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

#BeatZ Rainbow Role
@Beatz.command()
async def rainbow(ctx, *, role):
    
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(1)
        except:
            break        

#BeatZ Bitcoin Worth
@Beatz.command(aliases=['bitcoin'])
async def btc(ctx): 
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)    

@Beatz.command()
async def ping(ctx, ip):
  await ctx.message.delete()
  pingR = subprocess.getoutput("ping "+ip)
  pingP = pingR.split("\n")
  print (pingP[2])
  print (pingP[3])
  print (pingP[4])
  print (pingP[5])


#BeatZ Hypesquad Changer
@Beatz.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house): 
    await ctx.message.delete()
    request = requests.Session()
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }    
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"[ERROR]:")        

#BeatZ Message        
@Beatz.command()
async def spam(ctx, amount: int, *, message): 
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)

#BeatZ Clean Messages Command
@Beatz.command()
async def clearall(ctx): 
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=99999).filter(lambda m: m.author == Beatz.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

#BeatZ Clear Messages Command
@Beatz.command()
async def clear(ctx, amount: int): 
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Beatz.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass                                  

dm_log = 0
#DM Log Toggle On And Off
@Beatz.command()
async def dmlogger(message):
    await message.message.delete()
    global dm_log
    if dm_log == 0:
        dm_log += 1
        await message.send("Dm Logger `ON`", delete_after=5)
        
    elif dm_log == 1:
        dm_log -= 1
        await message.send("Dm Logger `OFF`", delete_after=5)      

#BeatZ Deleted Message Logger
@Beatz.event
async def on_message_delete(message):
     global dm_log
     if dm_log == 1:
        await Beatz.process_commands(message)
        try:
            if message.guild is None and message.author != Beatz.user:
                embed=discord.Embed(title="", color=0x000000) 
                embed.set_author(name="Message Deleted")
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name="LOL Nothing Can Be Deleted From Me :heart:", value="Deleted Message : {}".format(message.content), inline=True)
                embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
                await message.channel.send(embed=embed)
        except Exception as e:
            print(str(e))
     else:
        pass   

afk_log = 0
#BeatZ AFK On And Off
@Beatz.command()
async def afk(message):
    await message.message.delete()
    global afk_log
    if afk_log == 0:
        afk_log += 1
        await message.send("AFK `ON`", delete_after=5)
        
    elif afk_log == 1:
        afk_log -= 1
        await message.send("AFK `OFF`", delete_after=5)    

#BeatZ AFK Message
@Beatz.event                
async def on_message(message):
    global afk_log
    if afk_log == 1:
        await Beatz.process_commands(message)
        if message.guild is None:
            if message.author == Beatz.user:
                return
            embed = discord.Embed(title="I Am AFK! :heart:", description=f"Hi {message.author}, {afk_message}", color=0x000000,)
            embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif")
            await message.channel.send(embed=embed)
    await Beatz.process_commands(message)
      
#BeatZ Token Info
@Beatz.command()
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
    except KeyError:
        print(f"[ERROR]: Invalid token")
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)  

#BeatZ DDOS Command lel
@Beatz.command()
async def boot(ctx):
    await ctx.message.delete()
    await ctx.send("Booting You Offline.")
    time.sleep(1)
    await ctx.send("**3**")
    await ctx.send("**2**")
    await ctx.send("**1**")
    time.sleep(1)
    await ctx.send("`Nigga you Offline.`")



tiny_table = str.maketrans(string.ascii_lowercase, 'ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖ٩ʳˢᵗᵘᵛʷˣʸᶻ')
@Beatz.command(aliases=['tinyfont', 'small', 'smallfont'])
async def tiny(ctx, *, text: str = None):
        if text is None:
            return await ctx.error('Please provide text to convert!')
        await ctx.message.edit(content=text.lower().translate(tiny_table))

#BeatZ Magic 8 Ball Command
@Beatz.command()
async def magic8ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
      'That is a resounding no',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
      'Maybe',
      'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False,)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_footer(text="Kuro Selfbot <3", icon_url="https://media1.tenor.com/images/7cb33e07bf0f28f426fbd9412056813f/tenor.gif",)
    await ctx.send(embed=embed)

#BeatZ Combine Name Command
@Beatz.command()
async def combine(ctx, name1, name2):
    await ctx.message.delete()
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = "".join([name1letters, name2letters])
    embed = (discord.Embed(description=f"{ship}",color=0x000000))
    embed.set_author(name=f"{name1} + {name2}")
    await ctx.send(embed=embed) 

#BeatZ Ban Everyone  
@Beatz.command()
async def banall(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

#BeatZ DM All Command
@Beatz.command()
async def dmall(ctx, *, message):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)    
            await user.send(message)
        except:
            pass        

#BeatZ Kick All
@Beatz.command()
async def kickall(ctx):
    await ctx.message.delete()
    for user in list(ctx.group.members):
        try:
            await user.kick()
        except:
            pass               

#BeatZ Txt To TTS
@Beatz.command()
async def tts(ctx, *, message):
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))
   
#BeatZ Call Spammer
@Beatz.command()
async def phone(ctx):
    await ctx.message.delete()
    headers = {
    'authorization': token,
    'referer': 'https://discordapp.com/channels/@me/'+str(ctx.message.channel.id),
    'origin': 'https://discordapp.com/',
    'accept-encoding': 'gzip, deflate, br'
    }
    url = 'https://discordapp.com/api/v6/channels/'+str(ctx.message.channel.id)+'/call/ring'
    payload = {'recipients': 0}
    t_end = time.time() + 10
    while time.time() < t_end:
         r = requests.post(url, headers=headers, json=payload)
         if r.status_code != 204:
             print('[#] Being ratelimited, applying 100ms latency')
             time.sleep(0.1)
         time.sleep(0.3)

@Beatz.command()
async def cbomb(ctx):
    await ctx.message.delete()
    latency = 0
    choices = ['brazil','europe','frankfurt','hong-kong','india','japan','russia','singapore','south-africa','sydney','us-central','us-east','us-south','us-west', 'amsterdam']
    headers = {
    'authorization': token,
    'referer': 'https://discordapp.com/channels/@me/'+str(ctx.message.channel.id),
    'accept-encoding': 'gzip, deflate, br',
    'origin': 'https://discordapp.com/'
    }
    url = 'https://discordapp.com/api/v6/channels/'+str(ctx.message.channel.id)+'/call'
    t_end = time.time() + 10
    while time.time() < t_end:
        x = random.choice(choices)
        payload = {'region': x}
        r = requests.patch(url, headers=headers, json=payload)
        if r.status_code != 204:
            print("[#] Being ratelimited, applying 100ms latency")
            latency += 0.1
            time.sleep(latency)
        time.sleep(latency)

#BeatZ Get user Avatar
@Beatz.command()
async def av(ctx, *, user: discord.Member=None): 
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}"))             

@Beatz.event
async def on_message_edit(before, after):
    await Beatz.process_commands(after)    

#BeatZ Text To Acscii Command
@Beatz.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

#BeatZ Groupchat Leaver
@Beatz.command()
async def groupleaver(ctx):
    await ctx.message.delete()
    for channel in Beatz.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()    


# BeatZ Toxic Ass Spam Thingy Bruh LMFAOO
@Beatz.command(pass_context=True)
async def toxic(beaters): #this bitch is toxic -beatz
    await beaters.message.delete()
    
    await beaters.send('ﾠﾠ'+'\n' * 1000 + 'ﾠﾠ')
    
#BeatZ Slot Machine
@Beatz.command(aliases=['slots', 'bet'])
async def slot(ctx): 
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}))    

    #BeatZ Loves You Text
@Beatz.command(pass_context=True)
async def love(beaters):
    await beaters.send("\n".join(["```yaml",

" ____             _   ______",
"|  _ \           | | |___  /",
"| |_) | ___  __ _| |_   / / ",
"|  _ < / _ \/ _` | __| / /  ",
"| |_) |  __/ (_| | |_ / /__ ",
"|____/ \___|\__,_|\__/_____|",
" _                          ",
"| |                         ",
"| |     _____   _____  ___  ",
"| |    / _ \ \ / / _ \/ __| ",
"| |___| (_) \ V /  __/\__ \ ",
"|______\___/ \_/ \___||___/ ",
"__     __          ",
"\ \   / /          ",
" \ \_/ /__  _   _  ",
"  \   / _ \| | | | ",
"   | | (_) | |_| | ",
"   |_|\___/ \__,_| ",     
"```"]))
    await beaters.message.delete()

#BeatZ Joke Embed
@Beatz.command()
async def joke(ctx):  
    await ctx.message.delete()
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])    

#BeatZ Help Into Terminal
@Beatz.command() 
async def help(beaters):
        print("\033[31m◄ Commands. ►")
        print("\033[97mhelp -> \033[31mShows Commands.")  
        print("\033[97mabout -> \033[31mShows About Bot.")
        print("\033[97mgeo [\033[31mIP\033[97m] -> \033[31mGeo Lookups An IP.")
        print("\033[97mpscan [\033[31mIP\033[97m] -> \033[31mPort Scans An IP.")
        print("\033[97mcfres [\033[31mURL\033[97m] -> \033[31mResolves A Cloudflare Domain.")
        print("\033[97mtoxic -> \033[31mMakes Chat Blank.")
        print("\033[97mclear [\033[31mAmount\033[97m] -> \033[31mClears An Amount Of Messages.")
        print("\033[97mclearall -> \033[31mClears All Messages.")
        print("\033[97minfo -> \033[31mGives Info Of User.")
        print("\033[97mserverinfo -> \033[31mGives Info Of Server.")
        print("\033[97mbw -> \033[31mGives You Some Bubblewrap.")
        print("\033[97mhug -> \033[31mHugs Mentioned User.")
        print("\033[97mkiss -> \033[31mKisses Mentioned User.")
        print("\033[97mslap -> \033[31mSlaps Mentioned User.")
        print("\033[97mpat -> \033[31mPats Mentioned User.")
        print("\033[97mblowjob -> \033[31mShows You A Blowjob.")
        print("\033[97manal -> \033[31mShows You Some Anal.")  
        print("\033[97mspam [\033[31mAmount\033[97m] [\033[31mMessage\033[97m] -> \033[31mSpams Message.")
        print("\033[97mcombine [\033[31mName1\033[97m] [\033[31mName2\033[97m] -> \033[31mCombines Names.")
        print("\033[97mdmall [\033[31mMessage\033[97m] -> \033[31mDms Everyone In Server. [MIGHT GET BANNED].")
        print("\033[97mdmlogger -> \033[31mToggles DM Logger On/Off.")
        print("\033[97mafk -> \033[31mToggles AFK On/Off.")
        print("\033[97mtts [\033[31mMessage\033[97m] -> \033[31mTurns Message Into Audio.")
        print("\033[97mrainbow [\033[31mRole\033[97m] -> \033[31mTurns Role Color Into Rainbow.")
        print("\033[97mleavegroups -> \033[31mLeaves All Groupchats.")
        print("\033[97mascii [\033[31mText\033[97m] -> \033[31mTurns Text Into Ascii.")
        print("\033[97mslots -> \033[31mGambles.")
        print("\033[97mmagic8ball [\033[31mQuestion\033[97m] -> \033[31mAsks 8 Ball A Question.")
        print("\033[97mpaypal [\033[31mAmount\033[97m] -> \033[31mRquests Paypal Money.")
        print("\033[97mdick -> \033[31mShows Mentioned Users Dick Size.")
        print("\033[97mhypesquad [\033[31mHouse\033[97m] -> \033[31mChanges Your Hypesquad To What You Want.") 
        print("\033[97mav -> \033[31mShows Mentioned Users Profile Picture.")
        print("\033[97mping [\033[31mPing\033[97m] -> \033[31mPing An IP.") 
        print("\033[97mread -> \033[31mReads All Un Read Messages In Servers.") 
        print("\033[97mclose -> \033[31mClosed Out Selfbot.")
        print("\033[97mcls -> \033[31mClears Terminal.")
        await beaters.message.delete()   

#BeatZ Nitro Sniper
@Beatz.event
async def on_message(message):

    def GiveawayData():
        print(
        f"\033[97m - Channel:\033[97m[{message.channel}]"
        f"\n\033[97m - Server:\033[97m[{message.guild}]"   
    )

    def SlotBotData():
        print(
        f"\033[97m - CHANNEL:\033[97m[{message.channel}]"
        f"\n\033[97m - SERVER:\033[97m[{message.guild}]"   
    )  

    def NitroData(elapsed, code):
        print(
        f"\n\033[97m - Channel Code Was In: \033[93m[\033[31m{message.channel}\033[93m]" 
        f"\n\033[97m - Server Code Was In: \033[93m[\033[31m{message.guild}\033[93m]"
        f"\n\033[97m - Author: \033[93m[\033[31m{message.author}\033[93m]"
        f"\n\033[97m - Time: \033[93m[\033[31m{elapsed}\033[93m]"
        f"\n\033[97m - Code: \033[93m[\033[31m{code}\033[93m]"
    )

    def PrivnoteData(code):
        print(
        f"\033[97m - CHANNEL:\033[93m[\033[31m{message.channel}\033[93m]" 
        f"\n\033[97m - SERVER:\033[31m[{message.guild}]"
        f"\n\033[97m - CONTENT:\033[31m[The content can be found at Privnote/{code}.txt]"
    )        

    time = datetime.datetime.now().strftime("%H:%M %p")  
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')
                
            headers = {'Authorization': token}
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', 
                headers=headers,
            ).text
        
            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                f"\n\033[31m[{time} - Nitro Already Redeemed]")
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                f"\n\033[31m[{time} - Nitro Success]")
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                f"\n\033[31m[{time} - Nitro Unknown Gift Code]")
                NitroData(elapsed, code)
        else:
            return
            
    if 'Someone just dropped' in message.content:
        if slotbot_sniper == True:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                    f"\n\033[31m[{time} - SlotBot Couldnt Grab]")
                    SlotBotData()                     
                print(""
                f"\n\033[31m[{time} - Slotbot Grabbed]")
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:    
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                    f"\n\033[31m[{time} - Giveaway Couldnt React]")
                    GiveawayData()            
                print(""
                f"\n\033[31m[{time} - Giveaway Sniped]")
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Beatz.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:    
                print(""
                f"\n\033[31m[{time} - Giveaway Won]")
                GiveawayData()
        else:
            return

    if 'privnote.com' in message.content:
        if privnote_sniper == True:
            code = re.search('privnote.com/(.*)', message.content).group(1)
            link = 'https://privnote.com/'+code
            try:
                note_text = pn.read_note(link)
            except Exception as e:
                print(e)    
            with open(f'Privnote/{code}.txt', 'a+') as f:
                print(""
                f"\n\033[31m[{time} - Privnote Sniped]")
                PrivnoteData(code)
                f.write(note_text)
        else:
            return
    await Beatz.process_commands(message)                 

#BeatZ Blocking Out Dumbass Errors In CMD
@Beatz.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"[ERROR]: You're missing permission to execute this command")
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"[ERROR]: Not a valid image")
    elif isinstance(error, discord.errors.Forbidden):
        print(f"[ERROR]: Discord error: {error}")
    elif "Cannot send an empty message" in error_str:
        print(f"[ERROR]: Couldnt send a empty message")
    elif "Unknown Message" in error_str:
        pass       
    else:
        print(f"[ERROR]: {error_str}")   

if __name__ == '__main__':
    Init()
