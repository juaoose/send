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
                id: 1337
            })
        })
    }
    console.log("Sended");
}
