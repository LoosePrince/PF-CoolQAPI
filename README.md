## 公告
> 2024/1/14
> - PFingan服务器已宣布关服，本插件将面临可能无限期的停更

> 2024/06/18
> - `CoolQ API` 已失联，所幸的是我们保留的一份存档，请点击 [CoolQ API](https://github.com/LoosePrince/PF-GUGUBot/releases/download/GUGUbot-v1.0.6-CoolQAPI/CoolQAPI.zip) 下载存档。 
> - 请注意，存档版本是我们服务器此前使用的版本，理论上不会出现问题（原有版本在新版MCDR已不兼容，但是我们为它更新了一下兼容），然后请注意 **解压** 文件，而不是直接拖入插件目录。

> 2024/08/01
> - 在 `CoolQ API` 恢复正常或者我们彻底抛弃它之前将会由我们进行维护。预计将不会有功能上的更新。
> - 关于对 `CoolQ API` 的反馈我们仅接受与 `GUGUbot` 相关的部分，有关其它插件的交互和维护我们可能没有这个精力。
# PF-QQchat
> PFingan服务器MCDRQQ机器人插件

[![页面浏览量计数](https://badges.toozhao.com/badges/01H98QXADB4DYZBRC2EHSEJ4HW/green.svg)](/) 
[![查看次数起始时间](https://img.shields.io/badge/查看次数统计起始于-2023%2F9%2F2-1?style=flat-square)](/)
[![仓库大小](https://img.shields.io/github/repo-size/LoosePrince/PF-GUGUBot?style=flat-square&label=仓库占用)](/) 
[![最新版](https://img.shields.io/github/v/release/LoosePrince/PF-GUGUBot?style=flat-square&label=最新版)](https://github.com/LoosePrince/PF-GUGUBot/releases/latest/download/GUGUbot.mcdr)
[![Issues](https://img.shields.io/github/issues/LoosePrince/PF-GUGUBot?style=flat-square&label=Issues)](https://github.com/LoosePrince/PF-GUGUBot/issues) 
[![已关闭issues](https://img.shields.io/github/issues-closed/LoosePrince/PF-GUGUBot?style=flat-square&label=已关闭%20Issues)](https://github.com/LoosePrince/PF-GUGUBot/issues?q=is%3Aissue+is%3Aclosed)
[![下载量](https://img.shields.io/github/downloads/LoosePrince/PF-GUGUBot/total?style=flat-square&label=下载量)](https://github.com/LoosePrince/PF-GUGUBot/releases)
[![最新发布下载量](https://img.shields.io/github/downloads/LoosePrince/PF-GUGUBot/latest/total?style=flat-square&label=最新版本下载量)](https://github.com/LoosePrince/PF-GUGUBot/releases/latest)

本插件修改自： [QQChat-用于连接Minecraft和QQ的插件](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/qq_chat) [原作者](https://github.com/AnzhiZhang) <br>
技术支持：XueK__ [前往主页](https://github.com/XueK66)
<br></br>

> #### 这是基于原插件的修改版本

使用方式：
* 将Release里面的GUGUbot.mcdr放入`/plugins`
* 将解压后的CoolQAPI放入`/plugins`
* 加载后，在`/config/GUGUbot/config.yml`中配置机器人
* 加载后，在`/config/CoolQAPI/config.yml`中配置服务
* 注意修改`CoolQAPI`的`command_prefix`的为`#`，否则使用不了`命令`功能

## 依赖
#### Python包
- [Python™](https://www.python.org/)
#### Python模块
- 已存储在插件对应的文件夹内的 [requirements.txt](requirements.txt) 中, 可以使用 `pip install -r requirements.txt` 安装
#### 前置插件
- [CoolQAPI](https://github.com/AnzhiZhang/CoolQAPI)
#### 已废弃的前置插件

> <details>
>  
> [OnlinePlayerAPI](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/.archived/OnlinePlayerAPI) <br> 
> [ConfigAPI](https://github.com/MCDReforged/ConfigAPI) <br>
> [JsonDataAPI](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/.archived/JsonDataAPI)
>
> </details>

## 功能列表
> QQ部分帮助，向QQ机器人发送，可以私聊也可以群聊发送 `#帮助`

基本功能：聊天互相转发

#### 1.绑定游戏ID到QQ号
> 请注意，本插件的绑定功能不可关闭

#### 2.获取玩家和假人的在线情况
#### 3.QQ管理群
设定的QQ群内所有人都有管理员权限
```yml
admin_group_id:
- 123321
- 456654
```

#### 4.在QQ管理服务器白名单
同时支持正版和离线，详查[#36](https://github.com/LoosePrince/PF-GUGUBot/issues/36)
```yml
#配置文件
whitelist: true/false #（开启/关闭）
```
#### 5.服务器启动指令
在服务器启动时自动执行的指令。在某些特殊情况下会用到，可能可以救你一命
```yml
#配置文件
start_command: true/false #（开启/关闭）
```
#### 6.违禁词撤回
需要机器人有管理员
#### 7.群内&游戏内关键词回复
群内和游戏内关键词是分开设置的，群内关键词支持图片回复
#### 8.UUID管理
#### 9.机器人名字显示在线人数
通过机器人进行修改！
```yml
#配置文件
name: true/false #（开启/关闭）
```
#### 10.协助审核
添加协助审核功能，这通常是提供给有一套审核方案的服务器使用的<br>通过机器人添加审核员和对应别名，当有人申请加群时会将申请信息发送到审核员私信（如果绑定了游戏ID的同时还在线那么还会发送到游戏内），此时回复同意即可快速通过，也可以仅当作提醒功能
```yml
#配置文件
shenhe: true/false #（开启/关闭）
```
#### 11.机器人对话风格自定义
#### 12.在QQ删除服务器内假人

## 帮助提示
> 部分功能在群聊和私聊都能使用，以下内容较长请展开查看
#### 管理员部分，请私聊机器人
<details>
  
```
#绑定   -> 查看绑定相关帮助
#白名单 -> 查看白名单相关帮助
#启动指令 -> 查看启动指令相关帮助
#违禁词 -> 查看违禁词相关帮助
#关键词 -> 查看关键词相关帮助
#游戏内关键词 -> 查看游戏内关键词相关帮助
#uuid   -> 查看uuid 匹配相关帮助
#名字   -> 查看机器人名字相关帮助
#审核   -> 协助审核功能
```

> <details>
> 
> 游戏ID与QQ绑定 
> - `#绑定`
> ```
> #绑定 列表 -> 查看绑定列表
> #绑定 查询 <QQ号> -> 查询绑定ID
> #绑定 解绑 <QQ号> -> 解除绑定
> #绑定 <QQ号> <游戏ID> -> 绑定新ID
> ```
> 白名单管理 
> - `#白名单`
> ```
> #白名单 添加 <target> -> 添加白名单成员
> #白名单 列表 -> 列出白名单成员
> #白名单 关   -> 关闭白名单
> #白名单 开   -> 开启白名单
> #白名单 重载 -> 重载白名单
> #白名单 删除 <target> -> 删除白名单成员
> <target> 可以是玩家名/目标选择器/UUID
> ```
> 服务器启动时执行指令 
> - `#启动指令`
> ```
> 启动指令 添加 <名称> <指令> -> 添加启动指令
> #启动指令 列表 -> 查看现有启动指令
> #启动指令 删除 <名称> -> 删除指定启动指令
> #启动指令 开   -> 开启开服指令
> #启动指令 关   -> 关闭开服指令
> #启动指令 执行 -> 执行一遍开服指令
> #启动指令 重载 -> 重载开服指令
> ```
> 触发(包含模式)违禁词自动撤回 
> - `#违禁词`
> ```
> #违禁词 添加 <违禁词> <违禁理由> -> 添加违禁词
> #违禁词 列表 -> 显示违禁词列表及理由
> #违禁词 删除 <违禁词> -> 删除指定违禁词
> #违禁词 开   -> 开启违禁词
> #违禁词 关   -> 关闭违禁词
> #违禁词 重载 -> 重载违禁词
> ```
> 发送关键词（完全匹配模式）自动回复，支持图片 
> - `#关键词`
> ```
> #关键词 开   -> 开启关键词
> #关键词 关   -> 关闭关键词
> #关键词 重载 -> 重载关键词
> > #关键词 列表 -> 显示关键词列表
> #添加 <关键词> <回复> -> 添加关键词
> #删除 <关键词> -> 删除指定关键词
> ```
> 游戏内关键词 
> ```
> #不再提供开关
> ```
> uuid 匹配 游戏ID，如果有时游戏内现实ID不匹配，可以尝试重新匹配一下uuid 
> - `#uuid`
> ```
> #uuid 列表   -> 查看uuid绑定表
> #uuid 重载 -> 重新匹配uuid
> #uuid 更新 <老ID> <新ID> -> 改白名单的名字
> /uuid name 查看白名单名字 #此功能已失去
> ```
> 让机器人昵称显示为在线人数 
> - `#名字`
> ```
> #名字 开 -> 机器人名字显示为在线人数,需要在配置文件内配置服务器公网或IP域名和端口(一直显示会占用少许服务器资源)
> #名字 关 -> 机器人名字为特殊空白名字，如果不支持请关闭此功能，然后你就可以自己给机器人命名了
> ```
> 协助审核（请将问题设置为"你的邀请人？"或"你的邀请人?"）
> - `#审核`
> ```
> #审核 开 -> 开启自动审核
> #审核 关 -> 关闭自动审核
> #审核 添加 <QQ号> <别名> -> 添加审核员的别名(匹配用)
> #审核 删除 <QQ号> -> 删除审核员
> #审核 列表 -> 审核员列表
> ```
> </details>

</details>

#### 群聊部分，请在群内使用

<details>

```
#玩家 -> 获取在线玩家列表
#假人 -> 获取在线假人列表
#服务器 -> 同时获取在线玩家和假人列表
#绑定 <游戏ID> -> 绑定你的游戏ID
#mc <消息> -> 向游戏内发送消息（可以触发游戏内关键词）
#风格 -> 机器人风格帮助
#游戏关键词 列表 -> 显示现有游戏内关键词列表
#删除假人 <假人名字> -> 删除游戏内指定假人

关键词相关：
#添加 <关键词> <回复> -> 添加游戏内关键词回复
#添加图片 <关键词> -> 添加关键词图片
#删除 <关键词> -> 删除关键词
#列表 -> 获取关键词回复列表
```

> <details>
> 
> 机器人回复风格切换 `#风格`
> ```
> #风格 列表   -> 风格列表
> #风格 <风格> -> 切换至指定风格
> ```
> 内置模式：`普通` `傲娇`
> AI生成后内置的模式：`雌小鬼` `御姐` `萝莉` `波奇酱` `病娇` `中二病`
> 
> </details>

</details>

## 管理员
> 配置机器人管理
#### 1. 基础管理员
写在配置文件里的管理员，无论什么情况下都拥有管理员权限
- config.yml
```yml
admin_id:
- 123456
- 234567
```

#### 2.机器人好友管理员
只要有机器人的好友就能拥有管理员权限，请关闭机器人的好友申请功能
- 未来计划中...

#### 3.管理群
在管理群内的人都拥有管理员的权限，离群即失去管理员权限，仅限在群内生效
- config.yml
```yml
admin_group_id:
- 123456
```

## RCON的说明

> 基于指令并获取返回结果，后续可能会取消！

### 配置
#### 作用
1. 获取真实的在线情况
2. 获取添加白名单的反馈数据
#### 服务端配置 - Server
- server.properties
```
rcon.port=12345
enable-rcon=true
rcon.password=123456
```
#### MCDR配置 - MCDR
- config.yml
```
rcon:
  enable: true
  address: 127.0.0.1
  port: 12345
  password: 123456
```

## GUGUbot配置文件
> 非常建议看看

[点击查看配置文件说明](https://github.com/LoosePrince/PF-GUGUBot/blob/main/config_default.yml)
<br></br>

# CoolQAPI配置

> CoolQAPI是前置插件不可忽略

## 说明

### QQ Bot 配置
>配置方法部分源自原始插件说明

推荐使用 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)

#### 使用go-cqhttp
在`account`字段中设置QQ帐号和密码：

```yaml
account:
  uin: 1233456
  password: ''
```

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

> <details>
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
> </details>

### 关于多服使用
> 不支持

### 开发
> 无

# 有BUG或是新的IDEA
如果需要更多联动或提交想法和问题请提交 [issues](https://github.com/LoosePrince/PF-GUGUBot/issues) 或 QQ [1377820366](http://wpa.qq.com/msgrd?v=3&uin=1377820366&site=qq&menu=yes) 提交！ <br />
视情况添加，请勿联系他人（开发者：[雪开](https://github.com/XueK66)）

# TODO
- [ ] 修复功能异常或缺失的问题
- [ ] ~~更多的rcon功能接入~~
- [ ] [#39](https://github.com/LoosePrince/PF-GUGUBot/issues/39)
- [ ] [#45](https://github.com/LoosePrince/PF-GUGUBot/issues/45)

# 使用条款
- 禁止声明为你原创
- 在关键词回复处添加以下关键词

  `插件来源` -> `https://github.com/LoosePrince/PF-GUGUBot`
  
- 禁止商业服使用、盈利等
- 禁止售卖
- 允许二次创作，但请标明来源
