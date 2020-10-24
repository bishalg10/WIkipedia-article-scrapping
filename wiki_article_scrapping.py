from urllib.request import urlopen as uReq   #urllib grabs the parsed page
from bs4 import BeautifulSoup as soup        #BeautifulSoup parse HTML tag

# Wikipedia webpage source of the article
my_url = 'https://en.wikipedia.org/wiki/Pokhara_Valley'

#Opens up connection, grabbing the page
uClient = uReq(my_url) 			
page_html = uClient.read()
uClient.close()

#HTML parsing
article_soup = soup(page_html, "html.parser")  

#Grabs every detail of the article
container = article_soup.findAll("div",{"id":"bodyContent"})
cont = container[0]

#Gets the main heading of the article
main_heading = article_soup.findAll("h1",{"class":"firstHeading"})
article_main_heading = main_heading[0].text

#Gets the source of the article
source = cont.div.text

#Gets the description of the article
description = cont.p.text

#Gets all the main heading 
headlines = cont.findAll("span",{"class","mw-headline"})

#Gets all the paragraph that are inside p tag
paragraph = cont.findAll("p")

#Creating a .txt file
filename = "article.txt"

#Opening a new file article.txt
file_write = open(filename,"w+")    
file_write.write('Source:' + source + '\n' + article_main_heading + '\n' + description + '\n')

#Printing article detail in the console
print('Source:' + source)
print(article_main_heading)
print(description)

#Concanating two for loops for joing the heading and paragraph respectively.
for i in range(len(headlines)-4): 			#Reads 3 headings of the article
	title_head = headlines[i].text 
	print(title_head)				        #Prints the headling in text format without any HTML tags. 
	if i == len(headlines) - 2:				#Stops the iteration of the integer at the specified number.
		continue
	elif i > len(headlines) - 2:
		paragraph_detail = paragraph[i].text
		print(paragraph_detail)					#Iterate the paragraph through the index number
	else:
		paragraph_detail = paragraph[i+1].text
		#Prints text without HTML tags
		print(paragraph[i+1].text)											
		#Writing the detail of article in the .txt file
		file_write.write(title_head + '\n' +paragraph_detail + '\n')        
file_write.close() 	   #Closing the file



