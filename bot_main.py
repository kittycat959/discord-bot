import discord
import random
import time
import os

#setting up the connections
#setting up the connections
client = discord.Client()

#options for different things
prefix = "/"

#gererating the wiafu gif lists
kanna = ["https://media.tenor.com/images/3266d24fc649eb37eef9af6d9fbe38e5/tenor.gif","https://media1.tenor.com/images/f89b26e3a3d064079745d72cbb201373/tenor.gif?itemid=8403739","https://media.giphy.com/media/Q2DabV4eRh160/giphy.gif","https://memestatic.fjcdn.com/gifs/Cute_05a854_6424003.gif","https://78.media.tumblr.com/9169898bb5f3b5671da1c7369d8560ca/tumblr_olfracttCq1twgfw0o2_500.gif","https://i.kym-cdn.com/photos/images/original/001/239/111/8f2.gif","data:image/jpeg;base64,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","https://i.makeagif.com/media/5-01-2017/4_-8nV.gif","https://i.pinimg.com/originals/8f/b3/33/8fb3333aa0b2a46b9e7b0f338e35fbb2.gif","https://media2.giphy.com/media/l0IyjCRcRa6pQo2S4/giphy.gif"]
tohru = ["https://media.tenor.com/images/fbb5d8fd3f94fb2f66d9cd472ee65e9c/tenor.gif","https://media2.giphy.com/media/fT3PPZwB2lZMk/giphy.gif","https://media.tenor.com/images/3f66010aab8d833dfb0258fc4db1f3fc/tenor.gif","https://thumbs.gfycat.com/ClosedDistantKoodoo-max-1mb.gif","https://media.tenor.com/images/f8d50c5fceebda97dc41221116a9a95a/tenor.gif","https://i.kym-cdn.com/photos/images/original/001/221/161/c8e.gif","https://i.pinimg.com/originals/8f/92/20/8f9220a0d6a23e75828cf62335091862.gif"]
kobayashi = ["https://i.kym-cdn.com/photos/images/original/001/228/305/8ae.gif","https://steamusercontent-a.akamaihd.net/ugc/923668585465499655/F2C7A20538AECD156AD5D9F9EDB59251A07291B4/","https://78.media.tumblr.com/b1bba8bbc97be0ba6de97059051fd581/tumblr_opf7tfcoGX1tdj66po1_500.gif","https://i.kym-cdn.com/photos/images/newsfeed/001/237/735/e2a.gif","https://steamusercontent-a.akamaihd.net/ugc/814432560662096139/6D9CC45A2CF2A400CE08DD4B94F519840C1A55F2/"]
lucoa = ["https://i.kym-cdn.com/photos/images/newsfeed/001/230/217/0af.gif","https://media.tenor.com/images/69c4c3883286f8476fb0c8524890feea/tenor.gif","https://i.pinimg.com/originals/e2/24/6c/e2246c49cabff7a3683892e7913d3e22.gif","https://thumbs.gfycat.com/HomelyWhiteHapuku-size_restricted.gif"]
saikawa = ["https://thumbs.gfycat.com/CarefulLividGermanspaniel-size_restricted.gif","https://thumbs.gfycat.com/SlushyJauntyBats-size_restricted.gif","https://media1.tenor.com/images/6c3d6958671a4d476f7cb7acd9b42462/tenor.gif?itemid=7807792","https://i.pinimg.com/originals/c2/76/31/c2763106fae32740cfaea638300242a6.gif","https://i.kym-cdn.com/photos/images/newsfeed/001/224/085/326.gif"]

