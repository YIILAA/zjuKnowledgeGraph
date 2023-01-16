# 知识图谱应用

## 项目介绍

周杰伦（Jay Chou），1979年1月18日出生于台湾省，祖籍福建省福建省泉州市永春县，中国台湾流行乐男歌手、音乐人、演员、导演、编剧，曾获金马奖、金像奖最佳新人奖、金曲奖最佳作曲人奖，连续三年获世界音乐大奖中国区最畅销艺人奖，曾于2003年成为美国《时代周刊》封面人物，2012年登福布斯中国名人榜榜首。周杰伦于2000年发布第一张个人专辑《Jay》正式出道，出道至今已发布27张专辑，300多首歌曲，《七里香》、《听妈妈的话》、《青花瓷》等耳熟能详的歌曲陪伴一代又一代人的青春岁月。

本项目尝试对周杰伦出道以来参与过的所有歌曲作品、专辑以及合作歌手、作词人进行关系分析，将这些信息组织成三元组构建知识图谱，并基于知识图谱实现一个有关周杰伦歌曲的在线检索系统。

首先利用爬虫技术爬取有关周杰伦歌曲信息的文本描述，利用知识图谱抽取工具DeepKE抽取文本描述中的实体和关系，并将这些信息组织成三元组存入.csv格式文件中，然后使用非关系型数据库neo4j搭建知识图谱。随后，我们又用基于python的轻量级后端开发框架flask和前端框架Vue实现了一个基于知识图谱的在线检索系统。

## 技术栈

前端bootstrap, Ajax

- 打算改成使用vue

后端采用python, flask

数据库neo4j

## 运行

### 前端

todo

### 后端

安装python依赖

创建虚拟环境并开启

```
python -m venv neoflix
source ./neoflix/bin/activate
```

Todo:添加requirement文件

```
pip install -r requirements.txt
```

```
$ pip install flask
$ pip install flask-cors
$ pip install neo4j
neo4j-driver
```

开启服务器

```
$ python app.py
```

## 功能

支持的问句模版：

```
===== 匹配：歌曲 =====
1. 歌曲兰亭序所属的音乐专辑是？——魔杰座
pattern='歌曲(.+)所属的音乐专辑是'
2. 歌曲兰亭序的作词人是？——方文山
pattern='歌曲(.+)的作词人是'
3. 演唱兰亭序的歌手是？——周杰伦 
pattern='演唱(.+)的歌手是'

===== 匹配：专辑 =====
1. 专辑魔杰座包含的歌曲是？——展示所有
pattern='专辑(.+)包含的歌曲是'

===== 匹配：人物 =====
1. 周杰伦演唱的歌曲有？——展示10条
pattern='(.+)演唱的歌曲有'
2. 方文山作词的歌曲有？——展示10条
pattern='(.+)作词的歌曲有'
3. 周杰伦合作过的人有？——展示10条
pattern='(.+)合作过的人有'
```

问句模版和对应的数据库查询语句：

```
patterns = [
  '歌曲(.+)所属的音乐专辑是',
  '歌曲(.+)的作词人是',
  '演唱(.+)的歌手是',
  '专辑(.+)包含的歌曲是',
  '(.+)演唱的歌曲有',
  '(.+)作词的歌曲有',
  '(.+)合作过的人有'
]

queries = [
  "MATCH (a:作品{name:$val})-[:所属专辑]->(b:专辑) RETURN b.name AS name",
  "MATCH (a:作品{name:$val})-[:作词]->(b:人物) RETURN b.name AS name",
  "MATCH (a:作品{name:$val})-[:歌手]->(b:人物) RETURN b.name AS name",
  "MATCH (a:专辑{name:$val})<-[:所属专辑]-(b:作品) RETURN b.name AS name",
  "MATCH (a:人物{name:$val})<-[:歌手]-(b:作品) RETURN b.name AS name LIMIT 10",
  "MATCH (a:人物{name:$val})<-[:作词]->(b:作品) RETURN b.name AS name LIMIT 10",
  "MATCH (a:人物{name:$val})-[:合作]->(b:人物) RETURN b.name AS name LIMIT 10"
]
```



