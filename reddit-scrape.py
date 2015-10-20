import xml.etree.cElementTree as ET
import urllib2
from bs4 import BeautifulSoup

reddit = urllib2.urlopen('http://www.reddit.com/')
soup = BeautifulSoup(reddit, 'html.parser')
test = soup.find("p")
fp_ranks = soup.findAll("span", class_="rank")
top_rank = fp_ranks[len(fp_ranks)%25]
top_post = top_rank.parent.find("a", class_="title")

response = ET.Element("Response")

ET.SubElement(response, "Say", voice="alice").text = "Robert Krabek"
ET.SubElement(response, "Say", voice="alice").text = top_post.string

file = ET.ElementTree(response)
file.write("response.xml")
