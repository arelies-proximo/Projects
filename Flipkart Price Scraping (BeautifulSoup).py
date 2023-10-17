from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

flipkart_url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

uclient = ureq(flipkart_url)
    #ureq opens up the connection, grabs the page and loads it
    #save it to a variable

page_html = uclient.read()
    #read the page; store it in the variable

uclient.close()

page_soup = soup(page_html, "html.parser")
    #to parse the html page since it is very large


containers = page_soup.findAll("div", {"class": "_3pLy-c row"})


#print(len(containers))
    #print total number of products in the container
    #ans = 24


#print(soup.prettify(containers[1]))
    #prettify; make the html contnent readable
    #we access the 1st container


#container = containers[0]


'''
title = container.findAll("div", {"class":"_4rR01T"})
print(title[0].text)
    #to print the title of the container

attributes = container.findAll("div", {"class":"fMghEO"})
text = attributes[0].text

print("RAM:",text[0:6])
st = text.find("12")

print("CAMERA:",text[st:st+31])

attributes = container.findAll("div", {"class":"_30jeq3 _1_WHN1"})
print("Price:",attributes[0].text)

attributes = container.findAll("div", {"class":"_3LWZlK"})
print("Rating:",attributes[0].text)
'''



newfile = "iphone.csv"

f = open(newfile,"w")
    #to store the data in the file
header = "Iphone Title,Price,Rating\n"

f.write(header)
i=0
#for all the iphones in the page_soup
for container in containers:
    attributes = container.findAll("div", {"class":"_4rR01T"})
    title = attributes[0].text
    title = title.replace(",", "|")

    attributes = container.findAll("div", {"class":"_30jeq3 _1_WHN1"})
    price = attributes[0].text
    price = price.replace(",", "")
    price = price.replace("₹", "Rs.")

    attributes = container.findAll("div", {"class":"_3LWZlK"})
    ratings = attributes[0].text

    print(title+","+price+","+ratings+"\n")
    f.write(title + "," + price + "," + ratings + "\n")

f.close()



