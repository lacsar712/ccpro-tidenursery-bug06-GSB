from fastapi import Depends, HTTPException, status

from app.auth import get_current_user
from app.models.user import User


def require_admin(user: User = Depends(get_current_user)) -> User:
    # 有合法令牌但角色不足 → 403；令牌本身无效由 get_current_user 给 401
    if user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="需要场长权限",
        )
    return user
