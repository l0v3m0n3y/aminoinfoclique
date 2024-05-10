import AminoLab

async def get_global_user_info():
    client = AminoLab.AminoLab()
    link_info = await client.get_from_link(input("User Link >> "))
    user_info = await client.get_user_info(user_Id=link_info.object_Id)
    print(
        f"""User Info:
account created time >> {user_info.createdTime}
nickname >> {user_info.nickname}
content >> {user_info.content}
icon link >> {user_info.icon}
user_Id >> {link_info.object_Id}
amino_Id >> {user_info.amino_Id}
web_url >> {user_info.web_URL}"""
    )

async def get_chat_info():
    client = AminoLab.AminoLab()
    link_info = await client.get_from_link(input("Chat Link >> "))
    ndc_Id = link_info.ndc_Id; thread_Id = link_info.object_Id
    chat_info = await client.get_thread(ndc_Id=ndc_Id, thread_Id=thread_Id)
    chat_info=chat_info["thread"]
    print(
        f"""Chat info:
title >> {chat_info['title']}
content >> {chat_info['content']}
members_count >> {chat_info['membersCount']}
tippers_count >> {chat_info['tipInfo']['tippersCount']}
tipped_coins >> {chat_info['tipInfo']['tippedCoins']}
thread_Id >> {thread_Id}
"""
    )

async def get_account_info():
    client = AminoLab.AminoLab()
    email = input("Email >> ")
    password = input("Password >> ")
    await client.auth(email=email, password=password)
    account_info = await client.get_account_info()
    account_info = account_info["account"]
    print(
        f"""Account info:
account created time >> {account_info['createdTime']}
email >> {account_info['email']}
phoneNumber >> {account_info['phoneNumber']}
password >> {password}
nickname >> {account_info['nickname']}
user_Id >> {account_info['uid']}
amino_Id >> {account_info['aminoId']}"""
    )