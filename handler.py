from db import get_db, close_db
import re

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

def query_handler(question):
  print("问题：", question)
  for index, pattern in enumerate(patterns):
    matchObj = re.match(pattern, question)
    if matchObj:
      print("匹配成功 pattern is: ", pattern)
      val = matchObj.group(1)
      query = queries[index]
      # 查询数据库
      db = get_db()
      with db.session(database="neo4j") as session:
        result = session.run(query, val=val)
        rows = result.values('name')
        rows = [row[0] for row in rows]
        print("查询结果：", rows)
      close_db(db)
      return {
        "state": 0,
        "data": rows,
        "msg": "查询成功"
      }
  # 没有匹配的pattern
  print("匹配失败")
  return {
    "state": 1,
    "msg": "查询失败，没有匹配的字符串"
  }

if __name__ == "__main__":
  query_handler('歌曲兰亭序所属的音乐专辑是')
  query_handler('歌曲兰亭序的作词人是')
  query_handler('演唱兰亭序的歌手是')
  query_handler('专辑魔杰座包含的歌曲是')
  query_handler('周杰伦演唱的歌曲有')
  query_handler('方文山作词的歌曲有')
  query_handler('周杰伦合作过的人有')
