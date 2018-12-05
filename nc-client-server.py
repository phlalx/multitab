#!/usr/bin/env python3

from multitab import opentab
from time import sleep

app_dir = "~/"

server = [
  'echo starting server',
  'nc -l 8000'
]

client = [
  "echo 'hello' | nc localhost 8000"
]

opentab("Server", app_dir, server)

sleep(1)

opentab("Client", app_dir, client)
