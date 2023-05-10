$(function(){
    $("button").click(function(){
      alert( ($("#ps-type").val() || []).join(', ')  );
    })
  });