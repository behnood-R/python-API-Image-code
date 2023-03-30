# Gunicorn config created 2023-02-10 12:53:18
bind = ['0.0.0.0:8888']
chdir = "/Users/behnood/source/percipio_test/proxy-server"
workers = 33
threads = 33
keep_alive = 10
timeout = 180
log_file = "-"
worker_class = "gthread"



