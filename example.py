# -*- coding: utf-8 -*-

#Made By KazmiLineBot
#Api -- KazumiLine.py

import KazumiLine as Line
import time 


client = Line.LINE("將你的TOKEN置於此/PUT YOUR TOKEN HERE", "登入裝置/LoginType(Chrome, IOS.....)")
print('{} 登入成功 '.format(client.getProfile().displayName))
"""EXAMPLE"""

while 1:
    try:
        operations = client.fetchOperations(client.revision, 50)     #-----Do Not Remove This Line Or You Might Get Error
        if operations is not None:
            for op in operations:
                if op.type == 0:   #-----None
                    pass
                elif op.type in [25,26]:    #-----Recieve Message or Send Message
                    msg = op.message
                    text ,msg_id ,receiver, sender = msg.text ,msg.id ,msg.to ,msg._from
                    if msg.toType == 0:
                        if sender != client.getProfile().mid: to = sender    #-----You Can Not Send To Your Self
                        else: to = receiver
                    else: to = receiver
                    if text is None:
                        pass
                    if text.lower() == 'speed':
                        start = time.time()
                        client.sendMessage(to, "test speed...")
                        client.sendMessage(to,str(time.time() - start))
                    elif text.lower() == 'test':
                        client.kickoutFromGroup(to,['oo'])
                client.revision = max(op.revision, client.revision)    #-----Update Your OpRevision
    except Exception as e:
        pass
        if e.code != 0:
            print(e)

