import git

def pull_remote_repo(remote_url, local_path):
    try:
        # 打开本地仓库
        repo = git.Repo(local_path)

        # 添加远程仓库
        origin = repo.remote(name='origin')

        # 拉取远程仓库的内容，但不覆盖本地仓库已有的文件
        origin.fetch()
        origin.pull()

        print("成功拉取远程仓库内容到本地仓库")
    except git.exc.GitCommandError as e:
        print("拉取远程仓库内容失败:", e)

if __name__ == "__main__":
    remote_url = "git@github.com:camelliaxiaohua/Java-SE-Notes.git"  # 修改为你的GitHub仓库SSH URL
    local_path = "E:\\Notes"  # 修改为你本地的仓库路径
    
    pull_remote_repo(remote_url, local_path)
