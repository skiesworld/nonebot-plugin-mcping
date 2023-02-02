# nonebot-plugin-mcping

基于NoneBot的查询MineCraft服务器状态并返回图片的插件

## 安装

- 脚手架安装
    ```shell
    pip install nonebot-plugin-mcping
    ```
  在nb项目文件中添加插件
- NB商店安装
  ```shell
  nb plugin install nonebot-plugin-mcping
  ```

## 命令

默认查询 `25565`端口，如需指定端口只需要加上 `:port`，如：`jes mc.server.com:1234`

- 查询 `Java` 服务器状态
  ```
  jes mc.server.com
  ```

- 查询 `BE` 服务器状态
  ```
  bes mc.server.com
  ```

# 特别感谢

- [NoneBot2](https://github.com/nonebot/nonebot2)： 插件使用的开发框架。
- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)： 稳定完善的 CQHTTP 实现。

## 许可证

本项目使用 [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) 作为开源许可证。
