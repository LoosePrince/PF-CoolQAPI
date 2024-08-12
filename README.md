## 公告
> 看 [GUGUbot](https://github.com/LoosePrince/PF-GUGUBot) 的公告

# PF-CoolQ API
> PFingan服务器迁移和维护的CoolQAPI插件

[![页面浏览量计数](https://badges.toozhao.com/badges/01J53MWT9TCPVNH36K8Y5PGY72/green.svg)](/) 
[![查看次数起始时间](https://img.shields.io/badge/查看次数统计起始于-2024%2F08%2F12-1?style=flat-square)](/)
[![仓库大小](https://img.shields.io/github/repo-size/LoosePrince/PF-CoolQAPI?style=flat-square&label=仓库占用)](/) 
[![最新版](https://img.shields.io/github/v/release/LoosePrince/PF-CoolQAPI?style=flat-square&label=最新版)](https://github.com/LoosePrince/PF-CoolQAPI/releases/latest/download/GUGUbot.mcdr)
[![Issues](https://img.shields.io/github/issues/LoosePrince/PF-CoolQAPI?style=flat-square&label=Issues)](https://github.com/LoosePrince/PF-CoolQAPI/issues) 
[![已关闭issues](https://img.shields.io/github/issues-closed/LoosePrince/PF-CoolQAPI?style=flat-square&label=已关闭%20Issues)](https://github.com/LoosePrince/PF-CoolQAPI/issues?q=is%3Aissue+is%3Aclosed)
[![下载量](https://img.shields.io/github/downloads/LoosePrince/PF-CoolQAPI/total?style=flat-square&label=下载量)](https://github.com/LoosePrince/PF-CoolQAPI/releases)
[![最新发布下载量](https://img.shields.io/github/downloads/LoosePrince/PF-CoolQAPI/latest/total?style=flat-square&label=最新版本下载量)](https://github.com/LoosePrince/PF-CoolQAPI/releases/latest)

本插件修改自`CoolQAPI`,`CoolQAPI`目前已更新为 [QQAPI](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/qq_api) | [原作者：AnzhiZhang](https://github.com/AnzhiZhang) <br>
技术支持：XueK__ [前往主页](https://github.com/XueK66)

> #### 这是基于原插件的修改版本
<br></br>

使用方式：
* 将Release里面的CoolQAPI.zip解压后放入`/plugins`
* 加载后，在`/config/CoolQAPI/config.yml`中配置服务
* 注意修改`CoolQAPI`的`command_prefix`的为`#`，否则使用不了`GUGUBot`的`命令`功能

## 依赖
#### Python包
- [Python™](https://www.python.org/)
#### Python模块
- 已存储在插件对应的文件夹内的 [requirements.txt](requirements.txt) 中, 可以使用 `pip install -r requirements.txt` 安装
#### 前置插件
- 无

# CoolQAPI配置

## 说明

### QQ Bot 配置
>配置方法部分源自原始插件说明

推荐使用
- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) : 适用多个平台，但是容易风控
- [LLOneBot](https://github.com/LLOneBot/LLOneBot) : 不易风控，仅适用于QQNT，是 `LiteLoaderQQNT` 的附属插件
#### 使用go-cqhttp
在`account`字段中设置QQ帐号和密码：

```yaml
account:
  uin: 1233456
  password: ''
```

#### 使用LLOneBot
- 消息上传格式: CQ码
- 更多更详细的LLOneBot教程请看 [LLOneBot快速开始](https://llonebot.github.io/zh-CN/guide/getting-started)

#### 使用 HTTP
将配置中的 `http` 设置为 `true` ，将 `websocket` 设置为 `false` 。 然后在 go-cqhttp 配置的 `servers` 字段中设置 `http` （此配置应与CoolQAPI配置内容匹配）：

```yaml
servers:
  - http:
      address: 0.0.0.0:5700
      post:
      - url: http://127.0.0.1:5701/
```

### CoolQAPI配置文件
**更改CoolQAPI配置需重启服务器才会生效！！**

> 
>  
> | 配置项 | 默认值 | 说明 |
> | - | - | - |
> | post_host | `127.0.0.1` | 接收数据上报的地址 |
> | post_port | `5701` | 对应 go-cqhttp `url` 配置的端口 | 
> | post_path | `post` | 对应 go-cqhttp `url` 配置的终点名 |
> | api_host | `127.0.0.1` | 对应 go-cqhttp 的地址 |
> | api_port | `5700` | 对应 go-cqhttp 的 HTTP 监听端口 |
> | command_prefix | `/` | 需要修改成`#`以启用机器人函数功能 | 
> ```yaml
> api_host: 127.0.0.1
> api_port: 5700 
> command_prefix: "#"
> post_host: 127.0.0.1 
> post_path: ""    
> post_port: 5701 
> ```
> 机器人监听地址 = http://api_host:api_port
> 
> 机器人反向地址 = http://post_host:post_port/post_path/
>
> 由于机器人默认反向地址`http://127.0.0.1:5701/`没有post_path，所以CoolQAPI中post_path留空。
> 

### 开发
> 无

# 有BUG或是新的IDEA
如果需要更多联动或提交想法和问题请提交 [issues](https://github.com/LoosePrince/PF-CoolQAPI/issues) 或 QQ [1377820366](http://wpa.qq.com/msgrd?v=3&uin=1377820366&site=qq&menu=yes) 提交！ <br />
视情况添加，请勿联系他人（开发者：[雪开](https://github.com/XueK66)）
