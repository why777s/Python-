# Python爬虫学习
### 1.猫眼电影  
工具和环境：python3.5 scrapy1.5 mongodb  
之前用BeautifulSoup写过这个，最近刚学了scrapy，用scrapy写了这个爬虫，爬取猫眼电影网站上Top100电影的信息，将结果存至mongodb 
### 2.Boss直聘
工具和环境：python3.5 scrapy1.5 mongodb  
项目里两个爬虫，第一个用来爬取BOSS直聘首页上的职位分类（爬下来大概有700多个），并且将结果（分类名和url）保存至MongoDB。第二个爬取所有分类职位具体页面下的所有职位信息并且保存至MongoDB。（csv文件中展示了部分的爬取结果，jt.csv是爬取到的职位分类的信息。 ） 
