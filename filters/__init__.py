from loader import dp
from .admin import IsAdmin
from .group_filtr import IsGroup
from .private_chat import IsPrivate
from .raqam import Kod

if __name__ == 'filters':
    dp.filters_factory.bind(Kod)
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsGroup)
