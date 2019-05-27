
#!/bin/sh
ERROR_MSG=$(git_pull)
export ERROR_MSG
./monitor.sh
