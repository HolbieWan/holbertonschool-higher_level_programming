#!/usr/bin/python3
"""Requests Module"""
import requests
import csv

url = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder and prints their titles."""
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            # print("Post ID: {}".format(post['id']))
            print("{}".format(post['title']))
            # print("Body: {}\n".format(post['body']))
    else:
        print(
            "Failed to fetch posts. Status code: {}".format(
                response.status_code))


def fetch_and_save_posts():
    """Fetches posts from JSONPlaceholder and saves them to a CSV file."""
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        posts_dict_list = []
        for post in posts:
            posts_dict_list.append(
                {'Post ID': post['id'], 'Title': post['title'], 'Body': post['body']})
        csv_file = 'posts.csv'
        with open(csv_file, mode='w', newline='') as file:
            new_instance = csv.DictWriter(
                file, fieldnames=['Post ID', 'Title', 'Body'])
            new_instance.writeheader()
            new_instance.writerows(posts_dict_list)


"""
def print_csv_content(csv_file):
    #Read and print the content of the CSV file
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
"""
