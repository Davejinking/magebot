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

    if message.content.startswith('!명령어'): #만약 해당 메시지가 '!커맨드' 로 시작하는 경우에는
        await client.send_message(channel, '!help [command] -명령 목록을 인쇄하거나 명령 정보가 지정된 경우 정보를 인쇄합니다.')
        await client.send_message(channel, '!play <URL/query> -특정 URL에서 오디오를 재생하거나 YouTube에서 검색어를 검색하고 첫 번째 결과를 대기열에 넣습니다.')
        await client.send_message(channel, '!queue -대기중인 모든 미디어를 표시합니다.')
        await client.send_message(channel, '!np -현재 재생중인 미디어를 표시합니다.')
        await client.send_message(channel, '!skip-현재 미디어를 건너뛰기')
        await client.send_message(channel, '!search [service] [#] <query>-특정 서비스 (기본값 : YT)에서 쿼리를 검색하고 처음 몇 개의 결과 (기본값 : 3, 제한 : 10)를 반환합니다. 그런 다음 사용자는 대기열에 항목을 추가하려는 경우 결과에서 선택할 수 있습니다.')
    else: #위의 if에 해당되지 않는 경우
        #메시지를 보낸사람을 호출하며 말한 메시지 내용을 그대로 출력해줍니다.
        await client.send_message(channel, "<@"+id+"> 네놈이 \""+message.content+"\"라고 기침소리를 내었는가")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
