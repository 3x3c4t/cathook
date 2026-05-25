import os
import requests


CAT1 = r"""
 /\_/\\
( o.o )
 > ^ <
"""

CAT2 = r"""
 /\_/\ 
( -.- )
 > ~ <
"""


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def is_file(x):
    x = x.strip('"')
    return os.path.isfile(x)


def send_text(url, msg):
    requests.post(url, json={"content": msg}, timeout=10)


def send_file(url, path):
    path = path.strip('"')
    with open(path, "rb") as f:
        requests.post(url, files={"file": f}, timeout=20)


def ui(history):
    clear()
    for m in history:
        print(f"{CAT2} {m}")


def main():
    os.system("title cathook")
    clear()
    print(CAT1)
    url = input("webhook > ").strip()

    clear()

    history = []

    while True:
        ui(history)

        msg = input("> ").strip()

        if msg.lower() in ["/exit", "/quit"]:
            break

        if not msg:
            continue

        try:
            if is_file(msg):
                send_file(url, msg)
                history.append("[image sent]")
            else:
                send_text(url, msg)
                history.append(msg)
        except:
            history.append("[failed]")


if __name__ == "__main__":
    main()