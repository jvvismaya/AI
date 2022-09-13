from fastapi import FastAPI
app = FastAPI()
@app.get('/hello')
def hello():
    return 'Welcome'
if __name__ == '__main__':
    app.run()