import pytest
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# Create your tests here.

class PlayerFormTest(LiveServerTestCase):
  def test_website_chrome(self):
    options = ChromeOptions()
    options.add_argument('--hide-scrollbars')
    options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--window-size=1920,1080')
    options.add_argument("--disable-popup-blocking")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    driver.get('http://127.0.0.1:8000/')
    WebDriverWait(driver, 10)
    assert driver.current_url == "http://127.0.0.1:8000/"
    assert driver.title == "Player Database"

    try:  # Asserts visibility of navbar at top
      WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > nav')))
      found = True
    except:
      found = False
    assert found

    try:  # Asserts visibility of pictures below navbar
      WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > center')))
      found = True
    except:
      found = False
    assert found
    # Asserting the images are what you expect them to be
    identical_gifs = [driver.find_element(By.CSS_SELECTOR, 'body > center > img:nth-child(1)'), driver.find_element(By.CSS_SELECTOR, 'body > center > img:nth-child(3)')]
    for gif in identical_gifs:
      assert gif.get_attribute("src") == "https://thumbs.gfycat.com/BaggyAdorableFairybluebird-size_restricted.gif"
    assert driver.find_element(By.CSS_SELECTOR, 'body > center > img:nth-child(2)').get_attribute("src") == "https://www.freepnglogos.com/uploads/nba-logo-png/nba-stats-logo-documentation-with-examples-slothparadise-11.png"
    
    try:  # Asserts visibility of form and buttons below
      WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div:nth-child(5) > form')))
      found = True
    except:
      found = False
    assert found

    #find the elements you need to submit form
    player_name = driver.find_element(By.CSS_SELECTOR, '#id_name')
    player_height = driver.find_element(By.CSS_SELECTOR, '#id_height')
    player_team = driver.find_element(By.CSS_SELECTOR, '#id_team')
    player_ppg = driver.find_element(By.CSS_SELECTOR, '#id_ppg')

    submit = driver.find_element(By.CSS_SELECTOR, '#submit_button')

    #populate the form with data

    player_name.send_keys('Arnit Ibrahimovic')
    player_team.send_keys('LA Bakers')
    player_height.send_keys('6 foot 2 on dates')
    player_ppg.send_keys('27.2')

    submit.send_keys(Keys.RETURN)
    #check result; page source looks at entire html document
    assert 'Arnit Ibrahimovic' in driver.page_source

    # entering second (polls) page by a button in the first page
    enter_polls_page = driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(5) > form > a')
    enter_polls_page.click()
    assert driver.current_url == "http://127.0.0.1:8000/polls/"
    assert driver.find_element(By.CSS_SELECTOR, 'body > font').text == "NBA Polls:"
    assert driver.find_element(By.CSS_SELECTOR, 'body > ul > li > a').text == "Who's the GOAT in basketball?"
    assert driver.find_element(By.CSS_SELECTOR, 'body > a').text == "Go to Player Database"

    click_on_first_poll = driver.find_element(By.CSS_SELECTOR, 'body > ul > li > a')
    click_on_first_poll.click()
    assert driver.current_url == 'http://127.0.0.1:8000/polls/specifics/5/'
    
    try:  # Asserts the poll and vote buttons are visible
      WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > form')))
      found = True
    except:
      found = False
    assert found
    
    assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > legend > h1').text == "Who's the GOAT in basketball?"
    assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(3)').text == "Michael Jordan"
    assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(6)').text == "Lebron James"
    assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(9)').text == "Kobe Bryant"
    assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(12)').text == "Steph Curry"
    assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(15)').text == "Magic Johnsen"
    
    vote_button = driver.find_element(By.CSS_SELECTOR, 'body > form > input[type=submit]:nth-child(3)')
    assert vote_button.get_attribute("value") == "Vote"
    assert driver.find_element(By.CSS_SELECTOR, 'body > a').text == "Go back to Polls"

    # attempting to vote without choosing, which should give a popup message 
    vote_button.click()
    try:
      WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > form > fieldset > p > strong')))
      found = True
    except:
      found = False
    assert found
    assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > p > strong').text == "You didn't select a choice."
    
    click_choice_1 = driver.find_element(By.CSS_SELECTOR, '#choice1')
    click_choice_1.click()
    driver.find_element(By.CSS_SELECTOR, 'body > form > input[type=submit]:nth-child(3)').click()
    assert driver.current_url == "http://127.0.0.1:8000/polls/5/results/"
    
    votes_text = driver.find_element(By.CSS_SELECTOR, 'body > ul > li:nth-child(1)').text
    num1 = ""
    for c in votes_text:
      if c.isdigit():
        num1 = num1 + c
    votes_text = driver.find_element(By.CSS_SELECTOR, 'body > ul > li:nth-child(2)').text
    num2 = ""
    for c in votes_text:
      if c.isdigit():
        num2 = num2 + c
    votes_text = driver.find_element(By.CSS_SELECTOR, 'body > ul > li:nth-child(3)').text
    num3 = ""
    for c in votes_text:
      if c.isdigit():
        num3 = num3 + c
    votes_text = driver.find_element(By.CSS_SELECTOR, 'body > ul > li:nth-child(4)').text
    num4 = ""
    for c in votes_text:
      if c.isdigit():
        num4 = num4 + c
    votes_text = driver.find_element(By.CSS_SELECTOR, 'body > ul > li:nth-child(5)').text
    num5 = ""
    for c in votes_text:
      if c.isdigit():
        num5 = num5 + c

    voter_info = driver.find_element(By.CSS_SELECTOR, 'body > ul')
    assert voter_info.text == """Michael Jordan -- """ + num1 + """ votes\nLebron James -- """+ num2 +""" vote\nKobe Bryant -- """+ num3 + """ vote\nSteph Curry -- """+ num4 + """ votes\nMagic Johnsen -- """+ num5 + """ votes"""
    driver.find_element(By.CSS_SELECTOR, 'body > a').click()
    assert driver.current_url == 'http://127.0.0.1:8000/polls/specifics/5/'

  def test_website_edge(self):
    options = EdgeOptions()
    options.add_argument('--hide-scrollbars')
    options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--window-size=1920,1080')
    options.add_argument("--disable-popup-blocking")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Edge(options=options)
    driver.implicitly_wait(10)

    driver.get('http://127.0.0.1:8000/')
    WebDriverWait(driver, 10)
    assert driver.current_url == "http://127.0.0.1:8000/"
    assert driver.title == "Player Database"

    try:  # Asserts visibility of navbar at top
      WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > nav')))
      found = True
    except:
      found = False
    assert found

    try:  # Asserts visibility of pictures below navbar
      WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > center')))
      found = True
    except:
      found = False
    assert found
    # Asserting the images are what you expect them to be
    identical_gifs = [driver.find_element(By.CSS_SELECTOR, 'body > center > img:nth-child(1)'), driver.find_element(By.CSS_SELECTOR, 'body > center > img:nth-child(3)')]
    for gif in identical_gifs:
      assert gif.get_attribute("src") == "https://thumbs.gfycat.com/BaggyAdorableFairybluebird-size_restricted.gif"
    assert driver.find_element(By.CSS_SELECTOR, 'body > center > img:nth-child(2)').get_attribute("src") == "https://www.freepnglogos.com/uploads/nba-logo-png/nba-stats-logo-documentation-with-examples-slothparadise-11.png"
    
    try:  # Asserts visibility of form and buttons below
      WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div:nth-child(5) > form')))
      found = True
    except:
      found = False
    assert found

    #find the elements you need to submit form
    player_name = driver.find_element(By.CSS_SELECTOR, '#id_name')
    player_height = driver.find_element(By.CSS_SELECTOR, '#id_height')
    player_team = driver.find_element(By.CSS_SELECTOR, '#id_team')
    player_ppg = driver.find_element(By.CSS_SELECTOR, '#id_ppg')

    submit = driver.find_element(By.CSS_SELECTOR, '#submit_button')

    #populate the form with data

    player_name.send_keys('Arnit Ibrahimovic')
    player_team.send_keys('LA Bakers')
    player_height.send_keys('6 foot 2 on dates')
    player_ppg.send_keys('27.2')

    submit.send_keys(Keys.RETURN)
    #check result; page source looks at entire html document
    assert 'Arnit Ibrahimovic' in driver.page_source

    # entering second (polls) page by a button in the first page
    enter_polls_page = driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(5) > form > a')
    enter_polls_page.click()
    assert driver.current_url == "http://127.0.0.1:8000/polls/"
    assert driver.find_element(By.CSS_SELECTOR, 'body > font').text == "NBA Polls:"
    assert driver.find_element(By.CSS_SELECTOR, 'body > ul > li > a').text == "Who's the GOAT in basketball?"
    assert driver.find_element(By.CSS_SELECTOR, 'body > a').text == "Go to Player Database"

    click_on_first_poll = driver.find_element(By.CSS_SELECTOR, 'body > ul > li > a')
    click_on_first_poll.click()
    assert driver.current_url == 'http://127.0.0.1:8000/polls/specifics/5/'
    
    try:  # Asserts the poll and vote buttons are visible
      WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > form')))
      found = True
    except:
      found = False
    assert found
    
    assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > legend > h1').text == "Who's the GOAT in basketball?"
    assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(3)').text == "Michael Jordan"
    assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(6)').text == "Lebron James"
    assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(9)').text == "Kobe Bryant"
    assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(12)').text == "Steph Curry"
    assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(15)').text == "Magic Johnsen"
    
    vote_button = driver.find_element(By.CSS_SELECTOR, 'body > form > input[type=submit]:nth-child(3)')
    assert vote_button.get_attribute("value") == "Vote"
    assert driver.find_element(By.CSS_SELECTOR, 'body > a').text == "Go back to Polls"

    # attempting to vote without choosing, which should give a popup message 
    vote_button.click()
    try:
      WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > form > fieldset > p > strong')))
      found = True
    except:
      found = False
    assert found
    assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > p > strong').text == "You didn't select a choice."
    
    click_choice_1 = driver.find_element(By.CSS_SELECTOR, '#choice1')
    click_choice_1.click()
    driver.find_element(By.CSS_SELECTOR, 'body > form > input[type=submit]:nth-child(3)').click()
    assert driver.current_url == "http://127.0.0.1:8000/polls/5/results/"
    
    votes_text = driver.find_element(By.CSS_SELECTOR, 'body > ul > li:nth-child(1)').text
    num1 = ""
    for c in votes_text:
      if c.isdigit():
        num1 = num1 + c
    votes_text = driver.find_element(By.CSS_SELECTOR, 'body > ul > li:nth-child(2)').text
    num2 = ""
    for c in votes_text:
      if c.isdigit():
        num2 = num2 + c
    votes_text = driver.find_element(By.CSS_SELECTOR, 'body > ul > li:nth-child(3)').text
    num3 = ""
    for c in votes_text:
      if c.isdigit():
        num3 = num3 + c
    votes_text = driver.find_element(By.CSS_SELECTOR, 'body > ul > li:nth-child(4)').text
    num4 = ""
    for c in votes_text:
      if c.isdigit():
        num4 = num4 + c
    votes_text = driver.find_element(By.CSS_SELECTOR, 'body > ul > li:nth-child(5)').text
    num5 = ""
    for c in votes_text:
      if c.isdigit():
        num5 = num5 + c

    voter_info = driver.find_element(By.CSS_SELECTOR, 'body > ul')
    assert voter_info.text == """Michael Jordan -- """ + num1 + """ votes\nLebron James -- """+ num2 +""" vote\nKobe Bryant -- """+ num3 + """ votes\nSteph Curry -- """+ num4 + """ votes\nMagic Johnsen -- """+ num5 + """ votes"""
    driver.find_element(By.CSS_SELECTOR, 'body > a').click()
    assert driver.current_url == 'http://127.0.0.1:8000/polls/specifics/5/'
  
  # def test_firefox_website(self):
  #   options = FirefoxOptions()
  #   options.add_argument('--hide-scrollbars')
  #   options.add_argument('--headless')
  #   options.add_argument('--ignore-certificate-errors')
  #   options.add_argument('--window-size=1920,1080')
  #   options.add_argument("--disable-popup-blocking")

  #   driver = webdriver.Firefox(options=options)
  #   driver.implicitly_wait(10)

  #   driver.get('http://127.0.0.1:8000/')
  #   WebDriverWait(driver, 10)
  #   assert driver.current_url == "http://127.0.0.1:8000/"
  #   assert driver.title == "Player Database"

  #   try:  # Asserts visibility of navbar at top
  #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > nav')))
  #     found = True
  #   except:
  #     found = False
  #   assert found

  #   try:  # Asserts visibility of pictures below navbar
  #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > center')))
  #     found = True
  #   except:
  #     found = False
  #   assert found
  #   # Asserting the images are what you expect them to be
  #   identical_gifs = [driver.find_element(By.CSS_SELECTOR, 'body > center > img:nth-child(1)'), driver.find_element(By.CSS_SELECTOR, 'body > center > img:nth-child(3)')]
  #   for gif in identical_gifs:
  #     assert gif.get_attribute("src") == "https://thumbs.gfycat.com/BaggyAdorableFairybluebird-size_restricted.gif"
  #   assert driver.find_element(By.CSS_SELECTOR, 'body > center > img:nth-child(2)').get_attribute("src") == "https://www.freepnglogos.com/uploads/nba-logo-png/nba-stats-logo-documentation-with-examples-slothparadise-11.png"
    
  #   try:  # Asserts visibility of form and buttons below
  #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div:nth-child(5) > form')))
  #     found = True
  #   except:
  #     found = False
  #   assert found

  #   #find the elements you need to submit form
  #   player_name = driver.find_element(By.CSS_SELECTOR, '#id_name')
  #   player_height = driver.find_element(By.CSS_SELECTOR, '#id_height')
  #   player_team = driver.find_element(By.CSS_SELECTOR, '#id_team')
  #   player_ppg = driver.find_element(By.CSS_SELECTOR, '#id_ppg')

  #   submit = driver.find_element(By.CSS_SELECTOR, '#submit_button')

  #   #populate the form with data

  #   player_name.send_keys('Arnit Ibrahimovic')
  #   player_team.send_keys('LA Bakers')
  #   player_height.send_keys('6 foot 2 on dates')
  #   player_ppg.send_keys('27.2')

  #   submit.send_keys(Keys.RETURN)
  #   #check result; page source looks at entire html document
  #   assert 'Arnit Ibrahimovic' in driver.page_source

  #   # entering second (polls) page by a button in the first page
  #   enter_polls_page = driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(5) > form > a')
  #   enter_polls_page.click()
  #   assert driver.current_url == "http://127.0.0.1:8000/polls/"
  #   assert driver.find_element(By.CSS_SELECTOR, 'body > font').text == "NBA Polls:"
  #   assert driver.find_element(By.CSS_SELECTOR, 'body > ul > li > a').text == "Who's the GOAT in basketball?"
  #   assert driver.find_element(By.CSS_SELECTOR, 'body > a').text == "Go to Player Database"

  #   click_on_first_poll = driver.find_element(By.CSS_SELECTOR, 'body > ul > li > a')
  #   click_on_first_poll.click()
  #   assert driver.current_url == 'http://127.0.0.1:8000/polls/specifics/5/'
    
  #   try:  # Asserts the poll and vote buttons are visible
  #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > form')))
  #     found = True
  #   except:
  #     found = False
  #   assert found
    
  #   assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > legend > h1').text == "Who's the GOAT in basketball?"
  #   assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(3)').text == "Michael Jordan"
  #   assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(6)').text == "Lebron James"
  #   assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(9)').text == "Kobe Bryant"
  #   assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(12)').text == "Steph Curry"
  #   assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(15)').text == "Magic Johnsen"
    
  #   vote_button = driver.find_element(By.CSS_SELECTOR, 'body > form > input[type=submit]:nth-child(3)')
  #   assert vote_button.get_attribute("value") == "Vote"
  #   assert driver.find_element(By.CSS_SELECTOR, 'body > a').text == "Go back to Polls"

  #   # attempting to vote without choosing, which should give a popup message 
  #   vote_button.click()
  #   try:
  #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > form > fieldset > p > strong')))
  #     found = True
  #   except:
  #     found = False
  #   assert found
  #   assert driver.find_element(By.CSS_SELECTOR, 'body > form > fieldset > p > strong').text == "You didn't select a choice."
    
  #   click_choice_1 = driver.find_element(By.CSS_SELECTOR, '#choice1')
  #   click_choice_1.click()
  #   driver.find_element(By.CSS_SELECTOR, 'body > form > input[type=submit]:nth-child(3)').click()
  #   assert driver.current_url == "http://127.0.0.1:8000/polls/5/results/"
    
  #   choice_1_votes = 51
  #   voter_info = driver.find_element(By.CSS_SELECTOR, 'body > ul')
  #   assert voter_info.text == """Michael Jordan -- """ + str(choice_1_votes + 1) + """ votes\nLebron James -- 1 vote\nKobe Bryant -- 1 vote\nSteph Curry -- 1 vote\nMagic Johnsen -- 0 votes"""
  #   driver.find_element(By.CSS_SELECTOR, 'body > a').click()
  #   assert driver.current_url == 'http://127.0.0.1:8000/polls/specifics/5/'
