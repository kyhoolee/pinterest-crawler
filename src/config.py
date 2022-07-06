import urllib

'''
https://www.pinterest.com/resource/ApiResource/get/?
source_url=/pin/22236591903222945/
&
data=
{
	"options": {
		"url": "/v3/offsite/",
		"data": {
			"check_only": true,
			"client_tracking_params": "CwABAAAAEDQxNDU0OTk0NDg3NDMyOTMGAAMABwsABwAAAApuZ2FwaS9wcm9kAA",
			"pin_id": "22236591903222945",
			"url": "https://i.pinimg.com/originals/5b/99/b8/5b99b8c9c2fd2818577598a4b52c854e.png"
		},
		"no_fetch_context_on_resource": false
	},
	"context": {}
}



https://www.pinterest.com/resource/RelatedPinFeedResource/get/?
source_url=/pin/iris-by-len-yan-on-deviant-art--860257966336607477/
&
data=
{
	"options": {
		"field_set_key": "unauth_react",
		"page_size": 12,
		"pin": "_pin_",
		"prepend": false,
		"add_vase": true,
		"show_seo_canonical_pins": true,
		"source": "unknown",
		"top_level_source": "unknown",
		"top_level_source_depth": 1,
		"bookmarks": ["_bookmark_"]
	},
	"context": {}
}
'''


class RelatedConfig:
    IMAGE_SEARCH_URL = "https://www.pinterest.com/resource/RelatedPinFeedResource/get/?"
    
    
    def __init__(self, search_keywords="", file_lengths=100, image_quality="orig", bookmarks=""):
        self.search_keywords = search_keywords
        self.file_lengths = file_lengths
        self.image_quality = image_quality
        self.bookmarks = bookmarks

    #image search url
    @property
    def search_url(self):
        return self.IMAGE_SEARCH_URL

    #search parameter "source_url"
    @property
    def source_url(self):
         return "/pin/{}/".format(self.search_keywords)

    #search parameter "data"
    @property
    def image_data(self): 
        DATA_TEMPLATE = '''{
                "options": {
                    "field_set_key": "unauth_react",
                    "page_size": 12,
                    "pin": "_pin_",
                    "prepend": false,
                    "add_vase": true,
                    "show_seo_canonical_pins": true,
                    "source": "unknown",
                    "top_level_source": "unknown",
                    "top_level_source_depth": 1,
                    "bookmarks": ["_bookmark_"]
                },
                "context": {}
            }
            '''
        DATA_NO_BOOKMARK = '''{
                    "options": {
                        "field_set_key": "unauth_react",
                        "page_size": 12,
                        "pin": "_pin_",
                        "prepend": false,
                        "add_vase": true,
                        "show_seo_canonical_pins": true,
                        "source": "unknown",
                        "top_level_source": "unknown",
                        "top_level_source_depth": 1
                    },
                    "context": {}
                }
                '''       
        if self.bookmarks == "":
            return DATA_NO_BOOKMARK.replace('_pin_', self.search_keyword)
        else:
            return DATA_TEMPLATE.replace('_pin_', self.search_keyword).replace('_bookmark_', self.bookmark)


    @property
    def search_keyword(self):
        return self.search_keywords
    
    @search_keyword.setter
    def search_keyword(self, search_keywords):
        self.search_keywords = search_keywords
    
    @property
    def file_length(self):
        return self.file_lengths
    
    @file_length.setter
    def file_length(self, file_lengths):
        self.file_lengths = file_lengths

    @property
    def image_quality(self):
        return self.image_qualitys
    
    @image_quality.setter
    def image_quality(self, image_qualitys):
        self.image_qualitys = image_qualitys

    @property
    def bookmark(self):
        return self.bookmarks

    @bookmark.setter
    def bookmark(self, bookmarks):
        self.bookmarks = bookmarks




class Config:
    IMAGE_SEARCH_URL = "https://pinterest.com/resource/BaseSearchResource/get/?"
    def __init__(self, search_keywords="", file_lengths=100, image_quality="orig", bookmarks=""):
        self.search_keywords = search_keywords
        self.file_lengths = file_lengths
        self.image_quality = image_quality
        self.bookmarks = bookmarks

    #image search url
    @property
    def search_url(self):
        return self.IMAGE_SEARCH_URL

    #search parameter "source_url"
    @property
    def source_url(self):
         return "/search/pins/?q=" + urllib.parse.quote(self.search_keyword)

    #search parameter "data"
    @property
    def image_data(self):        
        if self.bookmarks == "":
            return '''{"options":{"isPrefetch":false,"query":"''' + self.search_keyword + '''","scope":"pins","no_fetch_context_on_resource":false},"context":{}}'''
        else:
            return '''{"options":{"page_size":25,"query":"''' + self.search_keyword + '''","scope":"pins","bookmarks":["''' + self.bookmark + '''"],"field_set_key":"unauth_react","no_fetch_context_on_resource":false},"context":{}}'''.strip()

    @property
    def search_keyword(self):
        return self.search_keywords
    
    @search_keyword.setter
    def search_keyword(self, search_keywords):
        self.search_keywords = search_keywords
    
    @property
    def file_length(self):
        return self.file_lengths
    
    @file_length.setter
    def file_length(self, file_lengths):
        self.file_lengths = file_lengths

    @property
    def image_quality(self):
        return self.image_qualitys
    
    @image_quality.setter
    def image_quality(self, image_qualitys):
        self.image_qualitys = image_qualitys

    @property
    def bookmark(self):
        return self.bookmarks

    @bookmark.setter
    def bookmark(self, bookmarks):
        self.bookmarks = bookmarks
    