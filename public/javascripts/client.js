function hitme(params) {
    console.log("Sending");
    fetch('/messages/',{
        headers: {
          'Accept':'application/json',
          'Content-Type':'application/json'  
        },
        method:'post',
        body:JSON.stringify({
            is:'alive!'
        })
    })
    console.log("Sended");
}