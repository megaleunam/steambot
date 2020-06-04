#!/usr/bin python3
import os

from django.core.management.base import BaseCommand
from asgiref.sync import async_to_sync

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/commands/'


class Command(BaseCommand):
    help = ""

    # A commands must define handle()
    def handle(self, *args, **options):
        # Enviar un mensaje al cliente.
        async_to_sync(channel_layer.group_send)(
                "bot",
                {   
                    "type": "chat.message",
                    "text": "Hola un nuevo mensaje",
                },
            )

