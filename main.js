window.onload = () => {
  var url = "https://y6de2ifmg8.execute-api.ap-northeast-1.amazonaws.com/studying-form-stage/users"
  $.ajax({
    type: 'GET',
    url: url,
    dataType: 'json'
  })
  .done(function(res){
    console.log(res);
    for(let i of res){
      $("#table").append(
        `<tr>
           <td>${i.name}</td>
           <td>${i.score}</td>
         </tr>`
      )
    }
  })
  .fail(function(res){
    console.log("fail");
  })
  $("#btn").on('click', (event) => {
  var name = $("#form-name").val()
  var done = $("#form-done").val()
  var plan = $("#form-plan").val()
  var memo = $("#form-memo").val()
  var today = new Date()
  var date = today.getFullYear() + "-" +  today.getMonth() + 1 + "-" + today.getDate()
    $.ajax({
      type: 'POST',
      url: url,
      data: JSON.stringify({
        name: name,
        date: date,
        text: {
          done: done,
          plan: plan,
          memo: memo,
        }
      }),
      dataType: 'json'
    })
    .done(function(res){
      console.log("success");
    })
    .fail(function(res){
      console.log("fail");
    })
  })
}
