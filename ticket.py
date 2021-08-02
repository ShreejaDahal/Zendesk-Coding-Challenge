"""This module connects to the Zendesk API, and makes requests for the tickets.
 Displays ticket as per the user's instructions"""
# Author: Shreeja Dahal
import os
from pathlib import Path
import sys
import requests
from dotenv import load_dotenv


def display_all_tickets(url, user, pwd):
    """Makes a connection to the Zendesk API,and displays all the tickets in a list
        : atmost 25 per page if more than 25 tickets present.
         Catches an exception if the API is unavailable"""
    # Requirement 1 and 2:
    # Connect to the Zendesk API and Request all the tickets for your account
    try:
        while url:
            # print(url)
            # print("--------------------PAGE:", page_num, "-------------)
            tickets_details = requests.get(url, auth=(user, pwd))
            if tickets_details.status_code != 200:
                if tickets_details.status_code == 401:
                    print('ERROR CODE 401 :Authentication error')
                elif tickets_details.status_code == 400 or \
                        tickets_details.status_code == 404 or \
                        tickets_details.status_code == 429:
                    print('[ERROR]', tickets_details.status_code,
                          "The page you requested is not available")
                else:
                    print('[ERROR]', tickets_details.status_code,
                          "Error in Request")
                return tickets_details.status_code
            data = tickets_details.json()
            count = 0
            # Requirement 3 and 5: Display them in a list and page
            # through tickets if more than 25 tickets are present
            for ticket in data['tickets']:
                count += 1
                print(" Ticket ID:", ticket['id'],
                      " Status:", ticket["status"],
                      " Subject:", ticket["subject"])
            if data['meta']['has_more']:
                print("Total ticket count in this page: ", count)
                print("-------------------END OF PAGE------------------")
                print('\n')
                next_page = input("Go to next page? Enter Yes or No ")
                print('\n')
                if next_page == 'Yes':
                    url = url = data['links']['next']
                    print("-----------------NEW PAGE------------------------")
                elif next_page == 'No':
                    url = None
                    return tickets_details.status_code
                else:
                    print("Invalid input, try again!")
            else:
                url = None
        return tickets_details.status_code
    except requests.exceptions.ConnectionError:
        print("[ERROR]: Connection failed!")
        sys.exit()


# Requirement 4: Display individual ticket details
def get_a_ticket(url, user, pwd):
    """Makes a connection to the Zendesk API and displays a particular
     ticket details based on the ticket id entered by the user.
     Catches an exception if the API is unavailable"""
    try:
        ticket_id_response = requests.get(url, auth=(user, pwd))
        if ticket_id_response.status_code != 200:
            print("The ticket id you entered doesn't exist! ")
            return ticket_id_response.status_code

        data = ticket_id_response.json()
        ticket = data["ticket"]
        print("\n")
        print("Ticket ID:", ticket['id'],
              "Subject:", ticket['subject'], "  Status:", ticket['status'])
        print("\n")
        print("Description: ")
        print(ticket['description'])
        print("\n")
        print("Created at:", ticket['created_at'],
              "Updated at:", ticket['updated_at'])
        print("\n")
        return ticket_id_response.status_code
    except requests.exceptions.ConnectionError:
        print("[ERROR]: Connection failed!")
        sys.exit()


def main():
    """Start page of the ticket viewing system that allows the user
    to either view all the tickets, an individual ticket, or exit"""
    load_dotenv()
    env_path = Path('.')/'.env'
    load_dotenv(dotenv_path=env_path)

    user = os.environ.get('user')
    pwd = os.environ.get('pwd')
    url = 'https://zccdahal.zendesk.com/api/v2/tickets.json?page[size]=25'
    message = ''
    while message != '0':
        message = input("Press 1 to view all ticket\n"
                        "Press 2 to view a ticket\n"
                        "Press 0 to exit: ")
        if message == '0':
            print("Goodbye!")
            sys.exit()
        elif message == '1':
            display_all_tickets(url, user, pwd)
        elif message == '2':
            ticket_id = input('Enter the id of the ticket you want to see:')
            if not ticket_id.isdigit():
                print("Invalid input! ")
                sys.exit()
            url = (
                f"https://zccdahal.zendesk.com/"
                f"api/v2/tickets/{str(ticket_id)}.json"
            )
            get_a_ticket(url, user, pwd)
        elif not message.isdigit():
            print("Invalid input!")
        else:
            print(f"The option {message} you just entered doesn't exist!")


if __name__ == "__main__":
    main()
