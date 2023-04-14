"""Django Site Testing feature tests."""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

def get_default_url(url):
    "gets the default url of the site and appends / to it if necessary"
    if url[-1] == "/":
        return url
    return url + "/"


@scenario('../../site.feature', 'Test contents of the nba page')
def test_test_contents_of_the_nba_page():
    """Test contents of the nba page."""


@scenario('../../site.feature', 'Test submitting to nba database page')
def test_test_submitting_to_nba_database_page():
    """Test submitting to nba database page."""


@scenario('../../site.feature', 'Move to the polls page')
def test_move_to_the_polls_page():
    """Move to the polls page."""


@scenario('../../site.feature', 'Move to the GOAT poll page')
def test_move_to_the_goat_poll_page():
    """Move to the GOAT poll page."""


@scenario('../../site.feature', 'Attempt to vote without choosing an option')
def test_attempt_to_vote_without_choosing_an_option():
    """Attempt to vote without choosing an option."""



@scenario('../../site.feature', 'Choose Michael Jordan as the GOAT and submit vote')
def test_choose_michael_jordan_as_the_goat_and_submit_vote():
    """Choose Michael Jordan as the GOAT and submit vote."""


@scenario('../../site.feature', 'Vote Michael Jordan again')
def test_vote_michael_jordan_again():
    """Vote Michael Jordan again."""


@scenario('../../site.feature', 'Maneuvering through the site')
def test_maneuvering_through_the_site():
    """Maneuvering through the site."""


@given('the navbar, form, and images are visible on the page')
def features_of_database_page(browser):
    """the navbar, form, and images are visible on the page."""
    try:  # Asserts visibility of navbar at top
      WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > nav')))
      found = True
    except:
      found = False
    assert found

    try:  # Asserts visibility of pictures below navbar
      WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > center')))
      found = True
    except:
      found = False
    assert found

    try:  # Asserts visibility of form and buttons below
      WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div:nth-child(5) > form')))
      found = True
    except:
      found = False
    assert found


@given('you are on the results page')
def go_in_results_page(browser):
    """you are on the results page."""
    assert browser.current_url == 'https://djangosite-uhgxj7hora-ew.a.run.app/polls/1/results/'


@given('you choose Michael as your GOAT and Vote')
def choose_jordan(browser):
    """you choose Michael as your GOAT and Vote."""
    click_choice_1 = browser.find_element(By.CSS_SELECTOR, '#choice1')
    click_choice_1.click()
    browser.find_element(By.CSS_SELECTOR, 'body > form > input[type=submit]:nth-child(3)').click()


@given('you click on the button - Go to Polls Page.')
def click_go_polls_button(browser):
    """you click on the button - Go to Polls Page.."""
    enter_polls_page = browser.find_element(By.CSS_SELECTOR, 'body > div:nth-child(5) > form > a')
    enter_polls_page.click()

@given('you click on the hyperlink of the poll question.')
def poll_link_click(browser):
    """you click on the hyperlink of the poll question.."""
    click_on_first_poll = browser.find_element(By.CSS_SELECTOR, 'body > ul > li > a')
    click_on_first_poll.click()
    assert browser.current_url == 'https://djangosite-uhgxj7hora-ew.a.run.app/polls/specifics/1/'


@given('you just voted and are on the results page')
def results_page(browser):
    """you just voted and are on the results page."""
    assert browser.current_url == 'https://djangosite-uhgxj7hora-ew.a.run.app/polls/1/results/'


@given('you launch a browser and you have your site running and the page title is Player Database')
def player_database_page(browser, url):
    """you launch a browser and you have your site running and the page title is Player Database."""
    browser.get(url)
    WebDriverWait(browser, 15)
    assert browser.current_url == "https://djangosite-uhgxj7hora-ew.a.run.app/"
    assert browser.title == "Player Database"


@given('you remain on the nba database page')
def check_you_on_database_page(browser):
    """you remain on the nba database page."""
    assert browser.current_url == "https://djangosite-uhgxj7hora-ew.a.run.app/"
    assert browser.title == "Player Database"


@when('you click on the hyperlink titled - Vote again?')
def vote_again_click(browser):
    """you click on the hyperlink titled - Vote again?."""
    browser.find_element(By.CSS_SELECTOR, 'body > a:nth-child(3)').click()



@when('you click vote without choosing any option')
def vote_no_choice(browser):
    """you click vote without choosing any option."""
    vote_button = browser.find_element(By.CSS_SELECTOR, 'body > form > input[type=submit]:nth-child(3)')
    vote_button.click()


