https://segmentfault.com/a/1190000017088424
1.查看源代码 里能看到的数据，可以直接通过程序请求当前 URL 获取。
2.Elements 里的 HTML 代码 不等于 请求返回值，只能作为辅助。
3.Network里用内容关键字搜索，或保存成 HAR文件后搜索，找到包含数据的实际请求
4.查看请求的具体信息，包括 方法、headers、参数 ，复制到程序里使用。



网站识别selenium原理：

```
爬虫程序可以借助渲染工具从动态网页中获取数据，“借助”其实是通过对应的浏览器驱动（及Webdriver）向浏览器发出指令的行为。也就是说，开发者可以根据客户端是否包含浏览器驱动这一特征来区分正常用户和爬虫程序。
```
