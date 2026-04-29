#!/bin/bash
# Docker Bench Security audit script
echo "=== Docker Bench Security Audit ==="
echo "Start time: $(date)"
echo "===================================="

# Запуск Docker Bench Security
docker run -it --net host --pid host --userns host \
  --cap-add audit_control \
  -e DOCKER_CONTENT_TRUST=$DOCKER_CONTENT_TRUST \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /usr/bin/docker-containerd:/usr/bin/docker-containerd \
  -v /etc:/etc:ro \
  -v /lib/systemd/system:/lib/systemd/system:ro \
  docker/docker-bench-security

echo "===================================="
echo "Audit completed at: $(date)"
