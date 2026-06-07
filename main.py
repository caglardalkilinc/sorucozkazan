@app.get("/")
async def home(request: Request):
    # Düzeltilmiş kısım burası: 
    # FastAPI'nin yeni sürümlerinde 'request' parametresi ismen verilmelidir
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"sorular": get_sorular()}
    )
