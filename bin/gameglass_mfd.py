from os import system
from os.path import join, dirname, abspath
from json import load
from tracemalloc import start
from webview import create_window, start
from requests import get

system("cls")

print("------------------------------------------")
print("             Project Astraeus             ")
print("------------------------------------------")

quick_url = ""
base_url = "https://app.gameglass.gg/shardlibrary/"

print("Checking internet connection...", flush=True, end=" ")
while True:
    try:
        get('https://google.com/', timeout=1).status_code
        break
    except:
        pass
print("Success")

print("Loading configuration file...", flush=True, end=" ")
try:
    base_path = dirname(abspath(__file__))
    conf_path = join(base_path, "gameglass_conf.json")
    with open(conf_path) as file:
        conf_json = load(file)
    
    print("Success")

    print("Checking for quick URL...", flush=True, end=" ")
    if conf_json["quick_url"]:
        print("Success")
        print("")

        quick_url = conf_json["quick_url"]
        print("Library ID:", quick_url.split("/")[0])
        print("Shard ID:", quick_url.split("/")[1].split("?")[0])
        print("Config ID:", quick_url.split("/")[1].split("?")[1].split("=")[1])
    else:
        print("Fail")
except:
    print("Fail")

print("")
print("Starting webview application...", flush=True, end=" ")

toggle_fullscreen = lambda window: window.toggle_fullscreen()

window = create_window("Project Astraeus", base_url + quick_url)
start(toggle_fullscreen, window)
print("Success")
