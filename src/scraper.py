import requests
import json
import os
import urllib
import sys
import traceback
import sys

class Scraper:

    def __init__(self, config, image_urls=[]):
        self.config = config
        self.image_urls = image_urls

    # Set config for bookmarks (next page)
    def setConfig(self, config):
        self.config = config

    # Download images
    def download_search_images(self):
        folder = "photos/search/" + self.config.search_keyword.replace(" ", "-")
        number = 0
        # prev get links
        results = self.get_search_urls()

        try:
            os.makedirs(folder)
            print("Directory ", folder, " Created ")
        except FileExistsError:
            a = 1
        arr = os.listdir(folder+"/")

        for i in results:
            if str(i + ".jpg") not in arr:
                try:
                    file_name = str(i.split("/")[len(i.split("/"))-1])
                    download_folder = str(folder) + "/" + file_name
                    print("Download ::: ", i)
                    urllib.request.urlretrieve(i,  download_folder)
                    number = number + 1
                except Exception as e:
                    print(e)


    # get_search_urls return array
    def get_search_urls(self):
        SOURCE_URL = self.config.source_url,
        DATA = self.config.image_data,
        URL_CONSTANT = self.config.search_url
        r = requests.get(URL_CONSTANT, params={
                         "source_url": SOURCE_URL, "data": DATA})
                
        print(DATA)
        print(SOURCE_URL)
        print(r.request.url)

        # return 
        

        with open(self.config.search_keyword.replace(" ", "-") + ".txt", "w") as text_file:
            jsonData = json.loads(r.content)
            jsonStr = json.dumps(jsonData, indent=4)
            text_file.write(jsonStr)



        jsonData = json.loads(r.content)
        resource_response = jsonData["resource_response"]
        data = resource_response["data"]
        results = data["results"]
        for i, d in enumerate(results):
            # print(type(i))
            # print(i.keys())
            # print(i['objects'][1].keys())
            # print(i['objects'][1]['images'])
            # break
            try :
                if 'objects' in d:
                    data = d['objects'][1]['images']
                    print('objects--{}'.format(i))
                if 'images' in d:
                    data = d['images']
                    print(i)
                    url = data[self.config.image_quality]["url"]
                    self.image_urls.append(url)
            except Exception as e:
                print(traceback.format_exc())
                print(i)
                print(d)
                break

        # return self.image_urls

            # url = i['objects']
            # url = url[1]["images"][self.config.image_quality]["url"]
            # self.image_urls.append(url)

        if len(self.image_urls) < int(self.config.file_length):
            self.config.bookmarks = resource_response["bookmark"]
            print(self.image_urls)
            print("Creating links", len(self.image_urls))
            self.get_search_urls()
            return self.image_urls[0:self.config.file_length]

        # if len(str(resource_response["bookmark"])) > 1 : connect(query_string, bookmarks=resource_response["bookmark"])



    # Download images
    def download_related_images(self):
        folder = "photos/related/" + self.config.search_keyword.replace(" ", "-")
        number = 0
        # prev get links
        results = self.get_related_urls()

        try:
            os.makedirs(folder)
            print("Directory ", folder, " Created ")
        except FileExistsError:
            a = 1
        arr = os.listdir(folder + "/")

        for i in results:
            if str(i + ".jpg") not in arr:
                try:
                    file_name = str(i.split("/")[len(i.split("/"))-1])
                    download_folder = str(folder) + "/" + file_name
                    print("Download ::: ", i)
                    urllib.request.urlretrieve(i,  download_folder)
                    number = number + 1
                except Exception as e:
                    print(e)


    # get_search_urls return array
    def get_related_urls(self):
        SOURCE_URL = self.config.source_url,
        DATA = self.config.image_data,
        URL_CONSTANT = self.config.search_url
        r = requests.get(URL_CONSTANT, params={
                         "source_url": SOURCE_URL, "data": DATA})
                
        print(DATA)
        print(SOURCE_URL)
        print(r.request.url)

        # return 
        

        with open(self.config.search_keyword.replace(" ", "-") + ".txt", "w") as text_file:
            jsonData = json.loads(r.content)
            jsonStr = json.dumps(jsonData, indent=4)
            text_file.write(jsonStr)



        jsonData = json.loads(r.content)
        resource_response = jsonData["resource_response"]
        results = resource_response["data"]
        for i, d in enumerate(results):
            # print(type(i))
            # print(i.keys())
            # print(i['objects'][1].keys())
            # print(i['objects'][1]['images'])
            # break
            try :
                if 'images' in d:
                    data = d['images']
                    print(i)
                    url = data[self.config.image_quality]["url"]
                    self.image_urls.append(url)
            except Exception as e:
                print(traceback.format_exc())
                print(i)
                print(d)
                break

        # return self.image_urls

            # url = i['objects']
            # url = url[1]["images"][self.config.image_quality]["url"]
            # self.image_urls.append(url)

        if len(self.image_urls) < int(self.config.file_length):
            self.config.bookmarks = resource_response["bookmark"]
            print(self.image_urls)
            print("Creating links", len(self.image_urls))
            self.get_related_urls()
            return self.image_urls[0:self.config.file_length]

        # if len(str(resource_response["bookmark"])) > 1 : connect(query_string, bookmarks=resource_response["bookmark"])



