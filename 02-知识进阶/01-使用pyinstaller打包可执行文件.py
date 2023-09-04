import time
print('hello world')
time.sleep(3)


'''
要将其打包为可执行文件，请按照以下步骤操作：

1、安装PyInstaller
pip install pyinstaller

2、打包脚本
pyinstaller hello.py

这将创建一个名为"dist"的目录，并在其中生成可执行文件"hello"。

3、运行可执行文件
./hello
这将运行可执行文件，并输出"Hello, world!"。

请注意，PyInstaller支持许多选项和配置，以便根据您的需要自定义打包过程。例如，您可以指定要包含的文件、要使用的图标、要使用的Python解释器等等。有关更多信息，请参阅PyInstaller文档。
'''