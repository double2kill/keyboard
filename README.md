# 项目操作步骤

## 安装依赖
从项目根目录运行以下命令以安装所需的依赖项：
`pip install -r requirements.txt`


## 启动项目

使用以下命令启动FastAPI开发服务器：
`sudo fastapi dev main.py`

`sudo fastapi run main.py`

访问 `http://127.0.0.1:8000` 查看应用。

## 设置不同端口

`sudo uvicorn main:app --port 8877`
