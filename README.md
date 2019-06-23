# blog_to_csdn

> markdown 格式的文件，发布到csdn

效果图：

![](https://beer-1256523277.cos.ap-shanghai.myqcloud.com/20190623091626_8c31bfeeccf70c2b4152ba5a2a5dda27.png)

### 缺点

需要手动配置 cookies.(我也不知道怎么获取。。。只支持微信扫码，比较繁琐)。

https://mp.csdn.net/mdeditor

发表一个测试文章，然后复制 cookie

```
cookies = "TINGYUN_DATA=%7B%22id%22%3A%22-sf2Cni530g%23HL5wvli0FZI%22%2C%22n%22%3A%22WebAction%2FCI%2Fmdeditor%252Findex%22%2C%22tid%22%3A%22ac9b3a77a3edba%22%2C%22q%22%3A0%2C%22a%22%3A71%7D; uuid_tt_dd=10_37072415380-1556441151636-475857; UM_distinctid=16a631fad40109-051bae8c54bc5d-9333061-1fa400-16a631fad41245; UN=qq_30009669; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_37072415380-1556441151636-475857!5744*1*qq_30009669!1788*1*PC_VC; smidV2=20190606120249fff51bdcc7873918bbd630e5a454f77a00c39559b932e4060; dc_session_id=10_1560941260118.938240; hasSub=true; c_adb=1; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1561194265,1561195400,1561196568,1561196575; TINGYUN_DATA=%7B%22id%22%3A%22-sf2Cni530g%23HL5wvli0FZI%22%2C%22n%22%3A%22WebAction%2FCI%2FpostList%252Flist%22%2C%22tid%22%3A%22aca7d112b0182e%22%2C%22q%22%3A0%2C%22a%22%3A65%7D; UserName=qq_30009669; UserNick=Beer+Home; AU=3E7; BT=1561196771040; p_uid=U000000; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1561197331; dc_tos=pthvkk"
```

![](https://beer-1256523277.cos.ap-shanghai.myqcloud.com/20190622180319_fefe56307a3d60f3d99fbadc866077a4.png)


如果直接在页面上：

![20190622181140_d26187bf3275e026b89dd7e816e7b275.png](https://beer-1256523277.cos.ap-shanghai.myqcloud.com/20190622181140_d26187bf3275e026b89dd7e816e7b275.png)

获取到的 cookies  比较，就多了个这个：

```
TINGYUN_DATA=%7B%22id%22%3A%22-sf2Cni530g%23HL5wvli0FZI%22%2C%22n%22%3A%22WebAction%2FCI%2Fmdeditor%252Findex%22%2C%22tid%22%3A%22ac9b3a77a3edba%22%2C%22q%22%3A0%2C%22a%22%3A71%7D
```

解码后：
```python
{"id":"-sf2Cni530g#HL5wvli0FZI","n":"WebAction/CI/mdeditor%2Findex","tid":"ac9b3a77a3edba","q":0,"a":71}
```

也不知道他这个的生成规则是个啥！！！。不过，没事，至少是半自动化。

### 简介

支持本地 markdown 文件格式，发送到 csdn。

例如 :
```

---
title: 2019
tags: [随记,list]
date: 2018-12-30 20:00:00
---

- [ ] 减肥到140
- [x] 买个Mac
- [ ] 黄山
<!--more-->
```
解析，title为：2019，tags 为: [随记,list]。
内容为：
```python

- [ ] 减肥到140
- [x] 买个Mac
- [ ] 黄山
```

### 文件
#### config

```python
# cookies
cookies = ""
# csdn 发表文章的 url
csdn_url = "https://mp.csdn.net/mdeditor/saveArticle"
# 本地博客存放的位置
path = 'E:\\beer\\csdn\\'
```

#### csdn

class csdn
````python
class Csdn:

    def __init__(self, cookies, url,form_data):
        self.cookies = cookies
        self.url = url
        self.headers = self.build_headers(self)
        self.form_data = form_data

    @staticmethod
    def build_headers(self):
        headers = {'cookie': self.cookies}
        return headers
````

#### blog_to_csdn 

核心代码

步骤

- 获取文件列表 （最大为 10 个文件，csdn 每天的最大量为 10）

![20190622180135_1840994e2fad8f89c9947ca91492d03f.png](https://beer-1256523277.cos.ap-shanghai.myqcloud.com/20190622180135_1840994e2fad8f89c9947ca91492d03f.png)

- 读取文件内容，并转为 html 格式
- 使用 requests 构造，post 发送
- 解析返回结果

```python
if __name__ == '__main__':
    cookies = config.cookies
    path = config.path
    csdn_url = config.csdn_url

    file_list = get_all_file(path)
    for file in file_list:
        content, title, tags = get_content(path + file)
        content_html = markdown.markdown(content)
        form_data = build_form_data(title, content, content_html, tags)
        csdn_obj = csdn.Csdn(cookies, csdn_url, form_data)
        result = put_article(csdn_obj)
        if result is not None:
            print("file: " + file + "; status: " + result)
```