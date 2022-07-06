
from src import PinterestScraper, PinterestSearchConfig, PinterestRelatedConfig


configs = PinterestSearchConfig(search_keywords="character face cyberpunk", # Search word
                          file_lengths=50,     # total number of images to download (default = "100")
                          image_quality="orig", # image quality (default = "orig")
                          bookmarks="")         # next page data (default= "")

configs = PinterestRelatedConfig(search_keywords="860257966336607477", # pin
                          file_lengths=50,     # total number of images to download (default = "100")
                          image_quality="orig", # image quality (default = "orig")
                          bookmarks="")         # next page data (default= "")                         


# PinterestScraper(configs).download_search_images()     # download images directly
# print(PinterestScraper(configs).get_search_urls())     # just bring image links


PinterestScraper(configs).download_related_images()  


