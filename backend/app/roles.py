from fastapi import Depends, HTTPException, status

from app.auth import get_current_user
from app.models.user import User


def require_admin(user: User = Depends(get_current_user)) -> User:
    # 令牌有效但角色不足 → 403（401 仅用于缺失/无效/过期令牌）
    if user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="需要场长权限",
        )
    return user
