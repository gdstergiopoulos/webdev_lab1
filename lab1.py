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
        print("\nThis site does not use Cookies")
    else:
        print("\nThe site uses the Cookies bellow: \n")
        print(cookies)
    


    cookiename_list=[]
    x=response.cookies.get_dict().keys()
    for i in x:
        cookiename_list.append(i)
        # print(i)
    
    #An atempt to print only information needed, without the use of regex. It will not work if the field after the name of the cookie is not the expiration date.
    #the use of regex is not required (mentioned in lab)
    expiration_date=[]
    z=cookies.split(";")
    for i in range(0,len(z)):
        for j in cookiename_list:
            if j in z[i]:
                if("expires" in z[i+1]):
                    expiration_date.append(z[i+1])
                else:
                    expiration_date.append("Unknown")
            else:
                continue

    for i in range(len(cookiename_list)):
        print("Cookie name: "+cookiename_list[i]+" and "+expiration_date[i])


        

    

   