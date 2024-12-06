# routes/__init__.py
from .users import router as users_router
# from .movies import router as movies_router
# from .favorites import router as favorites_router
import logging

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("routes")

logger.info("Routes package initialized.")
# Экспортируем маршруты, чтобы их можно было импортировать через routes
__all__ = ["users_router"]
