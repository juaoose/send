function hitme(color) {
    console.log("Sending");
    for (i = 0; i < 20; i++) {
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
    }
    console.log("Sended");
}
