# Changelog

## 1.0.5 - 2026-10-22

- 增加 Base64 文件传输模式，支持 AstrBot 与 NapCat 不共享临时目录的部署方式。
- 将 WebUI 中的文件传输方式改为下拉选项。
- 保留 `file_uri` 和 `legacy` 兼容模式。

## 1.0.4 - 2026-10-22

- 默认使用 `file:///...` URI 上传 QQ 文件，兼容 NapCat 对本地文件参数的解析。
- 增加 `upload_file_mode` 配置，可切换 `file_uri` 和旧版 `legacy` 上传格式。

## 1.0.3 - 2026-08-10

- 补充 AstrBot 插件市场所需的仓库与作者元数据。
- 在市场简介和 README 中明确 NapCat OneBot 反向 WebSocket 配置要求。
- 增加群文件上传权限与连接状态排查说明。

## 1.0.2 - 2026-08-10

- 使用 `event.send` 发送下载进度，避免 AstrBot 提前结束命令处理器。
- 通过 NapCat 的 `upload_group_file` / `upload_private_file` 上传真实 QQ 文件。
- 增加 PDF 文件头与文件大小校验。
- 增加下载队列、错误提示、临时目录清理、代理及 Cookie 配置。
