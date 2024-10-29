# Working with topics

docker exec -it <container_name or id> bash

# Working dir
cd /opt/bitnami/kafka/bin
# Show all the scripts
ls -a

## List Topics
./kafka-topics.sh --list --bootstrap-server localhost:9092

## Create Topic
./kafka-topics.sh --create --topic mytesttopic --bootstrap-server localhost:9092

## Describe a topic
./kafka-topics.sh --describe --topic mytesttopic --bootstrap-server localhost:9092
./kafka-console-consumer.sh --topic mytesttopic --bootstrap-server localhost:9092

# Check Consumer Offset
./kafka-consumer-groups.sh --bootstrap-server localhost:9092  --describe --group mypythonconsumer