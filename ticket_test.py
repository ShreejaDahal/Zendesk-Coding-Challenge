"""This module containts tests cases for ticket.py"""
import os
import random
import requests
from ticket import display_all_tickets, get_a_ticket


def test_setup():
    """This function sets up the username as user and password as pwd"""
    user = os.environ.get('user')
    pwd = os.environ.get('pwd')
    return user, pwd


def test_sample_data():
    """This function sets up sample data for unit testing"""
    users = ['cutie@google.com', 'coolgirl@standfor.edu']
    passwords = ['apple', 'lifeisgood', 'suvi12349098dtokenisgood', '-1', '-6']
    id_list = [121, 356, 201, 202, -6, -8]
    page_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    id_num = random.randint(-200, 200)
    tick_url = 'https://zccdahal.zendesk.com/api/v2/tickets.json?page[size]=25'
    id_url = f"https://zccdahal.zendesk.com/api/v2/tickets/{str(id_num)}.json"
    return {'users': users,
            'passwords': passwords, 'id_numbers': id_list,
            'pages': page_numbers, 'url': tick_url,
            'id_url': id_url}


def test_api():
    """Tests the availablity of Zendesk API"""
    user, pwd = test_setup()
    data = test_sample_data()
    result = requests.get(data["url"], auth=(user, pwd))
    assert display_all_tickets(data["url"], user, pwd) == result.status_code


def test_username_all():
    """Tests display_all_tickets function with incorrect usernames"""
    user, pwd = test_setup()
    data = test_sample_data()
    for user in data["users"]:
        result = requests.get(data["url"], auth=(user, pwd))
        assert display_all_tickets(data["url"], user, pwd) ==\
            result.status_code


def test_password_all():
    """Tests display_all_tickets function with incorrect passwords"""
    user, pwd = test_setup()
    data = test_sample_data()
    for pwd in data["passwords"]:
        result = requests.get(data["url"], auth=(user, pwd))
        assert display_all_tickets(data["url"], user, pwd) ==\
            result.status_code


def test_id():
    """Tests get_a_ticket function with incorrect ids"""
    user, pwd = test_setup()
    data = test_sample_data()
    id_list = data["id_numbers"]
    for id_num in id_list:
        url = f"https://zccdahal.zendesk.com/api/v2/tickets/{str(id_num)}.json"
        result = requests.get(url, auth=(user, pwd))
        assert get_a_ticket(url, user, pwd) == result.status_code


def test_username_id():
    """Tests get_a_ticket function with incorrect usernames"""
    user, pwd = test_setup()
    data = test_sample_data()
    for user in data["users"]:
        result = requests.get(data["id_url"], auth=(user, pwd))
        assert display_all_tickets(data["id_url"], user, pwd) == \
            result.status_code


def test_password_id():
    """Tests get_a_ticket function with correct id but incorrect password"""
    user, pwd = test_setup()
    data = test_sample_data()
    for pwd in data["passwords"]:
        result = requests.get(data["id_url"], auth=(user, pwd))
        assert get_a_ticket(data["id_url"], user, pwd) == result.status_code


def test_by_page():
    """Tests if a URL with a certain page number exists or not"""
    user, pwd = test_setup()
    data = test_sample_data()
    pages = data["pages"]
    for i in pages:
        url = f"https://zccdahal.zendesk.com/api/v2/tickets.json?\
            page={str(pages[i])}"
        result = requests.get(url, auth=(user, pwd))
        assert display_all_tickets(url, user, pwd) == result.status_code
