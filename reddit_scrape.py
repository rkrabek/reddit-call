import xml.etree.cElementTree as ET
from bs4 import BeautifulSoup

# parse reddit front page html
reddit = urllib2.urlopen('http://www.reddit.com/')
soup = BeautifulSoup(reddit, 'html.parser')

# find top post by finding rank 1 and then appropriate sibling sub-tag
fp_ranks = soup.findAll("span", class_="rank")
top_rank = fp_ranks[len(fp_ranks)%25]
top_post = top_rank.parent.find("a", class_="title")

# creates TwiML document with name and top post
response = ET.Element("Response")
ET.SubElement(response, "Say", voice="alice").text = "Robert Krabek"
ET.SubElement(response, "Say", voice="alice").text = top_post.string

# writes TwiML file to Dropbox Public directory accessible to autocall.py
file = ET.ElementTree(response)
file.write("../../Public/response.xml")
