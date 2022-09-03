const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  res.cookie("auth", "allowed");
  res.send("Hello World!");
});

app.post("/", (req, res) => {
  var cookie = req.headers.cookie;
  console.log(cookie);

  res.send();
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
