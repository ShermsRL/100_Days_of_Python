import requests
from datetime import datetime

USERNAME = "shermantayruilong"
TOKEN = "Shertayman1998"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

headers = {
    "X-USER-TOKEN": TOKEN,

}

# Creating the user---------------------------------------------------
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Creating the graph-----------------------------------------------------
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config ={
#     "id": GRAPH_ID,
#     "name": "Coding Graph",
#     "unit": "minutes",
#     "type": "int",
#     "color": "momiji",
#
# }
#
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Adding pixel to the graph----------------------------------------------------------------------------------------
add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

add_pixel_details = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How long did you code today?"),

}

# response = requests.post(url=add_pixel_endpoint, json=add_pixel_details, headers=headers)
# print(response.text)

# Updating the pixel-----------------------------------------------------------------------------------------------
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_details = {
    "quantity": "120"

}

# response = requests.put(url=update_endpoint, json=update_details, headers=headers)
# print(response.text)

# Deleting a pixel----------------------------------------------------------------------------------------------
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
