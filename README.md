# reddit-call
python script that scrapes the title of the top post on reddit and makes a call with the Twilio API saying my name and the title of the post

schedule using the at daemon
schedule reddit-scrape.py 1 minute before autocall.py to give dropbox time to update xml file

urllib2 and beautifulsoup to scrape reddit by accessing the sibling element of the top rank tag
xmletree to write the TwiML file to the Dropbox/Public directory so it can be accessed by autocall.py