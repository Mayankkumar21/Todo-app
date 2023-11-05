const express = require('express')
const { todo } = require('node:test')
const cors = require('cors');
const app = express()
const port = 3000
app.use(cors());
app.use(express.json());


app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

app.get("/",(req,res)=>{
    res.sendFile("/Users/mayankkumar/Desktop/prac/index.html");
})
app.post("/add",(req,res)=>{
    var title=req.body.title;
    var desc=req.body.description

    const todo_obj={
        "Title":title,
        "Description":desc
    }
    res.status(201).json(todo_obj)
})
app.get("/display",(req,res)=>{
    const obj={
        "Todo_id":"7",
        "Task":"Go to gym man please"
    }
    res.status(201).json(obj)
})