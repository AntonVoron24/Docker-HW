### Сборка образа

```
docker build ./ --tag stockproducts
```

### Запуск контейнера

```
docker run --name my_stockproducts -d -p 8000:8000 stockproducts
```