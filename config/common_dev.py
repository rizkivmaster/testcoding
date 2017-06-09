import services
from config import scheduling

config = {
    "host_url": "127.0.0.1:29000",
    "database_url": "sqlite:////home/rrangkuti/web/shopee/shopee/memory",
    "thread_size": 3,
    'scheduling': scheduling.config,
    'is_maintenance': False,
    'start_bank_fetcher':True,
    'image_url_config':'http://127.0.0.1:29000/',
    'token_notify_interval':10,
    'general_path':'/home/rrangkuti/web/shopee/shopee/',
    'busy_api_ttl_msec':500,
    'services':services.dev.config,
    'enable_modem':False
}
