# Scrapy settings for spiderProject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spiderProject'

SPIDER_MODULES = ['spiderProject.spiders']
NEWSPIDER_MODULE = 'spiderProject.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spiderProject (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 2

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
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
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'spiderProject.middlewares.SpiderprojectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'spiderProject.middlewares.RandomProxyMiddlewate': 749,
}
DOWNLOAD_TIMEOUT = 10  #默认180秒,设置10秒即可

TELNETCONSOLE_USERNAME='aa' #Telnet 账号
TELNETCONSOLE_PASSWORD='bb' #Telnet 密码
TELNETCONSOLE_PORT = [6024] #Telnet 端口
TELNETCONSOLE_HOST = '127.0.0.1' #Telnet 链接主机

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
   'scrapy.extensions.telnet.TelnetConsole': None,
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'spiderProject.pipelines.SpiderprojectPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#代理列表
SUNPROXYS = [
    'http://136.243.211.104:80',
    'http://39.106.223.134:80',
    'http://39.102.32.69:3128',
    'http://167.71.5.83:3128',
    'http://60.191.11.241:3128',
    'http://74.143.245.221:80',
    'http://120.55.39.108:80',
    'http://194.44.78.22:55443',
    'http://47.113.111.149:80',
    'http://103.17.102.3:8080',
    'http://37.49.127.238:8080',
    'http://18.180.152.249:80',
    'http://84.192.135.91:80',
    'http://94.180.106.94:32767',
    'http://46.229.187.169:53281',
    'http://193.136.119.10:80',
    'http://178.47.141.85:2580',
    'http://150.129.148.88:35101',
    'http://46.223.255.2:8080',
    'http://46.237.255.5:8080',
    'http://37.49.127.234:8080',
    'http://8.129.126.49:80',
    'http://51.178.55.187:9963',
    'http://47.115.83.125:80',
    'http://103.78.254.78:80',
    'http://138.68.60.8:8080',
    'http://66.209.54.230:8080',
    'http://118.179.223.130:80',
    'http://132.248.196.2:8080',
    'http://140.238.71.22:3128',
    'http://45.6.4.60:8080',
    'http://109.193.195.8:8080',
    'http://41.65.146.38:8080',
    'http://103.28.121.58:3128',
    'http://223.82.106.253:3128',
    'http://116.73.14.16:8080',
    'http://189.39.123.238:8080',
    'http://47.115.15.170:80',
    'http://103.148.216.5:80',
    'http://191.7.20.94:3128',
    'http://47.97.166.23:80',
    'http://191.101.39.45:80',
    'http://200.41.150.83:54958',
    'http://134.3.255.7:8080',
    'http://192.241.172.93:8080',
    'http://46.0.203.186:8080',
    'http://91.214.31.234:8080',
    'http://116.117.134.135:80',
    'http://176.9.119.170:8080',
    'http://46.4.168.53:80',
    'http://144.202.113.90:8080',
    'http://196.0.34.142:33855',
    'http://157.90.4.42:8003',
    'http://183.88.226.50:8080',
    'http://47.115.116.5:80',
    'http://120.222.17.151:3128',
    'http://157.90.0.85:8099',
    'http://51.75.164.68:8080',
    'http://125.26.7.83:8080',
    'http://103.36.35.135:8080',
    'http://78.42.42.35:3128',
    'http://198.199.86.11:3128',
    'http://52.78.172.171:80',
    'http://218.253.39.60:8380',
    'http://217.8.51.198:8080',
    'http://46.237.255.3:8080',
    'http://149.172.255.10:8080',
    'http://170.238.10.129:999',
    'http://72.23.14.208:80',
    'http://41.223.143.78:3128',
    'http://191.101.39.48:80',
    'http://46.5.252.61:8080',
    'http://103.154.65.218:8080',
    'http://14.225.11.126:8080',
    'http://121.8.146.99:8060',
    'http://181.225.41.131:8080',
    'http://46.5.252.62:8080',
    'http://195.110.7.195:3121',
    'http://134.3.255.9:8080',
    'http://201.91.82.155:3128',
    'http://47.112.237.208:80',
    'http://136.228.131.67:8080',
    'http://47.88.7.18:8088',
    'http://47.115.73.176:80',
    'http://154.16.202.22:3128',
    'http://128.199.202.122:8080',
    'http://170.254.224.7:55443',
    'http://43.249.224.172:84',
    'http://115.85.73.179:3128',
    'http://217.8.51.197:8080',
    'http://139.162.78.109:3128',
    'http://47.75.90.57:80',
    'http://47.57.188.208:80',
    'http://51.81.82.175:2003',
    'http://191.96.42.80:3128',
    'http://47.112.152.228:80',
    'http://120.232.150.100:80',
    'http://191.96.71.118:3128',
    'http://52.229.51.93:80',
    'http://200.115.108.2:8080',
    'http://177.99.206.82:8080',
    'http://193.25.120.80:8080',
    'http://134.209.29.120:8080',
    'http://143.137.204.6:80',
    'http://145.40.68.155:80',
    'http://94.199.75.171:8080',
    'http://212.164.52.198:80',
    'http://175.212.226.65:80',
    'http://153.126.137.205:9666',
    'http://82.212.62.20:8080',
    'http://212.174.242.114:8080',
    'http://117.28.246.15:80',
    'http://52.229.15.151:80',
    'http://91.89.89.12:8080',
    'http://61.183.176.122:57210',
    'http://39.101.221.247:9999',
    'http://45.71.201.122:999',
    'http://191.101.39.38:80',
    'http://52.149.152.236:80',
    'http://14.119.82.122:80',
    'http://118.163.94.3:80',
    'http://181.98.174.28:80',
    'http://134.3.255.4:8080',
    'http://103.120.144.144:80',
    'http://101.132.111.208:8082',
    'http://194.146.32.18:80',
    'http://43.129.20.96:80',
    'http://137.59.155.14:80',
    'http://46.4.96.137:3128',
    'http://45.4.85.152:9991',
    'http://120.196.112.6:3128',
    'http://168.119.103.160:10303',
    'http://45.190.185.10:3128',
    'http://45.165.131.6:8080',
    'http://41.76.155.134:8080',
    'http://111.23.16.250:3128',
    'http://05.252.161.48:8080',
    'http://217.8.51.206:8080',
    'http://132.145.18.53:80',
    'http://120.77.215.57:80',
    'http://77.38.21.239:8080',
    'http://161.35.70.249:8080',
    'http://88.198.50.103:3128',
    'http://82.212.62.27:8080',
    'http://114.233.169.89:8003',
    'http://186.157.242.229:8080',
    'http://118.194.242.156:80',
    'http://45.179.200.129:999',
    'http://52.142.220.26:80',
    'http://103.37.141.69:80',
    'http://114.233.169.63:8048',
    'http://154.16.63.16:3128',
    'http://178.212.54.137:8080',
    'http://47.95.205.25:8080',
    'http://41.215.85.74:8080',
    'http://176.9.75.42:8080',
    'http://85.216.127.188:8080',
    'http://47.116.76.219:80',
    'http://149.172.255.2:8080',
    'http://202.29.220.242:8080',
    'http://34.233.217.185:8080',
    'http://181.188.150.91:3128',
    'http://114.112.127.81:80',
    'http://175.141.69.200:80',
    'http://186.0.231.140:999',
    'http://91.202.230.219:8080',
    'http://5.252.161.48:8080',
    'http://47.99.209.194:80',
    'http://109.86.182.203:3128',
    'http://138.219.56.42:999',
    'http://79.120.177.106:8080',
    'http://103.127.93.94:80',
    'http://189.206.105.164:80',
    'http://85.216.127.182:8080',
    'http://118.137.167.216:8080',
    'http://222.112.240.162:80',
    'http://116.117.134.134:80',
    'http://106.51.252.229:80',
    'http://106.53.233.125:3128',
    'http://37.49.127.227:8080',
    'http://139.59.1.14:3128',
    'http://54.89.61.128:80',
    'http://78.42.42.44:3128',
    'http://150.109.32.166:80',
    'http://101.255.171.106:8080',
    'http://102.129.249.120:8080',
    'http://108.30.242.18:8080',
    'http://195.123.247.22:3128',
    'http://201.248.234.175:3128',
    'http://47.103.130.208:38888',
    'http://192.109.165.95:80',
    'http://203.142.69.179:8080',
    'http://203.202.245.58:80',
    'http://77.68.125.33:80',
    'http://118.127.99.93:53281',
    'http://75.119.144.28:80',
    'http://27.148.248.197:8091',
    'http://70.169.141.35:3128',
    'http://91.89.89.4:8080',
    'http://186.190.224.234:999',
    'http://182.92.239.16:8080',
    'http://51.89.182.224:8080',
    'http://103.98.128.51:8080',
    'http://123.194.89.104:8380',
    'http://217.8.51.199:8080',
    'http://78.42.42.42:8080',
    'http://120.232.150.110:80',
    'http://47.244.50.194:8081',
    'http://8.129.123.133:80',
    'http://80.211.179.30:3128',
    'http://186.248.173.74:8080',
    'http://84.244.69.29:8080',
    'http://60.255.151.82:80',
    'http://47.112.237.100:80',
    'http://124.48.218.245:80',
    'http://93.152.172.209:8080',
    'http://202.83.125.254:80',
    'http://95.208.208.233:8080',
    'http://159.203.61.169:8080',
    'http://82.212.62.24:8080',
    'http://175.212.226.67:80',
    'http://122.224.65.197:3128',
    'http://209.97.150.167:8080',
    'http://58.120.171.37:8080',
    'http://58.176.147.14:8193',
    'http://202.61.51.204:3128',
    'http://189.80.3.187:8080',
    'http://103.19.129.114:83',
    'http://212.129.29.139:80',
    'http://175.141.69.203:80',
    'http://31.14.49.1:8080',
    'http://88.198.24.108:8080',
    'http://49.85.189.121:8057',
    'http://181.143.106.162:52151',
    'http://46.223.255.4:3128',
    'http://118.194.242.40:80',
    'http://191.97.16.202:999',
]