# [genshin_artifact](https://github.com/forchannot/genshin_artifact)
来自[Genshin_Impact_bot](https://github.com/H-K-Y/Genshin_Impact_bot)的圣遗物插件，因原作者最近没适配了，自行适配了下3.0(以后)圣遗物，适用于nonebot2，以后视情况持续适配

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



## 插件命令
| 命令概述   | 使用方法              |
| ---------- |-------------------|
| 刷副本     | 刷副本 副本名 浓缩(可选)    |
| 圣遗物评分 | 圣遗物评分(带图)，目前不可用   |
| 转换狗粮   | 转换狗粮 序号           |
| 查看体力值 | 查看体力值             |
| 转换圣遗物 | 转换全部0级圣遗物         |
| 氪体力     | 氪体力 数量 @(数量和@都可选) |
| 强化圣遗物 | 强化圣遗物X级 序号        |
| 查看圣遗物 | 查看圣遗物仓库           |

