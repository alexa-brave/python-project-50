### Hexlet tests and linter status:
[![Actions Status](https://github.com/alexa-brave/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/alexa-brave/python-project-50/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=alexa-brave_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=alexa-brave_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=alexa-brave_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=alexa-brave_python-project-50)

## Ascinema gendiff from json, yaml; to stylish, plain, json:
[![asciicast](https://asciinema.org/a/HplmDCyez0Gg4nXb.svg)](https://asciinema.org/a/HplmDCyez0Gg4nXb)

## Описание

Gendiff — утилита для сравнения двух конфигурационных файлов.  
Поддерживает форматы JSON и YAML.

## Установка

```bash
make install
```

## Запуск
uv run gendiff path/to/file1.json path/to/file2.json

## Форматы вывода
### По умолчанию используется формат stylish:
```bash
uv run gendiff file1.json file2.json
```

### Для plain:
```bash
uv run gendiff file1.json file2.json -f plain
```

### Для json:
```bash
uv run gendiff file1.json file2.json -f json
```