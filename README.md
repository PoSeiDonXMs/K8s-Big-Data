
# Clickhouse and Superset (scaled on K8S)

This project has the basic idea of generating and visualization of big queries on big data using clickhouse and superset which is scaled on k8s.



## Demo

![alt clickhouse_local](https://github.com/vedant-204/clickhouse-superset-k8s/blob/dev/assets/clickhouse_local.png)
![alt k9s_dep_view](https://github.com/vedant-204/clickhouse-superset-k8s/blob/dev/assets/k9s_dep_view.png)
![alt superset_connection](https://github.com/vedant-204/clickhouse-superset-k8s/blob/dev/assets/superset_connection.png)
![alt superset_home_page](https://github.com/vedant-204/clickhouse-superset-k8s/blob/dev/assets/superset_home_page.png)



## Installation

Install my-project with npm

```bash
git clone https://github.com/vedant-204/clickhouse-superset-k8s
```

```bash
cd clickhouse-superset-k8s \
cd superset \ 
docker-compose -f docker-compose-non-dev.yml pull \
docker compose -f docker-compose-non-dev.yml up \
```

```bash
minikube start
```

```bash
cd .. \
cd clickhouse-operator/deploy/zookeeper/quick-start-persistent-volume
./zookeeper-1-node-create.sh
```

then you can further create the deployment using files in ```infrastructure``` directory.
