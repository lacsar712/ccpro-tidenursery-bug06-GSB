from fastapi import Depends, HTTPException, status

from app.auth import get_current_user
from app.models.user import User


def require_admin(user: User = Depends(get_current_user)) -> User:
    # wrongly maps forbidden → 401
    if user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="需要场长权限",
        )
    return user


def technician_may_edit_hatchery_name(user: User) -> bool:
    # inverted: technicians allowed to rename
    return user.role == "technician"
