import os

from config import common_dev

# temporarily use hardcoded config
global common_config
common_config = common_dev.config

def is_dev():
    return True


def get_database_url():
    """
    :rtype
    :return:
    """
    return common_config['database_url']


def get_host_url():
    return common_config['services']['bws']['url']


def get_thread_size():
    """
    :rtype int
    :return:
    """
    return common_config['thread_size']


def get_telegram_token():
    return common_config['telegram_config']['token']


def get_telegram_webhook_endpoint():
    return common_config['telegram_config']['webhook_endpoint']


def get_mandiri_username():
    return common_config['banking']['mandiri']['username']


def get_mandiri_password():
    return common_config['banking']['mandiri']['password']


def get_mandiri_max_retry_time():
    return common_config['banking']['mandiri']['max_retry_time']


def get_mandiri_max_refresh_time():
    return common_config['banking']['mandiri']['max_refresh_time']


def get_bca_max_refresh_time():
    return 10


def get_bni_max_refresh_time():
    return 10


def get_mandiri_account_number():
    return common_config['banking']['mandiri']['account_number']


def get_transaction_refresh_time():
    return common_config['scheduling']['transaction_refresh_time']


def get_maintenance_status():
    return common_config['is_maintenance']


def start_bank_fetcher():
    return common_config['start_bank_fetcher']


def get_image_prefix():
    return common_config['image_url_config']


def get_token_reminder_interval():
    return common_config['token_notify_interval']


def get_general_path():
    return common_config['general_path']


def get_general_log_path():
    return common_config['general_path'] + 'log/'


def get_cs_username():
    return common_config['cs_username']


def get_api_busy_ttl_msec():
    return common_config['busy_api_ttl_msec']


def get_chromedriver_path():
    return common_config['chromedriver_path']


def get_minimum_payment():
    return common_config['payment']['minimum_payment']


def get_receiving_charge():
    return common_config['payment']['receiving_charge']


def get_admin_id():
    return common_config['admin_chat_id']


def get_bte_url():
    return common_config['services']['bte']['url']


def get_bcp_url():
    return common_config['services']['bcp']['url']


def enable_modem():
    return common_config['enable_modem']


def get_line_api_token():
    return common_config['line_config']['token']


def get_line_channel_secret():
    return common_config['line_config']['secret']

def get_line_webhook_endpoint():
    return common_config['line_config']['webhook_endpoint']