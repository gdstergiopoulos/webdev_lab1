#up1083861 Lab 1- Web Dev
#HTTP headers get-response
import requests  # εισαγωγή της βιβλιοθήκης
# import re
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
    


    print("\n")
    cookiename_list=[]
    x=response.cookies.get_dict().keys()
    for i in x:
        print("Cookie Name: "+i)

    print("\nNote:\nSta proigoumena commits exei ginei prospathia gia ektiposi ton info xoris xrisi regex (ipothike sto lab oti den xreiazetai)\nGia site me polla cookies parousiaze lathi opote ekana\nroll back se mia ekdosi opou ektiponontai ta names ton cookies alla kai olo to Set-Cookie mesa sto opoio fainontai ta expire dates")
    

    

   