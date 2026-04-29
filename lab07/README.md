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
