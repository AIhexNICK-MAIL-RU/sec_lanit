#!/bin/bash
echo "=== Dependency Check ==="
echo "Update NVD database..."
mvn org.owasp:dependency-check-maven:check -Dupdate=true
echo "Scan completed"
