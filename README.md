# ChatYuan-webui

基于chatyuan AI对话模型的简单WEBUI

需要python3.10，CUDA版pytoch和SentencePiece、pywebio。

安装方法：首先安装python，并添加到path。之后去pytorch.org依据自己的cuda版本安装对应的pytoch。随后在python中安装SentencePiece、pywebi两个库。之后，去https://huggingface.co/ClueAI/ChatYuan-large-v1 下载模型文件（pytorch_model.bin）文件放入ChatYuan-large-v1。最后运行start-webui.bat。等待后，在浏览器里打开控制台里的URL即可使用


由于作者技术局限，目前只能完成单轮对话。

![202302121257.PNG](https://s2.loli.net/2023/02/12/Tt3R2nNWk65DVUC.png)