megumin=["https://media.tenor.com/images/2a5e22774498fbda42cccbb3bd4d49f3/tenor.gif","https://media1.tenor.com/images/f4dc9b8602807ccc73d1579d9f59a1cd/tenor.gif?itemid=5827518","https://i.pinimg.com/originals/59/29/11/59291146fc51ddaadf559a8ad69e1970.gif","https://orig00.deviantart.net/904b/f/2016/145/1/5/suba3_by_artemsan15-da3t1zv.gif","https://media3.giphy.com/media/eBN6oifiv4k5G/giphy.gif","https://thumbs.gfycat.com/GlaringRawEasteuropeanshepherd-small.gif","https://78.media.tumblr.com/095f6406be298d5be2a4ffb9fbf1ea77/tumblr_o6dhloXs6r1ue9gfbo1_500.gif","https://i.pinimg.com/originals/68/77/5b/68775be127cbc43346107697e1a012c6.gif","https://78.media.tumblr.com/cbadfb4245f483cf7f4676f2e344e34a/tumblr_otpwppyzNK1u0xk60o2_r1_500.gif"]
aqua = ["https://media.giphy.com/media/sFeoAaOqgEuTS/giphy.gif","https://media.giphy.com/media/n9NCmeG9wf7wY/giphy.gif","https://78.media.tumblr.com/66718aa3dcfe247aa608373e76642a60/tumblr_om2rt9w1WN1u2inano1_500.gif","https://media.giphy.com/media/oiyJ7Gluc50Zy/giphy.gif","https://media.giphy.com/media/qQNxoVSUdWhMs/giphy.gif"]
darkness = ["https://pa1.narvii.com/6560/9df2912995b8b7f0ffed65249f48a289e66c069a_hq.gif","https://media1.tenor.com/images/3081ad375292d7bbc06031bf7ad4960a/tenor.gif?itemid=7592940","https://i.imgur.com/MEc7OOW.gif","http://gifimage.net/wp-content/uploads/2017/10/darkness-konosuba-gif-1.gif","https://i.pinimg.com/originals/3a/ba/1d/3aba1d23c0a2a322cbca9f5b6898b795.gif"]
satou = ["https://vignette.wikia.nocookie.net/konosuba/images/0/0f/Kona_Suba.GIF/revision/latest?cb=20170130200606","https://i.kym-cdn.com/photos/images/original/001/141/487/7a8.gif","https://pa1.narvii.com/6054/9cefc24515b5ce43e96825e72a6b0290e024e742_hq.gif","https://media1.tenor.com/images/d2dd8122eac32df3ad87b436b90c3dd5/tenor.gif?itemid=7333081","https://78.media.tumblr.com/a4d28ee86770548b9bff82396b0c6b3d/tumblr_o9gtypfQH51sg8uefo2_540.gif"]