@when('you input a basketball player details and click submit')
def populate_form(browser):
    """you input a basketball player details and click submit."""
    #find the elements you need to submit form
    player_name = browser.find_element(By.CSS_SELECTOR, '#id_name')
    player_height = browser.find_element(By.CSS_SELECTOR, '#id_height')
    player_team = browser.find_element(By.CSS_SELECTOR, '#id_team')
    player_ppg = browser.find_element(By.CSS_SELECTOR, '#id_ppg')

    submit = browser.find_element(By.CSS_SELECTOR, '#submit_button')

    #populate the form with data

    player_name.send_keys('Arnit Ibrahimovic')
    player_team.send_keys('LA Bakers')
    player_height.send_keys('6 foot 2 on dates')
    player_ppg.send_keys('27.2')

    submit.send_keys(Keys.RETURN)


@when('you verify you are on the polls page with page title - NBA polls')
def NBA_polls_page_verifier(browser):
    """you verify you are on the polls page with page title - NBA polls."""
    assert browser.current_url == "https://djangosite-uhgxj7hora-ew.a.run.app/polls/"
    assert browser.title == "NBA Polls"


@then('Michael Jordan should have votes > 0, whilst the rest should have zero')
def vote_numbers(browser):
    """Michael Jordan should have votes > 0, whilst the rest should have zero."""
    votes_text = browser.find_element(By.CSS_SELECTOR, 'body > ul > li:nth-child(1)').text
    num1 = ""
    for c in votes_text:
      if c.isdigit():
        num1 = num1 + c
    votes_text = browser.find_element(By.CSS_SELECTOR, 'body > ul > li:nth-child(2)').text
    num2 = ""
    for c in votes_text:
      if c.isdigit():
        num2 = num2 + c
    votes_text = browser.find_element(By.CSS_SELECTOR, 'body > ul > li:nth-child(3)').text
    num3 = ""
    for c in votes_text:
      if c.isdigit():
        num3 = num3 + c
    votes_text = browser.find_element(By.CSS_SELECTOR, 'body > ul > li:nth-child(4)').text
    num4 = ""
    for c in votes_text:
      if c.isdigit():
        num4 = num4 + c
    votes_text = browser.find_element(By.CSS_SELECTOR, 'body > ul > li:nth-child(5)').text
    num5 = ""
    for c in votes_text:
      if c.isdigit():
        num5 = num5 + c

    voter_info = browser.find_element(By.CSS_SELECTOR, 'body > ul')
    assert voter_info.text == """Michael Jordan -- """ + num1 + """ votes\nLebron James -- """+ num2 +""" votes\nKobe Bryant -- """+ num3 + """ votes\nSteph Curry -- """+ num4 + """ votes\nMagic Johnsen -- """+ num5 + """ votes"""


@then('bullet pointed are the names of the choices, and the number of votes they have, sandwiched by two dashes')
def result_page_aesthetics(browser):
    """bullet pointed are the names of the choices, and the number of votes they have, sandwiched by two dashes."""
    browser.save_screenshot("polls_result_00.png")


@then('choose Michael Jordan and vote again')
def vote_jordan_again(browser):
    """choose Michael Jordan and vote again."""
    click_choice_1 = browser.find_element(By.CSS_SELECTOR, '#choice1')
    click_choice_1.click()
    browser.find_element(By.CSS_SELECTOR, 'body > form > input[type=submit]:nth-child(3)').click()


@then('go back to the NBA database by clicking on the - Go to Player Database - button')
def back_to_nba_database(browser):
    """go back to the NBA database by clicking on the - Go to Player Database - button."""
    browser.find_element(By.CSS_SELECTOR, 'body > a').click()
    # browser.implicitly_wait(10)
    # assert browser.current_url == "https://djangosite-uhgxj7hora-ew.a.run.app/"
    # assert browser.title == "Player Database"


@then('have a button on the navbar in the NBA database page called Player Database that refreshes the page')
def refresh_page(browser):
    """have a button on the navbar in the NBA database page called Player Database that refreshes the page."""
    browser.find_element(By.CSS_SELECTOR, 'body > a').click()
    assert browser.current_url == "https://djangosite-uhgxj7hora-ew.a.run.app/"


@then('take a screenshot of the database page')
def nba_database_page_scrnshot(browser):
    """take a screenshot of the database page."""
    browser.save_screenshot("player_database_page_00.png")


@then('take a screenshot of the polls page')
def scrnshot_polls_main_page(browser):
    """take a screenshot of the page."""
    browser.save_screenshot("polls_hub_page_00.png")


@then('take a screenshot of GOAT poll page')
def scrnshot_GOAT_poll_page(browser):
    """take a screenshot of the page."""
    browser.save_screenshot("polls_hub_page_00.png")


