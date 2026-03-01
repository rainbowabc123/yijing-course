# 易经课程网站

基于 MkDocs Material 主题的易经课程网站，包含4门课程共68讲内容。

## 课程列表

1. **易经个人成长课**（17讲）- 密码：756456
2. **易经判断力课**（18讲）- 密码：564826
3. **易经关系婚姻课**（18讲）- 密码：564823
4. **易经风水实用课**（15讲）- 密码：562864

## 本地开发

```bash
# 安装依赖
pip install -r requirements.txt

# 本地预览
mkdocs serve

# 构建网站
mkdocs build
```

## 部署到 Cloudflare Pages

### 1. 推送代码到 GitHub

```bash
git push origin master
```

### 2. 在 Cloudflare Pages 创建项目

1. 访问 [Cloudflare Pages](https://pages.cloudflare.com/)
2. 登录你的 Cloudflare 账号
3. 点击 "Create a project"
4. 选择 "Connect to Git"
5. 授权并选择 GitHub 仓库：`rainbowabc123/yijing-course`

### 3. 配置构建设置

在 Cloudflare Pages 的构建配置页面：

- **Framework preset**: 选择 "None"
- **Build command**: `pip install -r requirements.txt && mkdocs build`
- **Build output directory**: `site`
- **Root directory**: `/`（留空或填 `/`）

### 4. 环境变量（可选）

如果需要，可以添加环境变量：
- `PYTHON_VERSION`: `3.11`

### 5. 部署

点击 "Save and Deploy"，Cloudflare Pages 会自动：
1. 从 GitHub 拉取代码
2. 安装依赖
3. 运行构建命令
4. 部署到 CDN

部署完成后，你会获得一个 `.pages.dev` 域名，可以绑定自定义域名。

## 功能特性

- ✅ 课程密码保护（每门课独立密码）
- ✅ 密码记忆功能（session storage）
- ✅ 响应式设计
- ✅ 中文搜索支持
- ✅ 自定义首页样式
- ✅ 侧边栏导航

## 技术栈

- MkDocs
- Material for MkDocs
- mkdocs-encryptcontent-plugin
