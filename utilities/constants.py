from datetime import datetime
import os
import uuid


def generate_image_upload_prefix(filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    today = datetime.now()
    today_path = today.strftime("%Y/%m/%d/%H/%M/%S")
    return f"PRODUCT/{today_path}{filename}"


"""  These are the user permission types we will use for this project """
PERMISSION_TYPES = (
    ('0', 'Super Admin'),
    ('1', 'Admin'),
    ('2', 'Individual'),
    ('3', 'Guest'),
)

"""  These are the address types I would be using for my country. You can change them to suit your needs  """
ADDRESS_TYPES = (
    ('within_tema', 'Within Tema'),
    ('within_accra', 'Within Accra'),
    ('outside_accra', 'Outside Accra'),
)
