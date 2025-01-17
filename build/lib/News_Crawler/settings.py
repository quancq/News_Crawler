# -*- coding: utf-8 -*-

# Scrapy settings for News_Crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'News_Crawler'

SPIDER_MODULES = ['News_Crawler.spiders']
NEWSPIDER_MODULE = 'News_Crawler.spiders'

# LOG_LEVEL = "INFO"
# FEED_URI = "./Data/Archive/%(name)s/%(time)s.csv"
# FEED_FORMAT = "csv"
# FEED_EXPORT_ENCODING = "utf-8"
# FEED_EXPORT_FIELDS = ["lang", "category", "time", "url", "title", "intro", "content"]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'News_Crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# DEPTH_PRIORITY = -1

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'News_Crawler.middlewares.NewsCrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'News_Crawler.middlewares.NewsCrawlerDownloaderMiddleware': 543,
#}

# Proxy middleware settings
# Retry many times since proxies often fail
# RETRY_TIMES = 5
# Retry on most error codes since proxies fail for different reasons
# RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

DOWNLOADER_MIDDLEWARES = {
    # 'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    # 'scrapy_proxies.RandomProxy': 100,
    "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 110,
}

# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port
# ...
PROXY_LIST = "./News_Crawler/Proxy/proxy_list.txt"

# Proxy mode
# 0 = Every requests have different proxy
# 1 = Take only one proxy from the list and assign it to every requests
# 2 = Put a custom proxy to use in the settings
PROXY_MODE = 0

# If proxy mode is 2 uncomment this sentence :
#CUSTOM_PROXY = "http://host1:port"


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
	"News_Crawler.pipelines.ValidItemPipeline": 100,
    "News_Crawler.pipelines.CleanItemPipeline": 200,
    # "News_Crawler.pipelines.TransformItemPipeline": 250,
    # "News_Crawler.pipelines.SaveFilePipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