kaos = ["https://78.media.tumblr.com/f7d3897f56544e3094fce95f990bd440/tumblr_p7rxegKko61tx45yjo1_500.gif","https://78.media.tumblr.com/ccf819f154179e682c4eb306192fe00e/tumblr_p90lzrCXJh1tx45yjo1_500.gif","https://78.media.tumblr.com/700df5f9c85955d4cda4057d00bb0bc0/tumblr_p8t45d9WhO1tx45yjo1_500.gif","https://steamusercontent-a.akamaihd.net/ugc/919175706426856678/C2A95FB55E9A3D186F0796E5E757D9DFBBAEA27F/","https://78.media.tumblr.com/8398e7a3ad6060e67ff1994b3c92b71a/tumblr_pa89r3tYj31xtg4ygo1_500.gif"]
ruki = ["https://78.media.tumblr.com/8591fcdb76fc8aece76a9421d5a7112d/tumblr_p6smbpwwfQ1sxfvy5o1_500.gif","https://78.media.tumblr.com/9c1ec904368857d6f414b0fd035e2c51/tumblr_p7t2wmDPNm1t0lt8go1_500.gif","https://78.media.tumblr.com/8161a2de0a4bc9f57c728e3f92d0bbde/tumblr_p8o552Xho21wnhduho2_500.gif","https://78.media.tumblr.com/9f7289b5896dd46b9531aec99e9947a8/tumblr_p76znmBQt51u86t2qo1_540.gif","https://i.pinimg.com/originals/49/7c/4c/497c4c2d6efa9e7491cf8a77134e24b3.gif"]
tsubasa = ["http://pa1.narvii.com/6864/07e5dad2d882c1aaa93ff9789be9d320e50b3c11r1-540-304_00.gif","https://78.media.tumblr.com/32db8c513fa98c64b37e2737f068a6c1/tumblr_p9n1zzj5PV1s13tjpo2_500.gif","https://78.media.tumblr.com/36c5fbe106065d3aee3d6586b6b1001c/tumblr_p90m28Xrl31tx45yjo1_500.gif","https://78.media.tumblr.com/eb085cd10fe07496bd987c598114b668/tumblr_p6qkzsH9KF1xo4i3go3_500.gif"]
koyume = ["https://78.media.tumblr.com/b06a67c6e717ca02e74a5edcb305ffab/tumblr_p6q4syrDt01u0xk60o1_500.gif","https://78.media.tumblr.com/7df84c089ca9c8f094c06fb2525754ce/tumblr_p86necsn9y1wgkyjdo1_250.gif","https://78.media.tumblr.com/6871a90002d16c89aaf5e45459a65390/tumblr_p8t4372EIC1tx45yjo1_500.gif","https://78.media.tumblr.com/29d820caf74d2b0410077d17a9de87e6/tumblr_p7x3xqOJwt1rxajw6o2_r1_500.gif"]
fuura = ["https://78.media.tumblr.com/f4464eafec3cf9960d8d3a12dc917437/tumblr_p8mfsqTSiX1v6j467o1_500.gif","https://i.pinimg.com/originals/9c/81/5d/9c815ddf5843f0e0eae8fa134d81884b.gif","https://i.pinimg.com/originals/b9/9e/8b/b99e8b83a823420601b017ff23338c0f.gif","https://i.pinimg.com/originals/e3/35/63/e335638413cb72a8eea2ad9fd0664efb.gif","https://78.media.tumblr.com/46df86518bb415e8e02d6006203b3b29/tumblr_p8j08xiytj1t0lt8go1_540.gif"]
nyaos = ["https://2.bp.blogspot.com/-Hbon84eGYck/WuE6Ey2SEcI/AAAAAAABK6Q/BGlNvtsFbhoegepadqsQQwgGrXgBb3YMgCKgBGAs/s1600/Omake%2BGif%2BAnime%2B-%2BComic%2BGirls%2B-%2BEpisode%2B3%2B-%2BNyaos-sensei%2BWears%2Ba%2BHat.gif","https://4.bp.blogspot.com/-AP3bexfpCWc/Wv4DXMuVchI/AAAAAAABMjw/8ip2I7gbSRMDVTUGWaSm-pwQ4uaYvZFRgCKgBGAs/s1600/Omake%2BGif%2BAnime%2B-%2BComic%2BGirls%2B-%2BEpisode%2B7%2B-%2BSad%2BNyaos-Sensei.gif"]

zero_two = ["https://i.pinimg.com/originals/63/ca/58/63ca58fb23c0901176abf1787fa3bfce.gif","https://thumbs.gfycat.com/WideeyedFriendlyBongo-size_restricted.gif","https://media1.tenor.com/images/bfce835bfaf2d1176d490a0491de6b71/tenor.gif?itemid=12138790","https://i.redd.it/ldqbw71khjx01.gif","https://data.whicdn.com/images/309832622/original.gif"]

emilia = ["https://media.giphy.com/media/6srDH6BmmaMvK/giphy.gif","https://media.giphy.com/media/KvoLqIZle18Tm/giphy.gif","https://66.media.tumblr.com/fe779fcee196b534f2dfda13e8eb9de4/tumblr_ottqn7ya8c1v14hqvo1_500.gif","http://pa1.narvii.com/6145/fb722551559221f7dbed9e44299856f507c4222f_hq.gif"]

