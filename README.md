# astrbot-plugin-jmdownloader

一个用于 [AstrBot](https://github.com/AstrBotDevs/AstrBot) 的 JMComic PDF 下载插件。发送 `/jm <ID>` 后，插件会下载漫画图片、合成有效 PDF，并通过 NapCat/OneBot 作为真正的 QQ 群文件或私聊文件上传。

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
https://github.com/CLRedfield/astrbot-plugin-jmdownloader
```

也可以将仓库克隆到 AstrBot 的 `data/plugins/` 目录：

```bash
git clone https://github.com/CLRedfield/astrbot-plugin-jmdownloader.git
```

安装后重载插件或重启 AstrBot。AstrBot 会根据 `requirements.txt` 安装 `jmcomic` 和 `img2pdf`。

## 使用

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
| `cookies` | 空 | 可选 Cookie，格式为 `k=v; k2=v2` |
| `proxy` | 空 | 可选 HTTP/HTTPS 代理；留空沿用系统代理 |
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

### 提示内容不存在或仅登录可见

先确认 ID 正确。对于仅登录可见内容，请在插件配置中填写有效 Cookie。

### JMComic 连接失败

稍后重试，或配置可用代理。建议同时查看 AstrBot 日志中的具体网络异常。

## 说明

本项目仅用于技术学习与个人备份。请遵守所在地法律法规、目标站点规则以及内容版权要求。项目不托管、分发或提供任何漫画内容。

## License

[MIT](LICENSE)
