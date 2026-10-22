# astrbot-plugin-jmdownloader

一个用于 [AstrBot](https://github.com/AstrBotDevs/AstrBot) 的 JMComic PDF 下载插件。发送 `/jm <ID>` 后，插件会下载漫画图片、合成有效 PDF，并通过 NapCat/OneBot 作为真正的 QQ 群文件或私聊文件上传。当前版本为 `1.0.6`。

> [!IMPORTANT]
> 使用前必须配置好 NapCat：在 AstrBot 中创建并启用 `OneBot v11`（aiocqhttp）适配器，在 NapCat 的“网络配置”中启用 WebSockets 客户端并连接 `ws://<AstrBot主机>:6199/ws`。请确认 AstrBot 控制台出现“aiocqhttp(OneBot v11) 适配器已连接”，同时确保机器人具有群文件上传权限。

## 功能

- 支持 `/jm 123456` 与 `/jm JM123456`
- 使用 AstrBot 原生命令过滤器，不会把命令交给大模型回答
- 下载完成后校验 PDF 文件头及文件大小
- 通过 `upload_group_file` / `upload_private_file` 上传真实 QQ 文件
- 支持 Cookie、代理、超时、重试和下载并发配置
- 自动清理下载图片、PDF 和过期临时目录
- 下载失败、内容不存在或上传失败时返回明确提示

## 环境要求

- AstrBot `>= 4.27.1, < 5`
- aiocqhttp 平台适配器
- NapCat/OneBot 11
- Python 3.10+

## 安装

在 AstrBot 插件管理页选择“从 GitHub 安装”，填入：

```text
https://github.com/SunflowerYuuka/astrbot-plugin-jmdownloader
```

也可以将仓库克隆到 AstrBot 的 `data/plugins/` 目录：

```bash
git clone https://github.com/SunflowerYuuka/astrbot-plugin-jmdownloader.git
```

安装后重载插件或重启 AstrBot。AstrBot 会根据 `requirements.txt` 安装 `jmcomic` 和 `img2pdf`。

## 使用

### 先配置 NapCat

1. 在 AstrBot WebUI 的“机器人”页面创建 `OneBot v11` 适配器并启用；反向 WebSocket 端口默认为 `6199`。
2. 在 NapCat WebUI 的“网络配置”中新建并启用 WebSockets 客户端。
3. 本机部署时填写 `ws://127.0.0.1:6199/ws`；分离或 Docker 部署时将主机名换成 AstrBot 实际可达地址。
4. 如果 NapCat 配置了 Token，AstrBot 的反向 WebSocket Token 必须保持一致。
5. 在 AstrBot 控制台确认出现“aiocqhttp(OneBot v11) 适配器已连接”。
6. 群聊使用时，确认机器人账号可以上传群文件。

官方接入说明：[AstrBot OneBot v11 / NapCat 配置](https://docs.astrbot.app/platform/aiocqhttp.html)

### 下载命令

```text
/jm 123456
/jm JM123456
```

插件会先发送开始提示，下载并生成 PDF，随后上传 QQ 文件。成功后会显示文件大小。

## 配置

| 配置项 | 默认值 | 说明 |
| --- | ---: | --- |
| `enabled` | `true` | 是否启用插件 |
| `allow_group` | `true` | 是否允许群聊使用 `/jm` |
| `group_access_mode` | `disabled` | 群聊名单模式：`disabled`、`whitelist` 或 `blacklist` |
| `group_whitelist` | `[]` | 白名单群号列表，仅在 `whitelist` 模式生效 |
| `group_blacklist` | `[]` | 黑名单群号列表，仅在 `blacklist` 模式生效 |
| `cookies` | 空 | 可选 Cookie，格式为 `k=v; k2=v2` |
| `proxy` | 空 | 可选 HTTP/HTTPS 代理；留空沿用系统代理 |
| `upload_file_mode` | `base64` | QQ 文件传输方式：`base64`（跨容器推荐）、`file_uri`（共享路径）或 `legacy`（旧版裸路径） |
| `retry_without_title` | `true` | 标题文件名上传失败时，是否自动改用 `JM<ID>.pdf` 重试 |
| `pdf_password_enabled` | `false` | 是否给 PDF 加密；开启后密码为纯数字 JM ID，例如 `1465788` |
| `timeout` | `20` | 单次网络请求超时秒数 |
| `retry_times` | `3` | 请求重试次数 |
| `image_threads` | `16` | 单章节图片下载并发数 |
| `photo_threads` | `4` | 章节下载并发数 |
| `max_concurrent` | `1` | 同时处理的漫画数量 |
| `dir_rule` | `Bd / JM{Aid}-{Atitle}` | jmcomic 下载目录规则 |

## 常见问题

### 机器人只发送“开始下载”

请确认使用的是 `1.0.2` 或更高版本。进度提示必须通过 `event.send` 直接发送，否则 AstrBot 的 `after_message_sent` 可能提前结束命令生成器。

### 群里只出现“📑”而没有 PDF

通用 OneBot `file` 消息段在部分 NapCat 版本中只会显示文件占位符。本插件直接调用 `upload_group_file` 或 `upload_private_file`。若仍失败，请检查机器人是否有群文件上传权限。

默认的 `base64` 模式会通过 OneBot WebSocket 传输文件内容，AstrBot 与 NapCat 位于不同容器时也能工作。旧版 OneBot 可将 `upload_file_mode` 设置为 `legacy`；如果两边共享临时目录，也可以选择 `file_uri`，它会把本地路径转换为 `file:///...` URI。

默认情况下，插件先使用 `JM<ID>-标题.pdf` 上传。如果 QQ 或 NapCat 因文件名中的标题拒绝上传，会自动重试为 `JM<ID>.pdf`。将 `retry_without_title` 关闭后，可以禁用这个兜底行为。

### 一直没有收到文件

先检查 AstrBot 控制台是否显示 OneBot v11 适配器已经连接；然后检查 NapCat 的 WebSockets 客户端地址、启用状态和 Token。默认连接地址为 `ws://<AstrBot主机>:6199/ws`。

### 提示内容不存在或仅登录可见

先确认 ID 正确。对于仅登录可见内容，请在插件配置中填写有效 Cookie。

### JMComic 连接失败

稍后重试，或配置可用代理。建议同时查看 AstrBot 日志中的具体网络异常。

## 说明

本项目仅用于技术学习与个人备份。请遵守所在地法律法规、目标站点规则以及内容版权要求。项目不托管、分发或提供任何漫画内容。

## License

[MIT](LICENSE)
