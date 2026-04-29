# Lab 08: DAST с OWASP ZAP

## Найденные уязвимости

| Уязвимость | URL | Risk | CWE | Статус |
|------------|-----|------|-----|--------|
| Reflected XSS | /echo | High | 79 | Fixed |
| SQL Injection | /search | High | 89 | Fixed |
| Authentication Bypass | /login | High | 287 | Fixed |
| Insecure Cookie | /profile | Medium | 614 | Fixed |
| Missing AuthZ | /admin | High | 862 | Fixed |
| Directory Listing | /files/ | Medium | 548 | Fixed |
| Path Traversal | /files/ | High | 22 | Fixed |

## Сравнение ручного и автоматического тестирования

### ZAP нашёл автоматически:
- SQL Injection в /search
- Reflected XSS в /echo
- Missing Security Headers
- Cookie without HttpOnly flag

### ZAP пропустил (найдено вручную):
- Directory listing (ZAP не обходит все директории)
- Path traversal (требует специфического payload)
- Auth bypass через подделку cookie (требует бизнес-логики)

### False Positives (исключены):
- XSS в статическом контенте (не эксплуатируемо)

## HTTP заголовки безопасности

| Заголовок | Статус | Риск |
|-----------|--------|------|
| X-Frame-Options | Missing | Clickjacking |
| X-Content-Type-Options | Missing | MIME sniffing |
| Content-Security-Policy | Missing | XSS |
| Strict-Transport-Security | Missing | Protocol downgrade |

## Исправления

1. Экранирование пользовательского ввода (XSS)
2. Параметризованные запросы (SQL Injection)
3. Добавлена проверка авторизации для /admin
4. HttpOnly флаг для cookies
5. Запрет обхода директории
6. Отключен DEBUG режим
