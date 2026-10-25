from bs4 import BeautifulSoup
with open('itgen.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
#print(soup.prettify())
#print(soup.title.name)

heading = soup.find(name="h1", id="name")
#print(heading)

all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)

#for tag in all_anchor_tags:
  #print(tag.getText())
  #print(tag.get("href"))

section_heading = soup.find(name="h3", class_="heading")
#print(section_heading)

name = soup.select_one(selector="#name")
#print(name)

headings = soup.select(selector=".heading") 
#print(headings)

teach = soup.find_all(name='p')
print(teach[1].text)