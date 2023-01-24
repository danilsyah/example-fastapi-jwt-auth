import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        'app:appFast',
        reload=True,
    )