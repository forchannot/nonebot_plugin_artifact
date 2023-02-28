# [genshin_artifact](https://github.com/forchannot/genshin_artifact)
来自[Genshin_Impact_bot](https://github.com/H-K-Y/Genshin_Impact_bot)的圣遗物插件，因原作者最近没适配了，自行适配了下3.0(以后)圣遗物，适用于nonebot2，以后视情况持续适配
<!-- TOC -->
* [目录](#genshinartifact)
  * [简介](#简介)
  * [许可](#许可)
  * [安装方法](#安装方法)
  * [安装依赖](#安装依赖)
  * [插件命令](#插件命令)
  * [常见问题](#常见问题)
<!-- TOC -->
## 简介

这个插件帮助群员在QQ群内进行圣遗物刷取，强化，圣遗物评分等功能，目前已适配3.3最新圣遗物

## 许可

[GPL-3.0](https://github.com/forchannot/genshin_artifact/blob/main/LICENSE)

## 安装方法

打开你nonebot根目录的pyproject.toml文件，找到下列代码中`plugin_dirs =`一项，将本项目git clone(或者直接Download Zip并解压)到该代码指示的目录去，推荐使用git clone

```
[tool.nonebot]
plugins = []
plugin_dirs = ["src/plugins"]
```
## 安装依赖

进入你的机器人所在的虚拟环境，到本项目根目录执行`pip install -r requirements.txt`


## 插件命令
| 命令概述   | 使用方法              |
|--------|-------------------|
| 查看原神副本 | 原神副本              |
| 刷副本    | 刷副本 副本名 浓缩(可选)    |
| 圣遗物评分  | 圣遗物评分(带图)，目前不可用   |
| 转换狗粮   | 转换狗粮 序号           |
| 查看体力值  | 查看体力值             |
| 转换圣遗物  | 转换全部0级圣遗物         |
| 氪体力    | 氪体力 数量 @(数量和@都可选) |
| 强化圣遗物  | 强化圣遗物X级 序号        |
| 查看圣遗物  | 查看圣遗物仓库           |

## 插件配置项
在全局配置文件.env.prod中添加如下

`use_pic=False/True`
True为开启原神副本图片发送,False为关闭,默认为False

## 常见问题
Q:启动报错有关`nonebot_plugin_htmlrender`

A：在你的机器人的`bot.py`文件中`nonebot.load_from_toml("pyproject.toml")`上面增加一行`nonebot.load_plugin("nonebot_plugin_htmlrender")`，使得`nonebot_plugin_htmlrender`先于本插件启动

Q:No module named xxx

A:安装依赖到你的机器人虚拟环境中，见[安装依赖](#安装依赖)