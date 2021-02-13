# git学习笔记

## 创建版本库

```
mkdir learning
cd learning 
pwd
/User/XiaoFang/Desktop/learning
git init
```

learning文件夹中会出现.git隐藏文件，使用ls -ah可以看到

## 把文件添加到版本库

```
git add readme.txt
git commit -m "wrote a rea dme file"
```

-m 后面输入的是本次提交的说明

```
git status
```

git status命令可以让我们时刻掌握仓库当前的状态

```
git diff readme.txt
```

顾名思义就是查看difference，显示的格式正是Unix通用的diff格式

```
git log
git log --pretty==oneline
git relog
```

命令显示从最近到最远的提交日志,如果输出信息太多，看的眼花缭乱的，可以试试下面命令

```
git reset --hard HEAD^
git reset --hard [commit_id]
```

工作区和暂存区 清晰描述了add commit时的状态

```
git diff HEAD -- readme.txt
```

命令可以查看工作区和版本库里面最新版本的区别

```
git checkout -- readme.txt  可以丢弃工作区的修改
git reset HEAD	readme.txt	可以把暂存区的修改撤销掉
```

 ```
git rm test.txt
git commit -m "remove test.txt"
 ```

删除操作

## 远程仓库

### 添加远程仓库

第一步：创建SSH Key。id_rsa和id_rsa.pub

```
ssh-keygen -t rsa -C "youtemail@example.com"
```

第二步：登录GitHub，打开"Account settings","SSH Keys"页面，点"Add SSH Key"，填上任意Title，在Key文本框里粘贴id_rsa.pub文件的内容

GitHub告诉我们，可以从这个仓库克隆出新的仓库，也可以把一个已有的本地仓库与之关联，然后，把本地仓库的内容推送到GitHub仓库。

```
git remote add origin git@github.com:gqxiaofang/learngit.git
```

远程库的名字就是origin,这就是Git默认的叫法，也可以改成别的，但是origin这个名字一看就知道是远程库。

```
git push -u origin master
git push origin master
```

远程库是空的,第一次推送master，加上-u参数

### 从远程库克隆

```
git clone git@github.com:michaelliao/gitskills.git
```

## 分支管理

#### 创建dev分支

```
git checkout -b dev 创建并切换
git branch dev      创建
git checkout dev    切换
git branch		 	列出所有分支
git checkout master 切换至master
git merge dev		合并dev的工作成果到master分支上
git branch -d dev	删除分支

git switch -c dev
git switch master
```



