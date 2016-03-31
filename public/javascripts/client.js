function hitme(color) {
    console.log("Sending");
    fetch('/messages/',{
        headers: {
          'Accept':'application/json',
          'Content-Type':'application/json'  
        },
        method:'post',
        body:JSON.stringify({
            color:color,
            id: Math.floor(Math.random() * 100)
        })
    })
    console.log("Sended");
}