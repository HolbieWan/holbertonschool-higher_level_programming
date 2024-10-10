#!/usr/bin/python3
"""Requests Module"""
import requests
import json
import csv

url = 'https://jsonplaceholder.typicode.com/posts'
filename = "./json_file.json"

def fetch_and_save_posts(filename):
    """Fetches posts from JSONPlaceholder and saves them to a json file."""
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        posts_dict_list = []
        for post in posts:
            posts_dict_list.append(
                {'id': post['id'], 'title': post['title'], 'body': post['body']})
        with open(filename, "w") as get_request_json:
            json.dump(posts_dict_list, get_request_json)

def print_from_json(filename):
    """Reads data from filename and prints the Titles"""
    with open(filename, "r") as file:
        json_file = json.load(file)
        for jsons in json_file:
            print("Title: {}".format(jsons['title']))


fetch_and_save_posts(filename)
print_from_json(filename)