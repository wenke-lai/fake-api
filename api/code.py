from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter(prefix="/code", tags=["code"])


@router.get("/ok", status_code=200)
def ok():
    return {"status": 200}


@router.get("/created", status_code=201)
def created():
    return {"status": 201}


@router.get("/no-content", status_code=204)
def no_content():
    return {"status": 204}


@router.get("/move-permanently", response_class=RedirectResponse, status_code=301)
def move_permanently():
    return "/"


@router.get("/found", response_class=RedirectResponse, status_code=302)
def found():
    return "https://example.com"
