from datas_history import load_database, save_database
from transaction import transaction_history_service

database = load_database()
save_database(database)
transaction_history_service(database, user_name="user01")


"""
    History hissəsində history.json faylı doldurulmalı , cari istifadəçinin username-i main.py kodundakı user_name hissəsinə yazılmalıdır.
history.json faylında yeni tarixçə əlavə edən zaman hər fərqli əməliyyat tarixçəsi vergüllə, içərisindəki elementlər isə (məsələn: Recipient , Type) "/" işarəsi ilə ayrıllamlıdır.

"""