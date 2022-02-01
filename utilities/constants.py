from datetime import datetime
import os
import uuid


def generate_image_upload_prefix():
    return uuid.uuid4().hex


TODAY = datetime.now()
TODAY_PATH = TODAY.strftime("%Y/%m/%d/%H/%M/%S")
PROFILE_PIC_DIR = 'PROFILE/' + TODAY_PATH + generate_image_upload_prefix() + '/'
WALLPOST_PIC_DIR = 'WALLPOST/' + TODAY_PATH + generate_image_upload_prefix() + '/'


"""  These are the user permission types we will use for this project """
PERMISSION_TYPES = (
    ('0', 'Super Admin'),
    ('1', 'Admin'),
    ('2', 'Individual'),
    ('3', 'Organization'),
    ('4', 'Guest'),
)

"""  These are the address types I would be using for my country. You can change them to suit your needs  """
ADDRESS_TYPES = (
    ('within_tema', 'Within Tema'),
    ('within_accra', 'Within Accra'),
    ('outside_accra', 'Outside Accra'),
)
