# reads JSON file output form of human data
import json
# can crawl through the human_data directory
import os
# imports pretty-printable for outputs
import pprint

# sets up the pretty printer for a coding format
pp: pprint.PrettyPrinter = pprint.PrettyPrinter(4, 80)

# relative path to data
rel_path: str = "human_data/"
# list containing all the data
data: list[list[dict]] = []


# goes through all files in the data directory
filename: str
for filename in os.listdir(rel_path):
    
    # opens the file
    with open(f"{rel_path}{filename}", encoding="utf-8") as file:
        
        # reads in the json and appends it to the list storing all the data
        data.append(json.load(file))

# goes through list backwards
for i in range(len(data) - 1, -1, -1):

    # if you didn't complete the task
    if data[i][0]["success"] == False or data[i][0]["timeout"] == True:

        # remove this datapoint
        print(data.pop(i))
    
    # otherwise, prune non-data
    else:
        # deletes experiment header info
        del data[i][0]
        # deletes experiment page start
        del data[i][0]
        # deletes experiment page end
        del data[i][-1]

# list of choices and their index as presented to the user
choices: list[str] = [
    "Boat", 
    "Broccoli", 
    "Car", 
    "Cat", 
    "Dog",
    "Human",
    "Tree",
    "Other"
]

# number of difficulties
difficulties: int = 9

# correlates image shown to response by difficulty
homologated_data: list[dict[dict]] = []

# initializes the results list
i: int
for i in range(difficulties):

    # creates a dictionary for each difficulty
    homologated_data.append({})

    # populates each dictionary with key, corresponding to image-shown type
    # and values, corresponding to a dictionary mapping the response given to
    # the number of times that response was given
    shown: str
    for shown in choices:
        homologated_data[i][shown] = {}

        # initializes the amount of times each response was given
        for response in choices:
            homologated_data[i][shown][response] = 0



# tracks number of pictures
pics: int = 0

# goes through all people in the dataset
person: list[dict]
for person in data:

    # goes through all images the person went through
    pic: dict
    for pic in person:

        # increments the number of pictures gone through
        pics += 1
        # notes the image shown to the response
        homologated_data[int(pic["background_difficulty"])][pic["category"]][choices[pic["response"]]] += 1

pp.pprint(homologated_data)