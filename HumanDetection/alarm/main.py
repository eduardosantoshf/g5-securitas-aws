# @Author: Rafael Direito
# @Date:   2022-10-06 10:54:18 (WEST)
# @Email:  rdireito@av.it.pt
# @Copyright: Insituto de Telecomunicações - Aveiro, Aveiro, Portugal
# @Last Modified by:   Rafael Direito
# @Last Modified time: 2022-10-06 11:19:15

import os
from alarm import Alarm
from dotenv import load_dotenv
load_dotenv()

# ALARM VARIABLES
ALARM_ID = 1

# AMQP Variables
RABBIT_MQ_USERNAME = os.environ['RABBIT_MQ_USERNAME']
RABBIT_MQ_PASSWORD = os.environ['RABBIT_MQ_PASSWORD']
RABBIT_MQ_URL = os.environ['RABBIT_MQ_URL']
RABBIT_MQ_EXCHANGE_NAME = "human-detection-exchange"    #?
RABBIT_MQ_QUEUE_NAME = "human-detection-queue"          #?
INTRUSION_MANAGEMENT_API_URL = os.environ['INTRUSION_MANAGEMENT_API_URL']

alarm = Alarm(
    alarm_id=ALARM_ID,
    )

alarm.attach_to_message_broker(
    broker_url=RABBIT_MQ_URL,
    broker_username=RABBIT_MQ_USERNAME,
    broker_password=RABBIT_MQ_PASSWORD,
    exchange_name=RABBIT_MQ_EXCHANGE_NAME,
    queue_name=RABBIT_MQ_QUEUE_NAME
    )

alarm.listen_to_notifications()

