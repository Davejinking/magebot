import asyncio
import discord
import os

client = discord.Client()
# 봇이 구동되었을 때 동작되는 코드입니다.
@client.event
async def on_ready():
    print("Logged in as ") #화면에 봇의 아이디, 닉네임이 출력됩니다.
    print(client.user.name)
    print(client.user.id)
    print("===========")
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
    await client.change_presence(game=discord.Game(name="닌겐 감시", type=1))
# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith("!롤"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)

        url = "http://www.op.gg/summoner/userName=" + enc_location
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        rank1 = bsObj.find("div", {"class": "TierRankInfo"})
        rank2 = rank1.find("div", {"class": "TierRank"})
        rank3 = rank2.find("span", {"class": "tierRank"})
        rank4 = rank3.text  # 티어표시 (브론즈1,2,3,4,5 등등)
        print(rank4)
        if rank4 != 'Unranked':
          jumsu1 = rank1.find("div", {"class": "TierInfo"})
          jumsu2 = jumsu1.find("span", {"class": "LeaguePoints"})
          jumsu3 = jumsu2.text
          jumsu4 = jumsu3.strip()#점수표시 (11LP등등)
          print(jumsu4)

          winlose1 = jumsu1.find("span", {"class": "WinLose"})
          winlose2 = winlose1.find("span", {"class": "wins"})
          winlose2_1 = winlose1.find("span", {"class": "losses"})
          winlose2_2 = winlose1.find("span", {"class": "winratio"})

          winlose2txt = winlose2.text
          winlose2_1txt = winlose2_1.text
          winlose2_2txt = winlose2_2.text #승,패,승률 나타냄  200W 150L Win Ratio 55% 등등

          print(winlose2txt + " " + winlose2_1txt + " " + winlose2_2txt)

        channel = message.channel
        embed = discord.Embed(
            title='롤 정보',
            description='롤 정보입니다.',
            colour=discord.Colour.green()
        )
        if rank4=='Unranked':
            embed.add_field(name='당신의 티어', value=rank4, inline=False)
            embed.add_field(name='-당신은 언랭-', value="언랭은 더이상의 정보는 제공하지 않습니다.", inline=False)
            await client.send_message(channel, embed=embed)
        else:
         embed.add_field(name='당신의 티어', value=rank4, inline=False)
         embed.add_field(name='당신의 LP(점수)', value=jumsu4, inline=False)
         embed.add_field(name='당신의 승,패 정보', value=winlose2txt+" "+winlose2_1txt, inline=False)
         embed.add_field(name='당신의 승률', value=winlose2_2txt, inline=False)
         await client.send_message(channel, embed=embed)

    if message.content.startswith('!명령어'): #만약 해당 메시지가 '!커맨드' 로 시작하는 경우에는
        await client.send_message(channel, '!help')
    else: #위의 if에 해당되지 않는 경우
        #메시지를 보낸사람을 호출하며 말한 메시지 내용을 그대로 출력해줍니다.
        await client.send_message(channel, "<@"+id+"> 네놈이 \""+message.content+"\"라고 기침소리를 내었는가")




access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
