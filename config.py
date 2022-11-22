#    This file is part of the Compressor distribution.
#    Copyright (c) Binary Tech
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.



from . import *

try:
    APP_ID = config("4348597", cast=int)
    API_HASH = config("e96d78248a6d143dec4dcf76680dcb4e")
    BOT_TOKEN = config("5534857339:AAFOwsCcpnomw6IyMrQKPQC9shcgJC9rHS8")
    OWNER = config("5158302248", default=1322549723, cast=int)
    LOG = config("1001835795023", cast=int)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