#generating the fun gif lists
kiss = ["https://thumbs.gfycat.com/FondEvergreenIcterinewarbler-size_restricted.gif","https://media1.tenor.com/images/105a7ad7edbe74e5ca834348025cc650/tenor.gif?itemid=9158317","https://i.imgur.com/sGVgr74.gif","https://pa1.narvii.com/5746/28adf462fa4a2391fb044405655c67b8f5f1c7b9_hq.gif","https://lh3.googleusercontent.com/-Tncc7L3z88A/WvODFn1dO7I/AAAAAAAKy4A/gPGnvMieeeQTVnhNO3ioc679FRhPDxDzwCJoC/w530-h298-n-rw/Omake%2BGif%2BAnime%2B-%2BDarling%2Bin%2Bthe%2BFranXX%2B-%2BOP%2B-%2BZero%2BTwo%2BKisses%2BHiro.gif","https://media1.tenor.com/images/b6e36a6ed9b963e0f004bc0558405cb2/tenor.gif?itemid=12307773","https://data.whicdn.com/images/109154232/original.gif","http://24.media.tumblr.com/05f0f56f99dadb710e7307ebeac24129/tumblr_mzu1bv7dU61qbvovho1_500.gif"]
hug = ["https://i.imgur.com/wOmoeF8.gif","https://media.giphy.com/media/xJlOdEYy0r7ZS/giphy.gif","http://i.imgur.com/tuH4gqZ.gif","https://i.pinimg.com/originals/02/7e/0a/027e0ab608f8b84a25b2d2b1d223edec.gif","http://49.media.tumblr.com/ce3aad3f1d570fa06c253abfccf36d1b/tumblr_msexao8iX51re6rdoo1_500.gif","https://cdn.weeb.sh/images/r1v2_uXP-.gif","https://cdn.weeb.sh/images/HyNJIaVCb.gif","https://cdn.weeb.sh/images/S1a0DJhqG.gif","https://cdn.weeb.sh/images/S1a0DJhqG.gif","https://cdn.weeb.sh/images/HyllFdmwZ.gif","https://cdn.weeb.sh/images/Sk80wyhqz.gif","https://cdn.weeb.sh/images/rkYetOXwW.gif"]
lick = ["https://cdn.weeb.sh/images/Bkxge0uPW.gif","https://cdn.weeb.sh/images/rJ6hrQr6-.gif","https://cdn.weeb.sh/images/BkvTBQHaZ.gif","https://cdn.weeb.sh/images/S1Ill0_vW.gif","https://cdn.weeb.sh/images/Hkknfs2Ab.gif","https://cdn.weeb.sh/images/Bkagl0uvb.gif","https://cdn.weeb.sh/images/Sk15iVlOf.gif"]

#generating the wiafu list
waifus = [kanna,tohru,kobayashi,lucoa,saikawa,megumin,aqua,darkness,satou,kaos,ruki,tsubasa,koyume,fuura,nyaos,zero_two,emilia]
waifus2 = ["kanna","tohru","kobayashi","lucoa","saikawa","megumin","aqua","darkness","satou","kaos","ruki","tsubasa","koyume","fuura","nayos","zero_two","emilia"]
avaliablewiafu = ""
for x in range(0,int(len(waifus2))):
    avaliablewiafu = avaliablewiafu + waifus2[x] + ", "

#generating the fun gifs list
fun = [kiss,hug,lick]
fun2 = ["kiss","hug","lick"]
avaliablefun = ""
for x in range(0,int(len(fun2))):
    avaliablefun = avaliablefun + fun2[x] + ", "

