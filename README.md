# music_comment

爬取网易云，薛之谦热门30首歌曲的热门评论

利用技术 seleium+PhantomJS 也可以用seleium+FireFox 

网易云采取了框架，driver.switch_to.frame(driver.find_element_by_name("contentFrame"))

暂时只想到了模拟真实浏览器的行为。尝试解析post数据，发觉有两个js加密

试着查看了js怎么加密的，发觉写的乱七八操的，完全不是给人看的，最终放弃了

完成时间  2017年5月23日12:15:30

ps：有兴趣的人可以自己试着爬一次，会发觉并不是很容易哦

pps：需要包 beautifulsoup+selenium+phantomjs   自己pip安装














