from .auth.crud import auth  # noqa
from .user.crud import user  # noqa


# For a new basic set of CRUD operations you could just do

# from .base.crud import CRUDBase
# from app.data.item.model import Item
# from app.data.item.schemas import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
