import os
import sys
import subprocess

print('这是一个测试的脚本，谨慎使用')

folder=input('输入需要转码的目录: ')
folder=folder.replace('\\', '/')
while not os.path.exists(folder) or not os.path.isdir(folder):
    folder=input('路径不存在, 重新输入:')

fileList=[]
allFiles=os.listdir(folder)
for item in allFiles:
    if item.endswith('.mkv') or item.endswith('.mp4') or item.endswith('.flv'):
        fileList.append(item)

if(len(fileList)==0):
    print('这个目录下没有任何媒体')
    sys.exit(1)
print('搜索到的媒体文件列表如下')
for item in fileList:
    print(item)
output=input('输出的目录: ')
while not os.path.exists(output) or not os.path.isdir(output):
    output=input('路径不存在, 重新输入:')
output=output.replace('\\', '/')
scale='1280x720'    # 你可以在这里修改视频尺寸
encoder='libx264'   # 你可以在这里修改视频编码
for item in fileList:
    cmd=f'''ffmpeg -i "{item}" -c:v {encoder} -s {scale} "{output}/{item}"'''
    print(f"正在执行: {item}")
    print(f"命令: {cmd}")
    subprocess.run(cmd, cwd=folder, shell=True)

item=fileList[0]

print('执行完成')

# e:\视频\TV动画\白圣女与黑牧师
# d:\导出