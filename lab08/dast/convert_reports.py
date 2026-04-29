#!/usr/bin/env python3
import json
import sys

def convert_zap_json(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    sites = data.get('site', [])
    alerts = []
    
    for site in sites:
        for alert in site.get('alerts', []):
            alerts.append({
                'name': alert.get('name'),
                'risk': alert.get('risk'),
                'url': alert.get('url'),
                'param': alert.get('param'),
                'cwe': alert.get('cweid'),
                'description': alert.get('description'),
                'solution': alert.get('solution')
            })
    
    with open(output_file, 'w') as f:
        json.dump(alerts, f, indent=2)
    
    print(f"Converted {len(alerts)} alerts to {output_file}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        convert_zap_json(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'converted_report.json')
