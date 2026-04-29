#!/bin/bash

ZAP_IMAGE="${ZAP_IMAGE:-ghcr.io/zaproxy/zaproxy:stable}"
TARGET_URL="${TARGET_URL:-http://host.docker.internal:8080}"
REPORTS_DIR="./dast/reports"

mkdir -p "$REPORTS_DIR"

echo "=== ZAP DAST Scan ==="
echo "Target: $TARGET_URL"
echo "Reports dir: $REPORTS_DIR"

docker run --rm -v "$(pwd)/dast/reports:/zap/reports" \
  "$ZAP_IMAGE" zap-baseline.py \
  -t "$TARGET_URL" \
  -g gen.conf \
  -r reports/report.html \
  -w reports/report.md \
  -x reports/report.xml \
  -J reports/report.json \
  -z "configs/zap-baseline.conf"

echo "Scan completed. Reports saved to $REPORTS_DIR"
