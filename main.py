
from src import PinterestScraper, PinterestSearchConfig, PinterestRelatedConfig


# configs = PinterestSearchConfig(
#     search_keywords="Goth FACE", # Search word
#     file_lengths=50,     # total number of images to download (default = "100")
#     image_quality="orig", # image quality (default = "orig")
#     bookmarks="")         # next page data (default= "")
# urls = PinterestScraper(configs).get_search_urls()   # just bring image links



# 398427898289857670


configs = PinterestRelatedConfig(
    search_keywords="1041527851297924777", # pin
    file_lengths=50,     # total number of images to download (default = "100")
    image_quality="orig", # image quality (default = "orig")
    bookmarks="")         # next page data (default= "")                         
urls = PinterestScraper(configs).get_related_urls()


# PinterestScraper(configs).download_search_images()     # download images directly
# 

# PinterestScraper(configs).download_related_images()  

print('\n\n')
print(urls)


