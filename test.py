import sysv_ipc as svi
import pdb



#mq = svi.MessageQueue(99, svi.IPC_CREX)
mq = svi.MessageQueue(None, svi.IPC_CREX)

#sem = svi.Semaphore(99, 0, 0600, 1)
#sem = svi.Semaphore(None, svi.IPC_CREAT|svi.IPC_EXCL, 0600, 1)
#sem = svi.Semaphore(99, svi.IPC_CREAT)

#mem = svi.SharedMemory(99, svi.IPC_CREAT|svi.IPC_EXCL, 0600, size=20)
#mem = svi.SharedMemory(99, svi.IPC_CREX, 0600)

# 
# value = sem.value
# 
# while value == sem.value:
#     value += 1
#     sem.release()
#     
#     print sem.value
# 
# 

#mem.read(offset=-1)


#mem = mem

#pdb.set_trace()

#mq.send("iahsdgl", type=42)

pdb.set_trace()
# 
# print mq.receive()

#mem2 = svi.SharedMemory(99)

#print mem2.size

# mem=mem
# 
# mem.detach()
# mem.remove()

i = 42

# sem = sem
# sem.remove()


mq.remove()
