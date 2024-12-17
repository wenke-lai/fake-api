from fastapi import APIRouter

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
