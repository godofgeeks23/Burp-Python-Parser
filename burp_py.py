import requests
from pprint import pprint
import os
import json

def parse_request(file_name):
    line = ""
    headers = {}
    post_data = ""
    header_collection_done = False
    file_object = open(file_name, "r")
    file_object.seek(0)
    file_object.readline()
    for line in file_object.readlines():
        if header_collection_done is False:
            if line.startswith("\n"):
                header_collection_done = True
            else:
                headers.update({
                    line[0:line.find(":")].strip(): line[line.find(":")+1:].strip()
                })
        else:
            post_data = post_data + line
    file_object.close()
    return (headers, post_data)


directory = "input_files"
for filename in os.scandir(directory):
    if filename.is_file():
        print("Reading File - ", filename.path)
        header, post_data = parse_request(filename.path)
        json_header = json.dumps(header, indent=4)
        json_header = json.loads(json_header)
        json_post_data = json.dumps(post_data, indent=4)
        json_post_data = json.loads(json_post_data)
        pprint(json_header)
        pprint(json_post_data)
        print()
        with open("output_files/"+filename.name+"_headers.json", "w") as outfile:
            json.dump(json_header, outfile)
        with open("output_files/"+filename.name+"_data.json", "w") as outfile:
        	json.dump(json_post_data, outfile)
