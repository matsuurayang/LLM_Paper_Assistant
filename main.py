from fastapi import FastAPI
from routers import paper, summary, qa

app = FastAPI(title="论文阅读与总结助手 API", version="1.0")

# 挂载路由
app.include_router(paper.router, prefix="/api/paper", tags=["Paper Upload"])
app.include_router(summary.router, prefix="/api/paper", tags=["Paper Summary"])
app.include_router(qa.router, prefix="/api/paper", tags=["Paper QA"])

@app.get("/")
def read_root():
    return {"message": "Welcome to LLM Paper Assistant API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
