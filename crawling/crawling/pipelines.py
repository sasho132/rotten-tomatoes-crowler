# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from best_movies.movie.models import Movie

def clean_title(param):
    return param


class CrawlingPipeline:
    def process_item(self, item, spider):
        return item
