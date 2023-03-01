import requests
import csv

ENDPOINT = "https://api.github.com/search/repositories?q=is:public"

response = requests.get(ENDPOINT)
all_data = response.json()
# logic for filtering

fields = ['Name', 'Description', 'html_url', 'Watchers_count', 'Stargazers_count', 'Forks_count']

filtered_data = [data for data in all_data['items'] if
                 data['language'] == "JavaScript" and data['forks'] >= 50 and data['stargazers_count'] > 800]

data_list = [[data['name'], data['description'], data['html_url'], data['watchers_count'], data['stargazers_count'],
              data['forks_count']] for data in filtered_data]

with open('filtered_data.txt', 'w') as csv_file:
    # creating a csv writer object
    csv_writer = csv.DictWriter(csv_file, fieldnames=fields)

    # writing the fields
    csv_writer.writeheader()
    csv_file.write("\n")

    # writing the data rows
    for data in data_list:
        s = ', '.join([str(ele) for ele in data])
        csv_file.write(s + "\n")
