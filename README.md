# ip_pool

通过本地ip库，对给定站点列表进行循环访问，刷访问量。

<s>通过爬取https://www.xicidaili.com/ 上的信息，构建本地代理ip池</s>
因为[西刺](https://www.xicidaili.com)爬下来的ip基本不能用，改为本地直接使用第三方ip库。

***

## 不采用requests库而使用urllib库？

亲测，在浏览器可以打开的前提下，同样的headers配置，用requests库返回503，而urllib返回200，如下
```
In [24]: res=requests.get('https://www.xicidaili.com/nn/',headers)                                                                                                           

In [25]: res.status_code                                                                                                                                                     
Out[25]: 503
```
```
In [27]: s = urllib.request.Request(url='https://www.xicidaili.com/nn/', headers=headers)                                                                                    

In [28]: con = urllib.request.urlopen(s)                                                                                                                                     

In [29]: con.status                                                                                                                                                          
Out[29]: 200
```

## 本地ip库建立

尝试了一下自己去爬取西刺上的ip，结果发现几乎没有可用的。索性直接站在巨人的肩膀上采用github上的项目[jhao104/proxy_pool](https://github.com/jhao104/proxy_pool)。

不直接在本地安装他的项目了，而是直接利用他提供的docker镜像，不过前提条件是本地有一个可被访问的redis实例。

### 运行redis容器，并自定义配置

这里需要自己写Dockerfile，将redis.conf传递到镜像中，并且做一个本地的卷积映射。

具体步骤可以参考我的博客[《Redis从入门到精通（4）：docker运行redis容器详解》](https://blog.csdn.net/Victor2code/article/details/104215310)

### 运行proxy_pool容器，连接到redis容器

直接将下面命令中的ip换成redis容器的ip，将密码也换成redis容器的配置文件中的密码即可
```
docker pull jhao104/proxy_pool

docker run --env db_type=REDIS --env db_host=127.0.0.1 --env db_port=6379 --env db_password=pwd_str -p 5010:5010 jhao104/proxy_pool
```

### 获取代理ip

直接利用API去访问
```
proxy=requests.get("http://127.0.0.1:5010/get/").json().get("proxy")
```
更多的API可以去原作者的项目中去查看

## 使用方法

* 首先按照上述方法启动两个容器，确保可以成功获得ip
* 编辑`sites.txt`存储待访问的链接列表
* 直接运行`use_proxy.py`即可
