
#**使用步骤 ************************** #

1、使用记事本打开config.cfg文件

2、将pdf_folder更改为电脑中存放pdf的文件夹（默认为D:/pdf）

3、将img_folder更改为电脑中存放img的文件夹（默认为D:/img）
    ！！！注意！这个是暂存图片的文件夹，为减少内存占用，每次识别都会先清除文件夹内的图片，如果需要保存图片的话请识别后重命名文件夹！！！！
	
4、将word_folder更改为电脑中存放word的文件夹（默认为D:/word）

5、img_type默认设置为png（效果最好，使用wand可以改为jpg，但是pdfimagines只能png）

6、将word_folder更改为电脑中存放word的文件夹（默认为D:/word）

7、在https://cloud.baidu.com/注册一个百度云BCE账号，然后从控制面板新建一个文字识别应用。获得调用API需要的 AppID，API Key 和 Secret Key。

8、将config.cfg文件中的appId、apiKey、secretKey设置为你的相应数值

9、安装相应的ImageMagick-6.9程序（最好安装在默认位置，32位安装x86，64位安装x64！）

10、解压poppler-0.68.0.zip文件至任意位置，并将其/bin路径添加至环境变量的Path中！！

11、取消cmd快速编辑模式
	！！！取消方法：打开regedit，转到HKEY_CURRENT_USER\Console，将%SystemRoot%_System32（和64）_WindowsPowerShell_v1.0_powershell.exe中的QuickEdit的值从0改成1

12、点击运行ocr_pdf2word.exe，出现“请按任意键继续”即转换完成，可按任意按键或关闭命令行界面退出。





#**推荐选项 ************************** #

 1：识别pdf；
 
 1：表示保留结尾符号和大写开头单词结尾换行;
 
 0：表示不处理。
 
 0：表示不处理。
 
 1：pdfimages;





#**重要提示 ************************** #

1、任何时候长时间卡住，暂时性解决办法是按一下enter键即可，永久性解决请将cmd的属性中，快速编辑模式取消！！！
		取消方法：打开regedit，转到HKEY_CURRENT_USER\Console，将%SystemRoot%_System32（和64）_WindowsPowerShell_v1.0_powershell.exe中的QuickEdit的值从0改成1，完成！

1、pdf转为图片的过程可能出现识别Syntax Error warning，忽略即可

2、可以直接在img文件中存放想要识别的图片，然后选择操作 0：识别图片 可以直接将图片合成为picture.docx的文件

3、百度云账户可能会被判定为恶意用户中止识别，需要验证登陆一下https://cloud.baidu.com/

4、如果图片转换完成了，但是没有转换为doc，很可能是百度云误把请求作为ddos攻击拦截，可以在选择操作中选择“识别图片”，会直接将img中的图片合成为picture.docx的文件，但需要自己更名为pdf文件名！







# 出现闪退 ************************** #

1、请检车路径是否设置正确，存放pdf和word的文件夹是否均已创建，且名称与config文件中对应

2、ImageMagick-6.9程序是否安装且版本正确？

3、poppler是否添加路径？

4、如果图片转换完成了，参考重要提示4！





# @Author: qimeng
# @File  : readme.txt


