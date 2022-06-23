from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level='info', reload=True)


"""
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjU2NTkxNDQyLCJpYXQiOjE2NTU5ODY2NDIsInN1YiI6IjEifQ.Ez6BNcflgBWxjOgUD8_Q2BvqopsZdR6nkGYVBTI_Jpw
Tipo: bearer

"""
