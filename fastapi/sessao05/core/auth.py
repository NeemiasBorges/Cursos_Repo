from pytz import timezone

from typing import Optional,List 
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from jose import JWTError, jwt

from core.configs import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")