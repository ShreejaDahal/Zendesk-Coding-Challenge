# Zendesk-Coding-Challenge

This project was given as a 'Coding challenge' by Zendesk as a part of their Engineering Co-op 2021-2022 Hiring Process.
## Challenge Requirements:
1. Connect to the Zendesk API
2. Request all the tickets for your account
3. Display them in a list
4. Display individual ticket details
5. Page through tickets when more than 25 are returned

## Non-functional Requirements:
1. The UI can be browser-based or CLI.
2. The Ticket Viewer should handle the API being unavailable
3. Some unit tests for the application in a standard unit testing
framework for the language of choice


## Overview on the project
The UI chosen is command line interface written in Python and tested using pytest framework. The application connects to the Zendesk API using HTTP request and retrieves either a single ticket info or all the tickets from an account. When asked to display all the tickets, the application pages through tickets if more than 25 are returned.


# Steps Involved:
#### 1. Connect to the Zendesk API:
 Used ```Python-dotenv``` to read the username and password as 'user' and 'pwd' from a .env file, set as environment variables. 
#### 2. Display all the tickets; page through tickets when more than 25 are returned:
 Returned only 25 tickets per page by setting the page size to 25, using cursor pagination as recommended by Zendesk. Asked the user if they wanted to view the next page, if ```yes```, retrived next 25 tickets. 
#### 3. Display individual tickets:
 Displayed the detials of an individual ticket based on the ```ticket id.``` 
   
# Unit tests: Used pytest framework for unit testing.
1. Tests to see if an API is available.
2. Tests with incorrect usernames.
3. Tests with incorrect passwords and correct username.
4. Tests with correct password and correct username but incorrect ticket id.
5. Tests with correct ticket id but incorrect username.
6. Tests with correct username and id but incorrect password.
7. Tests to see if a URL with a certian page number exists or not.


## Instructions to run the program on your local machine:
1. Git cloning: On your terminal type
```
 https://github.com/ShreejaDahal/Zendesk-Coding-Challenge.git
 ```
2. Install dependencies: 
 ```pip3 install -r requirements.txt```
 Note: This is based on the fact that the program was built using Python3. 

3. Create a .env file in the same directory as your program. Add the environment variables `user` and `pwd` with their appropriate values.
   To learn more, visit https://pypi.org/project/python-dotenv/
 
 #### To run the program
 Navigate to the directory where the files are saved and then run the following command
 ```
 python3 ticket.py
 ```
#### To run the tests
Navigate to the directory and run the following command
```
pytest ticket_test.py
```

## Helpful Resources
  #### 1. Ticket Requests:
  https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-requests/
  #### 2. Pagination:
   https://developer.zendesk.com/documentation/developer-tools/pagination/paginating-through-lists-using-cursor-pagination/
  #### 3. Creating Zendesk API token:
   https://developer.zendesk.com/documentation/ticketing/working-with-oauth/creating-and-using-oauth-tokens-with-the-api/
  #### 4.  Authentication:
   https://developer.zendesk.com/api-reference/ticketing/introduction/#basic-authentication
   
