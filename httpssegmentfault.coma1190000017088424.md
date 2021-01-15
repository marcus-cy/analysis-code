https://segmentfault.com/a/1190000017088424
1.查看源代码 里能看到的数据，可以直接通过程序请求当前 URL 获取。
2.Elements 里的 HTML 代码 不等于 请求返回值，只能作为辅助。
3.Network里,一个个的条目，其中一个条目就代表一次发送请求和接收响应的过程。用内容关键字搜索，或保存成 HAR文件后搜索，找到包含数据的实际请求,

- Name：请求的名称，一般会将 URL 的最后一部分内容当作名称。
- Status：响应的状态码，这里显示为 200，代表响应是正常的。通过状态码，我们可以判断发送了请求之后是否得到了正常的响应。
- Type：请求的文档类型。这里为 document，代表我们这次请求的是一个 HTML 文档，内容就是一些 HTML 代码。
- Initiator：请求源。用来标记请求是由哪个对象或进程发起的。
- Size：从服务器下载的文件和请求的资源大小。如果是从缓存中取得的资源，则该列会显示 from cache。
- Time：发起请求到获取响应所用的总时间。
- Waterfall：网络请求的可视化瀑布流。

4.查看请求的具体信息，包括 方法、headers、参数 ，复制到程序里使用。


## Request
```
Requests 库是一个阻塞式 HTTP 请求库。
当我们发出一个请求后，程序会一直等待服务器响应，直到得到响应后，程序才会进行下一步处理。其实，这个过程比较耗费资源。如果程序可以在这个等待过程中做一些其他的事情，如进行请求的调度、响应的处理等，那么爬取效率一定会大大提高。

aiohttp 就是这样一个提供异步 Web 服务的库
```
## 请求

请求，由客户端向服务端发出，可以分为 4 部分内容：
- Request Method
get或post
- Request URL
- Request Headers
用来说明服务器要使用的附加信息，比较重要的信息有 Cookie、Referer、User-Agent；
Cookie：也常用复数形式 Cookies，这是网站为了辨别用户进行会话跟踪而存储在用户本地的数据。它的主要功能是维持当前访问会话
Referer：此内容用来标识这个请求是从哪个页面发过来的
- Request Body


## 解析库和解析方法
```
解析库:lxml、Beautiful Soup、pyquery 等。
解析方法:如 XPath 解析和 CSS 选择器解析
```

## 网页基础
- HTML：相当于骨架
不同类型的文字通过不同类型的标签来表示，如图片用 img 标签表示，视频用 video 标签表示，段落用 p 标签表示，它们之间的布局又常通过布局标签 div 嵌套组合而成，各种标签通过不同的排列和嵌套才形成了网页的框架
```
title 标签则定义了网页的标题
body 标签内则是在网页正文中显示的内容
div 标签定义了网页中的区块，它的 id 是 container，这是一个非常常用的属性，且 id 唯一的，我们可以通过它来获取这个区块。然
区块内又有一个 div 标签，它的 class 为 wrapper，这也是一个非常常用的属性，经常与 CSS 配合使用来设定样式。
```
- CSS： 相当于皮肤
  全称叫作 Cascading Style Sheets，即层叠样式表

- JavaScript：相当于肌肉

  ```
  简称 JS，是一种脚本语言。HTML 和 CSS 配合使用，提供给用户的只是一种静态信息，缺乏交互性。 JavaScript 实现了一种实时、动态、交互的页面功能。JavaScript 通常也是以单独的文件形式加载的，后缀为 js，在 HTML 中通过 script 标签即可引入
  
  我们在用 urllib 或 requests 抓取网页时，得到的源代码实际和浏览器中看到的不一样。
  
  这是一个非常常见的问题。现在网页越来越多地采用 Ajax、前端模块化工具来构建，整个网页可能都是由 JavaScript 渲染出来的，也就是说原始的 HTML 代码就是一个空壳
  ```

## CSS 

- 要选择文本节点，使用 `::text`

- 选择属性值，用`::attr(name)` name是指你想要的价值属性的名称

