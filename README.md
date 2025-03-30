# LiveNovel

使用 Python 3，利用 OpenAI SDK 和 DeepSeek V3 API 搭建的 TUI 互动小说工具。

## 使用教程

```sh
git clone https://github.com/originalFactor/liveNovel.git
cd liveNovel
pip3 install -r requirements.txt
echo 'OPENAI_API_KEY=sk-xxx' > .env # 将 sk-xxx 替换为你的 DeepSeek API Key
```

然后你需要创建一个`history.txt`文件，填入主角、世界观、开局等基础信息。

示例可以在`templates`目录中找到。

然后执行这个命令即可：
```sh
python3 main.py
```

按`Ctrl+C`可以退出，历史记录将自动保存到`history.txt`。

可以尝试修改`system.txt`中的系统提示词以达到更好的效果;)

