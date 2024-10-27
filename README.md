## Хакатон 2024 Осень - Axenix
Сервис по бронированию билетов на поезд  

## Локальный запуск с помощью Docker
1. Склонируйте репозиторий:
```bash
git clone https://github.com/yopepsiii/axenix_case.git .
```
2. Добавьте `.env` файл в папку `backend` и заполните согласно файлу `config.py`
3. Docker-compose:
```bash
docker compose -f compose_files/docker-compose-dev.yml up -d
```
4. Откройте документацию: [*тык*](http://localhost/api/v1/docs)

### Комментарии по backend  
- Надо продебажить `api/v1/order'  
- Возможно расширить роуты для фильтрованной информации
