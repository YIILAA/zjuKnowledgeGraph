<template>
  <div class="queryview-container">
    <h1 class="h3 mt-4">图谱问答</h1>
    <hr />
    <div class="mt-4 row justify-content-center">
      <form class="col-10">
        <div class="row mb-3 justify-content-center">
          <label class="col-auto col-form-label" for="inputGroupSelect01">参考模版</label>
          <select class="col-10" id="inputGroupSelect01">
            <option selected>问句模版</option>
            <option v-for="(item, index) in templates" :key="index" value="item.index">
              {{ item }}
            </option>
          </select>
        </div>

        <div class="row mb-3 justify-content-center">
          <label class="col-auto col-form-label" for="question">查询问句</label>
          <input
            type="text"
            class="col-10"
            id="question"
            v-model="query"
            placeholder="请参照模版输入查询问句"
          />
        </div>

        <div class="text-center">
          <button type="button" class="btn btn-primary" @click.prevent="toQuery">查询</button>
        </div>
        <hr />
      </form>
      <div class="col-10">
        <p class="answer" id="answer" :style="{ color: color }">
          {{ queryResult }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      templates: [
        '歌曲兰亭序所属的音乐专辑是？',
        '歌曲兰亭序的作词人是?',
        '演唱兰亭序的歌手是？',
        '专辑魔杰座包含的歌曲是？',
        '周杰伦演唱的歌曲有？',
        '方文山作词的歌曲有？',
        '周杰伦合作过的人有？'
      ],
      query: '',
      queryResult: '',
      color: 'black'
    }
  },
  methods: {
    async sendQuery() {
      const { data: res } = await this.$http.post('/api/query', {
        question: this.query.trim()
      })
      this.queryResult = res.msg
      if (res.state === 0) {
        res.data.forEach((item, index) => {
          index === 0 ? (this.queryResult += '：' + item) : (this.queryResult += '、' + item)
        })
        this.color = 'green'
        return
      }
      this.color = 'red'
    },
    toQuery() {
      let trim = this.query.trim()
      if (!trim) {
        this.queryResult = '查询语句不能为空，请重新输入！'
        this.color = 'red'
        this.query = ''
        return
      }
      this.queryResult = '正在查询...'
      this.color = 'black'
      this.sendQuery()
    }
  }
}
</script>

<style lang="less" scoped>
select {
  color: #666;
}

.answer {
  padding-top: 20px;
  text-align: center;
  font-weight: bold;
}
</style>
