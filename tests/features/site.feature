Feature: Django Site Testing
    Scenario: Test contents of the nba page
        Given you launch a browser and you have your site running and the page title is Player Database
        And the navbar, form, and images are visible on the page
        Then you should verify the 2 gifs and images on the page are what you expect
    
    Scenario: Test submitting to nba database page
        Given you remain on the nba database page
        When you input a basketball player details and click submit
        Then that player should be in the page source, i.e. in the database
        And take a screenshot of the database page

    Scenario: Move to the polls page
        Given you click on the button - Go to Polls Page. 
        When you verify you are on the polls page with page title - NBA polls
        Then verify there is a header which says NBA Polls:
        And verify there is a hyperlink with the name of the poll question - Who's the GOAT in basketball?
        And verify there is a hyperlink named - Go to Player Database
        And take a screenshot of the polls page 

    Scenario: Move to the GOAT poll page
        Given you click on the hyperlink of the poll question.
        Then verify the poll header is a repeat of the hyperlink
        And verify there are 5 options to vote for
        And there is a vote button
        And there is a hyperlink to go back to the main polls page
        And take a screenshot of GOAT poll page
    
    Scenario: Attempt to vote without choosing an option
        When you click vote without choosing any option
        Then you should receive a popup on the site saying - You didn't select a choice.
    
    Scenario: Choose Michael Jordan as the GOAT and submit vote
        Given you choose Michael as your GOAT and Vote
        Then you should be in the results page of the poll, verifiable by url, and the header of the results which is the poll question
        And bullet pointed are the names of the choices, and the number of votes they have, sandwiched by two dashes 
        And Michael Jordan should have votes > 0, whilst the rest should have zero
    
    Scenario: Vote Michael Jordan again
        Given you just voted and are on the results page
        When you click on the hyperlink titled - Vote again?
        Then choose Michael Jordan and vote again
        And you will see his votes have increased by 1 
    
    Scenario: Maneuvering through the site
        Given you are on the results page
        Then you should be able to go back to the polls page with a button
        And go back to the NBA database by clicking on the - Go to Player Database - button
        And have a button on the navbar in the NBA database page called Player Database that refreshes the page
    


