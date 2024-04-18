# 导入【Monkey Patch】, 在应用程序所有导入之前. 在不改变原有代码的情况下, 将任何可能执行阻塞操作的调用转换成异步调用.
from gevent import monkey
monkey.patch_all()

import multiprocessing

# 设置服务进程数
workers = multiprocessing.cpu_count() * 2 + 1
# 设置线程数
threads = multiprocessing.cpu_count() * 2
# 设置监听端口
bind = '0.0.0.0:8080'
# 设置守护进程, 使用Docker时无需设置
daemon = True
# 设置Worker模式
worker_class = 'gevent'
# 设置最大并发量
worker_connections = 2000
# 设置进程文件目录
pidfile = '/var/run/gunicorn.pid'
# 设置访问日志和错误信息日志路径
accesslog = './log/gunicorn_access.log'
errorlog = './log/gunicorn_error.log'
# 设置日志记录水平
loglevel = 'debug'
