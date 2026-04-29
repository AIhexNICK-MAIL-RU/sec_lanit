# Lab 07: SAST, SCA и Secret Detection

## Результаты сканирования

### Semgrep (SAST)
| Правило | Файл | Строка | Severity | Статус |
|---------|------|--------|----------|--------|
| hardcoded-password | app.py | 7-9 | ERROR | Fixed |
| sql-injection | app.py | 15 | ERROR | Fixed |
| command-injection | app.py | 21 | ERROR | Fixed |
| unsafe-pickle | app.py | 26 | ERROR | Fixed |
| eval-detected | app.py | 31 | WARNING | Fixed |

### Checkov (IaC)
| Check ID | Описание | Статус |
|----------|----------|--------|
| CKV_DOCKER_2 | HEALTHCHECK отсутствует | Fixed |
| CKV_DOCKER_3 | USER не указан | Fixed |
| CKV_DOCKER_7 | Latest tag | Fixed |

### Gitleaks (Secret Detection)
| Секрет | Файл | Статус |
|--------|------|--------|
| AWS ключ | config.yaml | Removed |
| GitHub токен | app.py | Removed |
| API ключ | app.py | Removed |

### TruffleHog
*Больше секретов найдено за счёт entropy-анализа*

## Сравнение инструментов

| Инструмент | Тип | Находки | TP/FP | Статус |
|------------|-----|---------|-------|--------|
| Semgrep | SAST | SQLi, Command Injection | TP | Fixed |
| Checkov | SAST | Docker misconfigs | TP | Fixed |
| OWASP DC | SCA | Log4j, Jackson | TP | Accepted |
| Gitleaks | Secret | Hardcoded secrets | TP | Fixed |
| TruffleHog | Secret | High entropy strings | TP/FP | Investigated |

## Semgrep Report

{
    "version": "1.161.0",
    "results": [
        {
            "check_id": "sast.unsafe-pickle",
            "path": "vulnerable-app/app.py",
            "start": {
                "line": 27,
                "col": 12,
                "offset": 767
            },
            "end": {
                "line": 27,
                "col": 33,
                "offset": 788
            },
            "extra": {
                "message": "Unsafe deserialization with pickle",
                "metadata": {},
                "severity": "ERROR",
                "fingerprint": "requires login",
                "lines": "requires login",
                "validation_state": "NO_VALIDATOR",
                "engine_kind": "OSS"
            }
        },
        {
            "check_id": "sast.eval-detected",
            "path": "vulnerable-app/app.py",
            "start": {
                "line": 31,
                "col": 12,
                "offset": 917
            },
            "end": {
                "line": 31,
                "col": 28,
                "offset": 933
            },
            "extra": {
                "message": "Eval execution of untrusted code",
                "metadata": {},
                "severity": "WARNING",
                "fingerprint": "requires login",
                "lines": "requires login",
                "validation_state": "NO_VALIDATOR",
                "engine_kind": "OSS"
            }
        }
    ],
    "errors": [
        {
            "code": 2,
            "level": "error",
            "type": "Rule parse error",
            "rule_id": "sast.command-injection",
            "message": "Rule parse error in rule sast.command-injection:\n Invalid pattern for Python: Stdlib.Parsing.Parse_error\n----- pattern -----\nsubprocess.call(... shell=True)\n----- end pattern -----\n"
        }
    ],
    "paths": {
        "scanned": [
            "vulnerable-app/app.py"
        ]
    },
    "time": {
        "rules": [],
        "rules_parse_time": 0.0017399787902832031,
        "profiling_times": {
            "config_time": 0.2922186851501465,
            "core_time": 0.22259283065795898,
            "ignores_time": 7.700920104980469e-05,
            "total_time": 0.524301290512085
        },
        "parsing_time": {
            "total_time": 0.0,
            "per_file_time": {
                "mean": 0.0,
                "std_dev": 0.0
            },
            "very_slow_stats": {
                "time_ratio": 0.0,
                "count_ratio": 0.0
            },
            "very_slow_files": []
        },
        "scanning_time": {
            "total_time": 0.00928187370300293,
            "per_file_time": {
                "mean": 0.00928187370300293,
                "std_dev": 0.0
            },
            "very_slow_stats": {
                "time_ratio": 0.0,
                "count_ratio": 0.0
            },
            "very_slow_files": []
        },
        "matching_time": {
            "total_time": 0.0,
            "per_file_and_rule_time": {
                "mean": 0.0,
                "std_dev": 0.0
            },
            "very_slow_stats": {
                "time_ratio": 0.0,
                "count_ratio": 0.0
            },
            "very_slow_rules_on_files": []
        },
        "tainting_time": {
            "total_time": 0.0,
            "per_def_and_rule_time": {
                "mean": 0.0,
                "std_dev": 0.0
            },
            "very_slow_stats": {
                "time_ratio": 0.0,
                "count_ratio": 0.0
            },
            "very_slow_rules_on_defs": []
        },
        "fixpoint_timeouts": [],
        "prefiltering": {
            "project_level_time": 0.0,
            "file_level_time": 0.0,
            "rules_with_project_prefilters_ratio": 0.0,
            "rules_with_file_prefilters_ratio": 1.0,
            "rules_selected_ratio": 0.75,
            "rules_matched_ratio": 0.75
        },
        "targets": [],
        "total_bytes": 0,
        "max_memory_bytes": 90164608
    },
    "engine_requested": "OSS",
    "skipped_rules": [],
    "profiling_results": []
}
