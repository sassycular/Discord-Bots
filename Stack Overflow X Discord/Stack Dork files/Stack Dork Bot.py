# Created for Strawhats DAO in May 2022
# This is a Python and Selenium based bot 
# Ran this bot on Repl.it so there's some things you need to do before you can run Selenium on Repl.it
# This bot can take your question from a Discord server that its added to and post it on your StackOverflow Teams page 
# The code is 'well commented' for understanding
# Type $post and write your question although you can change this command in the code to whatever you like 
# Created in collaboration with Krypto Kiddo The First XD 

# Discord token for the bot is called sauce because I bring the sauce ;)

import discord
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time  # i can control time :3 

class questionObject:
  title = ""  # String Title
  body = ""  # Long String Body
  tags = []  # Linear array of tags
  # skipping tagged people attribute for now

def upload(question):
# Setting up options to run on repl
 chrome_options = Options()
 chrome_options.add_argument('--no-sandbox')
 chrome_options.add_argument('--disable-dev-shm-usage')

# Not needed now. Implement later.
# To make selenium-chrome run in a headless state
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
 browser = webdriver.Chrome(options=chrome_options)

# Initialising Browser to team page
# Change the link to your teams page
 browser.get("https://www.stackoverflow.com/c/UwU")
 time.sleep(5)

# Accepting Cookies
 evilBtn = browser.find_element_by_class_name("js-accept-cookies")
 evilBtn.click()

# Click on "I already have an account" option to login
 loginRadio = browser.find_element_by_id("has-public-account-radio")
 loginRadio.click()

# Finding login elements
 email = browser.find_element_by_id("email")
 pwd = browser.find_element_by_id("password")
 submit = browser.find_element_by_id("submit-button")

# Interacting with login elements
 email.send_keys("stackbot@dndmeta.org")
 pwd.send_keys(os.environ['password'])
 submit.click()  # logs in successfully

# Navigating to new question page
 time.sleep(5)  
#need to give prev page time to load else the next get command doesnt work
 browser.get("https://stackoverflow.com/c/uwu/questions/ask")

# Driver code for question object, to be imported from JSON later
 Q = question
  
 title = browser.find_element_by_id("title")
 body = browser.find_element_by_class_name("js-editor")
 tagsBar = browser.find_element_by_id("tageditor-replacing-tagnames--input")
# (optional) ASK TEAM MEMBERS id: tageditor-replacing-mentionnames--input
 submit = browser.find_element_by_id("submit-button")

 title.send_keys(Q.title)
 body.send_keys(Q.body)

# Entering tags
 for tag in Q.tags:
  tagsBar.send_keys(tag)
  tagsBar.send_keys(" ")  # Spaces seperate tags on Stackoverflow

# finally submitting the question
 submit.click()
 time.sleep(1)  # waiting for the confirmation box to load

# If a tag is new:
 try:
  tagConfirmation = browser.find_element_by_class_name(
    "js-confirm-tag-creation")
  tagConfirmation.click()
 except:
  pass
   # This should be enough to post a question
 time.sleep(10)
 print("FUNCTION COMPLETE UWU")

# The discord part starts here
client = discord.Client()

@client.event 
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

# Feel free to customize the way you say hello :P
  if message.content.startswith('$hello'): 
    await message.channel.send('Hello!')

  if message.content.startswith('$post'):
    quesTitle = message.content.split("$post ")[-1]
    #this is in an if do not indent or unindent 
    Q = questionObject()
    Q.title = quesTitle
    Q.body = "This is the body text"
    Q.tags = ["Tag1", "Tag2", "Tag3", "Tag4"]
    upload(Q)
client.run(os.getenv('sauce'))

# Ok bye
