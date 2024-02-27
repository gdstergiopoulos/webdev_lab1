import requests  # εισαγωγή της βιβλιοθήκης
import re
def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

url = input("Insert a valid URL: ")  # προσδιορισμός του url


with requests.get(url) as response:  # το αντικείμενο response
    # html = response.text
    # more(html)

    #a) print headers
    headers=response.headers
    print("Website Headers are: \n",headers)

    #b) the sw that the server uses to response
    server= response.headers.get("Server")
    if server:
        print(f"\nThe server is {server}")
    else:
        print("No server found")

    #c) cookies and expiration
    cookies=response.headers.get("Set-Cookie")
    if (cookies==None):
        print("This site does not use Cookies")
    else:
        print("\nThe site uses the Cookies bellow: \n")
        print(cookies)

   