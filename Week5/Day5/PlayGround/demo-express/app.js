const express = require("express");
const app = express()

app.listen(5000, ()=>{
    console.log("Listening on localhost in port 5000");
})


app.get("/", (req, res)=>{
    // console.log("request is:", req);
    // if (req.url === '/')
    //     res.end("Wa Drab L7labaln a wlaydi");
    res.json([
        { name: 'iPhone', price: 800 },
        { name: 'iPad', price: 650 },
        { name: 'iWatch', price: 750 }
    ])
})


app.get("/users/:userName", (req, res)=>{
    console.log(req.params);
    res.send(req.params.userName);
})