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
        print(f"The server is {server}")
    else:
        print("No server found")

    #c) cookies and expiration
    cookies=response.headers.get("Set-Cookie")
    cooklist=response.cookies.itervalues()
    # print(cooklist)
    # print(cookies)

    x=cookies.split(",")
    print(x)
    pattern = r'(\w+)=.*?expires=([A-Za-z]+), (\d{2}-[A-Za-z]+-\d{4})'

    # Find all matches
    matches = re.findall(pattern, cookies)

    # Iterate over matches and print cookie name and expiration date
    for match in matches:
        cookie_name = match[0]
        expiration_time = match[2]
        print(f"Cookie Name: {cookie_name}, Expiration Date: {expiration_time}")