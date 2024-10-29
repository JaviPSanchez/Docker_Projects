# Use the Bitnami Kafka image as the base image
FROM bitnami/kafka:2.8.0-debian-10-r42

# Optional: Add any custom scripts or configurations
COPY custom-config.sh /opt/bitnami/kafka/custom-config.sh
RUN chmod +x /opt/bitnami/kafka/custom-config.sh

# Optional: Run any additional setup commands
# RUN apt-get update && apt-get install -y <additional-packages>

# Set entrypoint
ENTRYPOINT ["/opt/bitnami/kafka/custom-config.sh"]
