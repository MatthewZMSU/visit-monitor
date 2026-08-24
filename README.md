# visit-monitor

Репозиторий содержит:
* Python приложение на FastAPI с использованием SQLAlchemy + Psycopg;
* Миграция БД с помощью Alembic;
* Управление Python-зависимостями с помощью uv;
* k8s-манифесты.

# Сборка приложения

Создать докер образ можно, запустив команду из корня проекта:
```bash
docker build -t visits-service:0.1
```

# Поднятие k8s-кластера с помощью minikube

Для поднятия кластера запускаем команду:
```bash
minikube start --vm-driver=kvm
```

# Загрузка docker-образа

Загрузить [docker-образ](#сборка-приложения) можно так:
```bash
minikube image load visits-service:0.1
```

Проверить загрузку можно командой:
```bash
minikube image ls --format table
```

# Применение k8s-манифестов

По-очереди применяем манифесты:

Для Postgres нужно место, обеспечим его с помощью PVC:
```bash
kubectl apply -f k8s-manifests/persistent-volume-claim.yaml
```

Так как Postgres нужно место на определённом PVC, то используем StatefulSet,
а не Deployment или ReplicaSet:
```bash
kubectl apply -f k8s-manifests/stateful-set.yaml
```

Чтобы обеспечить доступ к Postgres из Python-приложения по доменному имени организуем service:
```bash
kubectl apply -f k8s-manifests/service.yaml
```

И в последнюю очередь разворачиваем deployment с 2 репликами:
```bash
kubectl apply -f k8s-manifests/deployment.yaml
```

# Демонстрация

Видео демонстрация: [гугл-диск](https://drive.google.com/file/d/1jKnzR2-3To1fpcJv1yBAPVpME510bsB0/view?usp=drive_link)