- | **选择器** | **含义**                                                     |
  | ---------- | ------------------------------------------------------------ |
  | *          | 通用元素选择器，匹配页面任何元素（这也就决定了我们很少使用） |
  | #id        | id选择器，匹配特定id的元素                                   |
  | .class     | 类选择器，匹配class**包含(不是等于)**特定类的元素            |
  | element    | 标签选择器 根据标签选择元素                                  |
  | [attr]     | 属性选择器 根据元素属性去选择                                |

- | **选择器**        | ***\*示例\**** | ***\*示例说明\****                   | **含义**                                                     |
| ----------------- | -------------- | ------------------------------------ | ------------------------------------------------------------ |
| elementE,elementF | div,p          | 选择所有<div>元素和<p>元素           | 多元素选择器，用”,分隔，同时匹配元素E或元素F                 |
| elementE elementF | div p          | 选择<div>元素内的所有<p>元素         | 后代选择器，用空格分隔，匹配E元素所有的**后代（不只是子元素、子元素向下递归）**元素F |
| elementE>elementF | div>p          | 选择所有父级是 <div> 元素的 <p> 元素 | 子元素选择器，用”>”分隔，匹配E元素的所有直接子元素           |
| elementE+elementF | div+p          | 选择所有紧接着<div>元素之后的<p>元素 | 直接相邻选择器，匹配E元素**之后**的**相邻**的**同级**元素F   |
| elementE~elementF | p~ul           | 选择p元素之后的每一个ul元素          | 普通相邻选择器，匹配E元素**之后**的**同级**元素F（无论直接相邻与否） |
| .class1.class2    | .user.login    | 匹配如<div class="user login">元素   | 匹配类名中既包含class1又包含class2的元素                     |

<img src="F:\gitcode\analysis-code\微信图片_20210111135712.png" alt="CSS1" style="zoom:67%;" />
<img src="F:\gitcode\analysis-code\微信图片_20210111135607.png" alt="CSS2" style="zoom:67%;" />
<img src="F:\gitcode\analysis-code\微信图片_20210111135801.png" alt="CSS3" style="zoom:67%;" />


## WebService
```
通过WebService，应用程序可以向全世界发布信息，或提供某项功能
Web Services 脚本平台需支持 XML + HTTP
Web Service 的本质，就是通过网络调用其他网站的资源
```
### Web框架
```
Flask是一个相对于Django而言轻量级的Web框架
所有的 python web 框架功能方式都一样：它们接收HTTP请求，然后分发任务，并生成 HTML，然后返回包含 HTML 的 HTTP 应答
```

## 代理协议区分
```
FTP 代理服务器：主要用于访问 FTP 服务器，一般有上传、下载以及缓存功能，端口一般为 21、2121 等。
HTTP 代理服务器：主要用于访问网页，一般有内容过滤和缓存功能，端口一般为 80、8080、3128 等。
SSL/TLS 代理：主要用于访问加密网站，一般有 SSL 或 TLS 加密功能（最高支持 128 位加密强度），端口一般为 443。
RTSP 代理：主要用于访问 Real 流媒体服务器，一般有缓存功能，端口一般为 554。
Telnet 代理：主要用于 telnet 远程控制（黑客入侵计算机时常用于隐藏身份），端口一般为 23。
POP3/SMTP 代理：主要用于 POP3/SMTP 方式收发邮件，一般有缓存功能，端口一般为 110/25。
SOCKS 代理：只是单纯传递数据包，不关心具体协议和用法，所以速度快很多，一般有缓存功能，端口一般为 1080。SOCKS 代理协议又分为 SOCKS4 和 SOCKS5，前者只支持 TCP，而后者支持 TCP 和 UDP，还支持各种身份验证机制、服务器端域名解析等。简单来说，SOCK4 能做到的 SOCKS5 都可以做到，但 SOCKS5 能做到的 SOCK4 不一定能做到
```

## Selenium

```
Selenium 是一个自动化测试工具.
利用它我们可以驱动浏览器执行特定的动作，如点击、下拉等操作。对于一些 JavaScript 渲染的页面来说，这种抓取方式非常有效
```

