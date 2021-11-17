import logging
import traceback
# logger = logging.getLogger(__name__)

# #create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')

# # level and the format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning('This is a warning')
# logger.error('This is an error')

# try:
#     a=[1,2,3]
#     val=a[4]
# except:
#     logging.error("The error is %s",traceback.format_exc())

from logging.handlers import RotatingFileHandler
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#roll over after 2KB, and keep backup logs app.log1, app.log2, etc.
handler = RotatingFileHandler('app.log',maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello ,world')