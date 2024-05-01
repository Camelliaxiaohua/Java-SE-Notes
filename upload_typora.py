import os
import subprocess

# 设置Typora文件夹路径
typora_folder = r"E:\Notes"

def upload_typora_to_github():
    # 切换到Typora文件夹
    os.chdir(typora_folder)

    # 添加所有文件到Git仓库
    subprocess.run(["git", "add", "."])

    # 提交更改
    subprocess.run(["git", "commit", "-m", "Update notes"])

    # 修改远程仓库的 URL（使用 SSH URL）
    github_repo_url = "git@github.com:Camelliaxiaohua/Java-SE-Notes.git"
    subprocess.run(["git", "remote", "set-url", "origin", github_repo_url])

    # 推送到GitHub
    subprocess.run(["git", "push", "--force", "origin", "master"])

if __name__ == "__main__":
    upload_typora_to_github()
