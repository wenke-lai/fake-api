from fastapi import APIRouter, HTTPException
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


@router.get("/bad-request")
def bad_request():
    raise HTTPException(400, detail="Bad Request")


@router.get("/unauthorized")
def unauthorized():
    raise HTTPException(401, detail="Unauthorized")


@router.get("/payment-required")
def payment_required():
    raise HTTPException(402, detail="Payment Required")


@router.get("/forbidden")
def forbidden():
    raise HTTPException(403, detail="Forbidden")


@router.get("/not-found")
def not_found():
    raise HTTPException(404, detail="Not Found")


@router.get("/method-not-allowed")
def method_not_allowed():
    raise HTTPException(405, detail="Method Not Allowed")


@router.get("/conflict")
def conflict():
    raise HTTPException(409, detail="Conflict")


@router.get("/too-many-requests")
def too_many_requests():
    raise HTTPException(429, detail="Too Many Requests")


@router.get("/internal-server-error")
def internal_server_error():
    raise HTTPException(500, detail="Internal Server Error")


@router.get("/bad-gateway")
def bad_gateway():
    raise HTTPException(502, detail="Bad Gateway")


@router.get("/service-unavailable")
def service_unavailable():
    raise HTTPException(503, detail="Service Unavailable")


@router.get("/gateway-timeout")
def gateway_timeout():
    raise HTTPException(504, detail="Gateway Timeout")
