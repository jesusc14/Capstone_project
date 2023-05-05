<<<<<<< HEAD
# import requests
# import google.protobuf
# from google.transit import gtfs_realtime_pb2

# feed_url = 'https://s3.amazonaws.com/kcm-alerts-realtime-prod/tripupdates_enhanced.json'

# response = requests.get(feed_url)

# print(response.content)

# feed = gtfs_realtime_pb2.FeedMessage()
# feed.ParseFromString(response.content)

# for entity in feed.entity:
#     if entity.HasField('trip_update'):
#         print(entity.trip_update)

# import requests

# response = requests.get('https://s3.amazonaws.com/kcm-alerts-realtime-prod/tripupdates_enhanced.json')
# json_data = response.json()

# # now you can work with the JSON data



# import json

# # Read in the JSON data from a file
# # with open('https://s3.amazonaws.com/kcm-alerts-realtime-prod/tripupdates_enhanced.json', 'r') as f:
# #     json_data = json.load(f)

# # Access the stops field and iterate over the stops
# for stop in json_data['stops']:
#     stop_id = stop['stop_id']
#     stop_name = stop['stop_name']
#     stop_lat = stop['stop_lat']
#     stop_lon = stop['stop_lon']
    
#     # Process the stop data as needed
#     print(f'Stop {stop_id}: {stop_name} ({stop_lat}, {stop_lon})')


# import json
# import urllib.request

# url = "https://s3.amazonaws.com/kcm-alerts-realtime-prod/tripupdates_enhanced.json"
# response = urllib.request.urlopen(url)
# data = json.loads(response.read().decode())

# print(json.dumps(data, indent=4))


# import json
# import urllib.request

# # read the JSON file from the URL
# url = "https://s3.amazonaws.com/kcm-alerts-realtime-prod/tripupdates_enhanced.json"
# response = urllib.request.urlopen(url)
# json_data = json.loads(response.read().decode())

# # extract information for each stop
# for stop in json_data['entity'][0]['trip_update']['stop_time_update']:
#     stop_sequence = stop['stop_sequence']
#     stop_id = stop['stop_id']
#     arrival_delay = stop['arrival']['delay']
#     arrival_time = stop['arrival']['time']
#     departure_delay = stop['departure']['delay']
#     departure_time = stop['departure']['time']
#     schedule_relationship = stop['schedule_relationship']

#     # print the extracted information
#     print("Stop Sequence:", stop_sequence)
#     print("Stop ID:", stop_id)
#     print("Arrival Delay:", arrival_delay)
#     print("Arrival Time:", arrival_time)
#     print("Departure Delay:", departure_delay)
#     print("Departure Time:", departure_time)
#     print("Schedule Relationship:", schedule_relationship)
#     print()

import requests
import json

response = requests.get("https://s3.amazonaws.com/kcm-alerts-realtime-prod/tripupdates_enhanced.json")

# print(response.status_code)


# print(response.json())

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())


from google.transit import gtfs_realtime_pb2
import requests

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get('https://s3.amazonaws.com/kcm-alerts-realtime-prod/tripupdates.pb')
feed.ParseFromString(response.content)
for entity in feed.entity:
  if entity.HasField('trip_update'):
    print(entity.trip_update)
=======
>>>>>>> parent of 11070be (added python files)