## PhantomJS
```
PhantomJS 是一个无界面的、可脚本编程的 WebKit 浏览器引擎
Selenium 支持 PhantomJS，这样在运行的时候就不会再弹出一个浏览器了
**Selenium 对应的三大主流浏览器的对接方式：Chrome、Firefox 、PhantomJS**
```
### 网站识别selenium原理：

```
爬虫程序借助渲染工具从动态网页中获取数据。
“借助”其实是通过对应的浏览器驱动（及Webdriver）向浏览器发出指令的行为。
开发者可以根据客户端是否包含浏览器驱动这一特征来区分正常用户和爬虫程序。
```

## Docker
```
Docker 是一种容器技术，可以将应用和环境等进行打包，形成一个独立的、类似于 iOS 的 App 形式的 “应用”,这个应用可以直接被分发到任意一个支持 Docker 的环境中，通过简单的命令即可启动运行。
Docker 是一种最流行的容器化实现方案。使用 Docker，可以让每个应用彼此相互隔离，在同一台机器上同时运行多个应用，不过它们彼此之间共享同一个操作系统。Docker 的优势在于，它可以在更细的粒度上进行资源管理，也比虚拟化技术更加节约资源。
```
## HTTPS 基本原理
```
HTTPS 的全称是 Hyper Text Transfer Protocol over Secure Socket Layer，是以安全为目标的 HTTP 通道，简单讲是 HTTP 的安全版，即 HTTP 下加入 SSL 层，简称为 HTTPS。
HTTPS 的安全基础是 SSL，因此通过它传输的内容都是经过 SSL 加密的，它的主要作用可以分为两种。

1.建立一个信息安全通道来保证数据传输的安全。
2.确认网站的真实性，凡是使用了 HTTPS 的网站，都可以通过点击浏览器地址栏的锁头标志来查看网站认证之后的真实信息，也可以通过 CA 机构颁发的安全签章来查询
```
## Scrapy框架
![kuangjia](F:\gitcode\analysis-code\13-1.jpg)

- Engine，引擎，用来处理整个系统的数据流处理，触发事务，是整个框架的核心。

- Item，项目，它定义了爬取结果的数据结构，爬取的数据会被赋值成该对象。

- Scheduler， 调度器，用来接受引擎发过来的请求并加入队列中，并在引擎再次请求的时候提供给引擎。

- Downloader，下载器，用于下载网页内容，并将网页内容返回给蜘蛛。

- Spiders，蜘蛛，其内定义了爬取的逻辑和网页的解析规则，它主要负责解析响应并生成提取结果和新的请求。

- Item Pipeline，项目管道，负责处理由蜘蛛从网页中抽取的项目，它的主要任务是清洗、验证和存储数据。

- Downloader Middlewares，下载器中间件，位于引擎和下载器之间的钩子框架，主要是处理引擎与下载器之间的请求及响应。

- Spider Middlewares， 蜘蛛中间件，位于引擎和蜘蛛之间的钩子框架，主要工作是处理蜘蛛输入的响应和输出的结果及新的请求。

```
Engine 首先打开一个网站，找到处理该网站的 Spider 并向该 Spider 请求第一个要爬取的 URL。
Engine 从 Spider 中获取到第一个要爬取的 URL 并通过 Scheduler 以 Request 的形式调度。
Engine 向 Scheduler 请求下一个要爬取的 URL。
Scheduler 返回下一个要爬取的 URL 给 Engine，Engine 将 URL 通过 Downloader Middlewares 转发给 Downloader 下载。
一旦页面下载完毕， Downloader 生成一个该页面的 Response，并将其通过 Downloader Middlewares 发送给 Engine。
Engine 从下载器中接收到 Response 并通过 Spider Middlewares 发送给 Spider 处理。
Spider 处理 Response 并返回爬取到的 Item 及新的 Request 给 Engine。
Engine 将 Spider 返回的 Item 给 Item Pipeline，将新的 Request 给 Scheduler。
重复第二步到最后一步，直到  Scheduler 中没有更多的 Request，Engine 关闭该网站，爬取结束。
```

