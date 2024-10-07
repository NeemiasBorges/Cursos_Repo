from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession


from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL, echo=True)

Session: AsyncSession = sessionmaker(
      autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)