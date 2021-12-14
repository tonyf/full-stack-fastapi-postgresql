# Import all the models, so that Base has them before being
# imported by Alembic
from app.data.base.model import Base  # noqa
from app.data.auth.model import Auth  # noqa
from app.data.user.model import User  # noqa
