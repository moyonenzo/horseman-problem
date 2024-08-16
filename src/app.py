from time import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.utils.chessboard import Chessboard, PathItem

app = FastAPI(title="HorsemanProblem - API", version="0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=[""],
)


class SolveHorsemanProblemResponse(BaseModel):
    path: list[PathItem]
    time: float


@app.get("/")
async def root() -> None:
    pass


@app.get("/solve")
async def solve(size: int, x: int, y: int) -> SolveHorsemanProblemResponse:
    chessboard = Chessboard(size=size)
    start = time()
    path = chessboard.solve(x, y)
    return SolveHorsemanProblemResponse(path=path, time=time() - start)
