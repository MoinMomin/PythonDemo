from fastapi import FastAPI
app=FastAPI()
@app.get("/")
async def getData():
    return {"moin"}
@app.get("/moin/{name}")
async  def moin(name):
    return {"welcome  "+name}
@app.get("/data")
async  def moins(lastName :str | None=None):
    return {"welcome  "+lastName}
