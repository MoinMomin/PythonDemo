from fastapi import FastAPI
app=FastAPI()
@app.get("/")
async def getData():
    return {"moin"}
@app.get("/moin/{name}")
async  def moin(name):
    return {"welcome  "+name}
@app.get("/data")
async  def mas(last : str):
    return {"welcome  " + last}
@app.get("/dataa")
async  def masa(lasts : str):
    return {"welcome  " + lasts}
@app.get("/dataya/{op}")
async  def masks(op :int, lastsw : str):
    return {"welcome  " +" " + op + " " + lastsw}
