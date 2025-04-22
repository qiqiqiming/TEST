# Hello World API

这是一个简单的Hello World API，使用Flask框架开发。

## 功能特点

- 返回Hello World消息
- 健康检查接口

## API端点

- `GET /` - 返回Hello World消息
- `GET /health` - 健康检查

## 本地开发

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行应用：
```bash
python app.py
```

3. 访问API：
- 本地地址：http://localhost:5000

## 部署到Railway

1. 在Railway上创建新项目
2. 连接GitHub仓库
3. 部署应用

## 示例请求

### 获取Hello World消息
```bash
curl http://localhost:5000/
```

### 健康检查
```bash
curl http://localhost:5000/health
``` 