# Ilhabela

```

1、进程间通信
pool 需要manager中的queue
多进程中的queue 是不能进行通信的

可以使用pipe 进行进程间的通信,只适用于两个进程间的通信

也可以使用共享内存的方式实现  Manager.dict()

```