```
scrapy.cfg：它是 Scrapy 项目的配置文件，其内定义了项目的配置文件路径、部署相关信息等内容。
items.py：它定义 Item 数据结构，所有的 Item 的定义都可以放这里。
pipelines.py：它定义 Item Pipeline 的实现，所有的 Item Pipeline 的实现都可以放这里。
settings.py：它定义项目的全局配置。
middlewares.py：它定义 Spider Middlewares 和 Downloader Middlewares 的实现。
spiders：其内包含一个个 Spider 的实现，每个 Spider 都有一个文件。
```



### Scrap项目创建

- 1.windows中cmd环境下执行：`scrapy startproject 项目名`
若报错 “ImportError:DLL load failed”，执行 `pip install -I cryptography`
- 2.`cd 项目名`；`scrapy genspider 爬虫文件名 所爬网站`
### Item创建
Item 是保存爬取数据的容器，它的使用方法和字典类似。不过，相比字典，Item 多了额外的保护机制，可以避免拼写错误或者定义字段错误。
创建 Item 需要继承 scrapy.Item 类，并且定义类型为 scrapy.Field 的字段

### Response解析
parse() 方法的参数 response 是 start_urls 里面的链接爬取后的结果。所以在 parse() 方法中，我们可以直接对 response 变量包含的内容进行解析，提取的方式可以是 CSS 选择器或 XPath 选择器

### Request
上面的操作实现了从初始页面抓取内容。那么，下一页的内容该如何抓取？这就需要我们从当前页面中找到信息来生成下一个请求，然后在下一个请求的页面里找到信息再构造再下一个请求。这样循环往复迭代，从而实现整站的爬取。

start_requests()，此方法用于生成初始请求，它必须返回一个可迭代对象，此方法会默认使用 start_urls 里面的 URL 来构造 Request，而且 Request 是 GET 请求方式。如果我们想在启动时以 POST 方式访问某个站点，可以直接重写这个方法，发送 POST 请求时我们使用 FormRequest 即可

### Downloader Middleware 

Downloader Middleware 的功能十分强大，修改 User-Agent、处理重定向、设置代理、失败重试、设置 Cookies 等功能都需要借助它来实现。下面我们来了解一下 Downloader Middleware 的详细用法。在整个架构中起作用的位置是以下两个。

- 在 Scheduler 调度出队列的 Request 发送给 Downloader 下载之前，也就是我们可以在 Request 执行下载之前对其进行修改。
- 在下载后生成的 Response 发送给 Spider 之前，也就是我们可以在生成 Resposne 被 Spider 解析之前对其进行修改。

### Item Pipeline

- process_item(item, spider)

- open_spider(spider)
- close_spider(spider)
- from_crawler(cls, crawler)

### Scrapy对接Selenium
Scrapy 抓取页面的方式和 requests 库类似，都是直接模拟 HTTP 请求，而 Scrapy 也不能抓取 JavaScript 动态渲染的页面。抓取 JavaScript 渲染的页面有两种方式
一种是分析 Ajax 请求，找到其对应的接口抓取，Scrapy 同样可以用此种方式抓取。
另一种是直接用 Selenium 或 Splash 模拟浏览器进行抓取，我们不需要关心页面后台发生的请求，也不需要分析渲染过程，只需要关心页面最终结果即可，可见即可爬。那么，如果 Scrapy 可以对接 Selenium，那 Scrapy 就可以处理任何网站的抓取了

当 process_request() 方法返回 Response 对象的时候，更低优先级的 Downloader Middleware 的 process_request() 和 process_exception() 方法就不会被继续调用了，转而开始执行每个 Downloader Middleware 的 process_response() 方法，调用完毕之后直接将 Response 对象发送给 Spider 来处理。

这里直接返回了一个 HtmlResponse 对象，它是 Response 的子类，返回之后便顺次调用每个 Downloader Middleware 的 process_response() 方法。而在 process_response() 中我们没有对其做特殊处理，它会被发送给 Spider，传给 Request 的回调函数进行解析。