#the actual messaging part of the bot
@client.event
async def on_message(message):

    #making sure the bot doesnt message itself
    if message.author == client.user:
        return
    
    #making the help command
    if message.content.startswith(prefix + 'help'):
        embed = discord.Embed(
             description = ("Just type " + prefix + "wiafus to get a lits of avaliable wiafus \n\n Type " + prefix + " folowed by a name of a waifu in order to get a gif of that character \n\n we also have " + prefix + "random which will randomly sellect a gif at random! \n\n  finally we have the interactive section of the bot, this will allow you to do things like hug or kiss others, you can type" + prefix + "fun in order to see what fun gifs are avaliable"),
             colour = discord.Colour.magenta()
             )
        embed.set_author(name="Help", icon_url="https://cdn.discordapp.com/app-icons/486911878996557839/17fd735ea2a33f992274583814498ee7")
        await client.send_message(message.channel, embed=embed)

    #specific wiafu
    if message.content.replace(prefix, "") in waifus2:
        embed = discord.Embed(
            colour = discord.Colour.magenta()
            )
        embed.set_image(url= random.choice(waifus[waifus2.index(message.content.replace(prefix, ""))]))
        embed.set_author(name="Here is your gif OwO", icon_url="https://cdn.discordapp.com/app-icons/486911878996557839/17fd735ea2a33f992274583814498ee7")
        await client.send_message(message.channel, embed=embed)

    #fun commands
    if "@" in message.content and message.content[1 : message.content.index("@") - 2] in fun2:
        msg = (message.content[message.content.index("@") - 1 : len(message.content)]).format(message)
        await client.send_message(message.channel, msg)
        embed = discord.Embed(
            colour = discord.Colour.magenta()
            )
        embed.set_image(url= random.choice(fun[fun2.index(message.content[1 : message.content.index("@") - 2])]))
        embed.set_author(name="you recieved a " + message.content[1 : message.content.index("@") - 2] +  " from " + str(message.author), icon_url="https://cdn.discordapp.com/app-icons/486911878996557839/17fd735ea2a33f992274583814498ee7")
        await client.send_message(message.channel, embed=embed)

    #/fun section of the bot
    if message.content.startswith(prefix + 'fun'):
        embed = discord.Embed(
            description = ("Hello, you can currently " + avaliablefun),
            colour = discord.Colour.magenta()
            )
        embed.set_author(name="Here is your gif OwO", icon_url="https://cdn.discordapp.com/app-icons/486911878996557839/17fd735ea2a33f992274583814498ee7")
        await client.send_message(message.channel, embed=embed)

    #random wiafu function of the bot
    if message.content.startswith(prefix + 'random'):
        embed = discord.Embed(
                colour = discord.Colour.magenta()
                )
        embed.set_image(url= random.choice(random.choice(waifus)))
        embed.set_author(name="Here is your random gif OwO", icon_url="https://cdn.discordapp.com/app-icons/486911878996557839/17fd735ea2a33f992274583814498ee7")
        await client.send_message(message.channel, embed=embed)

    #the wiafus function of the bots
    if message.content.startswith(prefix + 'wiafus'):
        embed = discord.Embed(
            description = ("Hello, we currently have " + avaliablewiafu),
            colour = discord.Colour.magenta()
            )
        embed.set_author(name="Here is your gif OwO", icon_url="https://cdn.discordapp.com/app-icons/486911878996557839/17fd735ea2a33f992274583814498ee7")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith(prefix + 'waifus'):
        embed = discord.Embed(
            description = ("Hello, we currently have " + avaliablewiafu),
            colour = discord.Colour.magenta()
            )
        embed.set_author(name="Here is your gif OwO", icon_url="https://cdn.discordapp.com/app-icons/486911878996557839/17fd735ea2a33f992274583814498ee7")
        await client.send_message(message.channel, embed=embed)

    #the owo function of the bot
    if 'OWO' in message.content.upper():
        msg = ("{0.author.mention} whats this?" ).format(message)
        await client.send_message(message.channel, msg)

#some info about the bot loging in
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#actually connecting the bot
client.run(os.getenv("TOKEN"))
