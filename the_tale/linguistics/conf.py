# coding: utf-8
import datetime

from dext.common.utils.app_settings import app_settings

linguistics_settings = app_settings('LINGUISTICS_SETTINGS',
                                    WORDS_ON_PAGE=25,
                                    TEMPLATES_ON_PAGE=25,
                                    MODERATOR_GROUP_NAME='linguistics moderators group',

                                    LINGUISTICS_MANAGER_UPDATE_DELAY=datetime.timedelta(minutes=1))
