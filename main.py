import asyncio
import logging

import aioamqp

from Monitor import Monitor
from SimpleStrategy import SimpleStrategy

demo_strat=SimpleStrategy(None,5.0,Monitor())

async def callback(channel, body, envelope, properties):
    demo_strat.strategy(body)

async def connect():
    try:
        transport, protocol = await aioamqp.connect()  # use default parameters
    except aioamqp.AmqpClosedConnection:
        print("closed connections")
        return

    print("connected !")
    channel=await protocol.channel()
    exchange_name="timealign"
    routing_key='ticker'
    queue_name=exchange_name+"."+routing_key
    await channel.exchange_declare(exchange_name=exchange_name, type_name='topic')
    await channel.queue_declare(queue_name,auto_delete=True)
    await channel.queue_bind(queue_name,exchange_name,routing_key)
    while True:
        await channel.basic_consume(callback, queue_name=queue_name)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(connect())