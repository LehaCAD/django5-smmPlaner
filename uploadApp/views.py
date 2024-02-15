from django.shortcuts import render
from telethon import TelegramClient, events, sync
from django.http import HttpResponse
from telethon.tl.types import PeerChannel
from .models import Post
from .forms import PostForm
import requests
import time
import asyncio, os
from telegram import settings
from pathlib import Path
from asgiref.sync import sync_to_async
from telethon.tl.types import DocumentAttributeVideo
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
# from .tasks import async_success


def handle_uploaded_file(f):
    with open(f"MEDIA/files/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

async def success(request):
    client = await startClient()
    await upload_post(request)

    await asyncio.sleep(1)
    message = await get_message()
    user_list = await get_user_list(request)
    # print(user_list)
    form = PostForm()
    file = await get_path()
    # print('ПУТЬ ТУТ СУКА: ' + str(file))
    result = file
    attributes = await get_file_attributes(file)
    await send_to_many_people(user_list, client, result, attributes, message)
    await disconnectClient(client)
    return render(request,'uploadApp/uploadForm.html', {'form':form, 'uspeh':'успех!'})


async def send_to_many_people(user_list, client, result, attributes, message):
    for user in user_list:
        await client.send_file(user, file = result, supports_streaming=True, attributes=attributes, caption = message)
        await asyncio.sleep(1)

@sync_to_async
def get_file_attributes(file):
    parser = createParser(str(file))
    metadata = extractMetadata(parser)
    duration = metadata.get('duration').seconds if metadata.has('duration') else 0
    width = metadata.get('width') if metadata.has('width') else 0
    height = metadata.get('height') if metadata.has('height') else 0

    attributes = [DocumentAttributeVideo(
    w = width,
    h = height,
    duration = duration
)]

async def upload_to_client(file):
    result =''
    if os.path.exists(file):
        with open(file, 'rb') as file:
            result = await client.upload_file(file)
            return result

async def disconnectClient(client):
    await client.disconnect()

async def startClient():
    api_id = ''
    api_hash = ''
    client = TelegramClient('NikitaSes', api_id, api_hash, device_model="Window11_AlexeyAs", system_version="12,4")
    await client.start()
    await client.connect()
    return client

@sync_to_async
def get_path():
    last_post =  Post.objects.latest('id')
    file_path =  last_post.file_path.url
    full_path = str(settings.BASE_DIR) + file_path
    return full_path

@sync_to_async
def get_message():
    last_post =  Post.objects.latest('id')
    description =  last_post.description
    return description

@sync_to_async
def get_user_list(request):
    users =[]
    for i in range(1, 6):  # Перебираем все 5 введенных имен
        username = request.POST.get(f'username{i}')
        if username:
            users.append(username)
    return users



@sync_to_async
def upload_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        form.save()
        return render(request,'uploadApp/uploadForm.html', {'form':form})
    else:
        form = PostForm()
        return render(request,'uploadApp/uploadForm.html', {'form':form})
