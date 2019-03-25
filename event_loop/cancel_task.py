# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/25 下午9:43
"""

import asyncio


async def consume():
    print('start consume...')
    await  asyncio.sleep(10)
    print('end consume...')


if __name__ == '__main__':
    tasks = [consume() for i in range(10)]

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all = asyncio.Task.all_tasks()
        for t in all:
            print('cancel task')
            print(t.cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()

"""
lishulongdeMBP:event_loop lishulong$ python cancel_task.py 
start consume...
start consume...
start consume...
start consume...
start consume...
start consume...
start consume...
start consume...
start consume...
start consume...
^Ccancel task
True
cancel task
True
cancel task
True
cancel task
True
cancel task
True
cancel task
True
cancel task
True
cancel task
True
cancel task
True
cancel task
True
cancel task
True
lishulongdeMBP:event_loop lishulong$ 

"""
