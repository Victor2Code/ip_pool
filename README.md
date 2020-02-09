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

## 使用方法
