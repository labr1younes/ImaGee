function get_img_src(elementid,outputid) {
    let output = document.getElementById(outputid);
    let tmp = document.getElementById(elementid).src
    output.setAttribute('value',tmp.split('\\').pop().split('/').pop())
  }

  function testing(txt){
    console.log("hello from +++ " + txt)
  }