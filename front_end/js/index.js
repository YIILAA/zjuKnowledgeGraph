$(function () {
  console.log('test')
  // 导航栏切换
  $('.nav-item').on('click', function () {
    console.log('click')
    // navbar
    $(this).children().addClass('active').attr('aria-current', 'page')
    $(this).siblings().children().removeClass('active').removeAttr('aria-current')
    // main对应显示
    let id = $(this).children().attr('data-label')
    $(id).css('display', 'block')
    $(id).siblings().css('display', 'none')
  })
  // 项目介绍
  let intro = ''

  // 图谱问答
  $('#query button').on('click', function (e) {
    console.log('click button')
    // 获取input内容
    let question = $('#question').val()
    console.log(question)
    // 发起ajax请求
    $.ajax({
      type: 'POST',
      url: 'http://127.0.0.1:5001/query',
      data: {
        question
      },
      success: function (res) {
        if (res.state === 0) {
          data = res.data
          msg = res.msg
          $('#answer').text(msg + ' ' + data)
        } else {
          msg = res.msg
          $('#answer').text(msg)
        }
      }
    })
  })
})
