from kafka import KafkaConsumer
import six
import sys
if sys.version_info >= (3, 12, 0):
    sys.modules['kafka.vendor.six.moves'] = six.moves
    
    
#consumer = KafkaConsumer()

# define a consumer that waits for new messages
def kafka_python_consumer():
    
    # Consumer using the topic name and setting a group id
    consumer = KafkaConsumer('mytesttopic', group_id='mypythonconsumer',bootstrap_servers='localhost:9092',)
    for msg in consumer:
      print(msg)

print("start consuming")

# start the consumer
kafka_python_consumer()

print("done")