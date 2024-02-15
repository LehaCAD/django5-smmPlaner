# from django.shortcuts import render
# from telethon import TelegramClient, events, sync
# from django.http import HttpResponse
# from telethon.tl.types import PeerChannel
# from .models import Post
# from .forms import PostForm
# import requests
# import time
# import asyncio, os
# from telegram import settings
# from pathlib import Path
# from asgiref.sync import sync_to_async
# from telethon.tl.types import DocumentAttributeVideo
# from hachoir.parser import createParser
# from hachoir.metadata import extractMetadata
# from celery import shared_task
#
#
#
#     client = await startClient()
#     upload_post(request)
#
#     await asyncio.sleep(1)
#     message = await get_message()
#     user_list = await get_user_list(request)
#     print(user_list)
#     form = PostForm()
#     file = await get_path()
#
#     full_path = str(settings.BASE_DIR) + file
#     print('ПУТЬ ТУТ СУКА: ' + str(full_path))
#     result =''
#     if os.path.exists(full_path):
#         with open(full_path, 'rb') as file:
#             result = await client.upload_file(file)
#
#     parser = createParser(str(full_path))
#     metadata = extractMetadata(parser)
#     duration = metadata.get('duration').seconds if metadata.has('duration') else 0
#     width = metadata.get('width') if metadata.has('width') else 0
#     height = metadata.get('height') if metadata.has('height') else 0
#
#     attributes = [DocumentAttributeVideo(
#     w = width,
#     h = height,
#     duration = duration
# )]
#
#     for user in user_list:
#         await client.send_file(user, file = result, supports_streaming=True, attributes=attributes, caption = message)
#         await asyncio.sleep(1)
#     await disconnectClient(client)
#     return render(request,'uploadApp/uploadForm.html', {'form':form, 'uspeh':'успех!'})
#
#
#
#
# async def disconnectClient(client):
#     await client.disconnect()
#
# async def startClient():
#     api_id = '27719948'
#     api_hash = '262979569d87119356cc493e4b5e7d1c'
#     client = TelegramClient('NikitaSes', api_id, api_hash, device_model="Window11_AlexeyAs", system_version="12,4")
#     await client.start()
#     await client.connect()
#     return client
#
# @sync_to_async
# def get_path():
#     last_post =  Post.objects.latest('id')
#     file_path =  last_post.file_path.url
#     return file_path
#
# @sync_to_async
# def get_message():
#     last_post =  Post.objects.latest('id')
#     description =  last_post.description
#     return description
# @sync_to_async
#
# def get_user_list(request):
#     users =[]
#     for i in range(1, 6):  # Перебираем все 5 введенных имен
#         username = request.POST.get(f'username{i}')
#         if username:
#             users.append(username)
#     return users