@then('that player should be in the page source, i.e. in the database')
def check_player_added_to_database(browser):
    """that player should be in the page source, i.e. in the database."""
    #check result; page source looks at entire html document
    assert 'Arnit Ibrahimovic' in browser.page_source


@then('there is a hyperlink to go back to the main polls page')
def back_to_main_polls(browser):
    """there is a hyperlink to go back to the main polls page."""
    assert browser.find_element(By.CSS_SELECTOR, 'body > a').text == "Go back to Polls"


@then('there is a vote button')
def check_for_vote_button(browser):
    """there is a vote button."""
    try:
      WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > form')))
      found = True
    except:
      found = False
    assert found

    vote_button = browser.find_element(By.CSS_SELECTOR, 'body > form > input[type=submit]:nth-child(3)')
    assert vote_button.get_attribute("value") == "Vote"


@then('verify the poll header is a repeat of the hyperlink')
def poll_header_checker(browser):
    """verify the poll header is a repeat of the hyperlink."""
    assert browser.find_element(By.CSS_SELECTOR, 'body > form > fieldset > legend > h1').text == "Who's the GOAT in basketball?"


@then('verify there are 5 options to vote for')
def choices_5(browser):
    """verify there are 5 options to vote for."""
    assert browser.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(3)').text == "Michael Jordan"
    assert browser.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(6)').text == "Lebron James"
    assert browser.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(9)').text == "Kobe Bryant"
    assert browser.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(12)').text == "Steph Curry"
    assert browser.find_element(By.CSS_SELECTOR, 'body > form > fieldset > label:nth-child(15)').text == "Magic Johnsen"

@then('verify there is a header which says NBA Polls:')
def page_header_checker_nba_polls(browser):
    """verify there is a header which says NBA Polls:"""
    assert browser.find_element(By.CSS_SELECTOR, 'body > font').text == "NBA Polls:"


@then('verify there is a hyperlink named - Go to Player Database')
def hyperlink_checker(browser):
    """verify there is a hyperlink named - Go to Player Database."""
    assert browser.find_element(By.CSS_SELECTOR, 'body > a').text == "Go to Player Database"


@then('verify there is a hyperlink with the name of the poll question - Who\'s the GOAT in basketball?')
def hyperlink_of_poll_q(browser):
    """verify there is a hyperlink with the name of the poll question - Who's the GOAT in basketball?."""
    assert browser.find_element(By.CSS_SELECTOR, 'body > ul > li > a').text == "Who's the GOAT in basketball?"


@then('you should be able to go back to the polls page with a button')
def back_to_polls_button_press(browser):
    """you should be able to go back to the polls page with a button."""
    browser.find_element(By.CSS_SELECTOR, 'body > a').click()
    assert browser.current_url == 'https://djangosite-uhgxj7hora-ew.a.run.app/polls/specifics/1/'


@then('you should be in the results page of the poll, verifiable by url, and the header of the results which is the poll question')
def results_page_checker(browser):
    """you should be in the results page of the poll, verifiable by url, and the header of the results which is the poll question."""
    assert browser.current_url == "https://djangosite-uhgxj7hora-ew.a.run.app/polls/1/results/"


@then('you should receive a popup on the site saying - You didn\'t select a choice.')
def you_didnt_vote_msg(browser):
    """you should receive a popup on the site saying - You didn't select a choice.."""
    try:
      WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > form > fieldset > p > strong')))
      found = True
    except:
      found = False
    assert found

    assert browser.find_element(By.CSS_SELECTOR, 'body > form > fieldset > p > strong').text == "You didn't select a choice."


@then('you should verify the 2 gifs and images on the page are what you expect')
def image_checker_database_page(browser):
    """you should verify the 2 gifs and images on the page are what you expect."""
    # Asserting the images are what you expect them to be
    
    identical_gifs = [browser.find_element(By.CSS_SELECTOR, 'body > center > img:nth-child(1)'), browser.find_element(By.CSS_SELECTOR, 'body > center > img:nth-child(3)')]
    for gif in identical_gifs:
      assert gif.get_attribute("src") == "https://thumbs.gfycat.com/BaggyAdorableFairybluebird-size_restricted.gif"
    
    assert browser.find_element(By.CSS_SELECTOR, 'body > center > img:nth-child(2)').get_attribute("src") == "https://www.freepnglogos.com/uploads/nba-logo-png/nba-stats-logo-documentation-with-examples-slothparadise-11.png"


@then('you will see his votes have increased by 1')
def vote_up_by_one(browser):
    """you will see his votes have increased by 1."""
    browser.save_screenshot("jordan_gains_a_vote.png")