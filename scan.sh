#!/bin/bash
echo "Scanning Python code with Bandit..."
bandit -r . \
  -f json \
  --exclude venv,.venv,env,__pycache__,test,tests,build,dist \
  --output bandit_report.json \
  --severity LOW \
  --confidence LOW

echo "Report saved to bandit_report.json"
