import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "src.infrastructure.api.doctor_api:app",
        host="0.0.0.0",
        port=8002,
        reload=True
    )
