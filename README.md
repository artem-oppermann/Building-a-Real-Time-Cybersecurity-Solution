# README: Real-Time Cybersecurity Solution using Streaming Database for Threat Detection

This README outlines the steps to set up a real-time threat detection system using RisingWave, a streaming database. The system is designed to analyze network traffic and server log data to identify and mitigate potential cyber threats instantly.

## Overview

Real-time threat detection is crucial in cybersecurity. This project demonstrates building such a system with RisingWave to detect threats like DDoS attacks, unusual log entries, and CVE vulnerabilities.

## Prerequisites

- Python 3.11 or higher
- Docker (v24.0.6 or higher)
- Apache Kafka (running on Docker)
- RisingWave (latest version in Docker)
- psql (Postgres interactive terminal)
- psycopg2-binary (PostgreSQL database adapter for Python)

## Setup

### 1. Generate Synthetic Dataset

- Create `generate_data.py` and run it to generate `synthetic_log_data.json`.

  ```bash
  python generate_data.py
  ```

### 2. Install Risingwave using Docker

- Pull and run RisingWave Docker image.

  ```bash
  docker run -it --pull=always -p 4566:4566 -p 5691:5691 risingwavelabs/risingwave:latest playground
  ```

- Connect to RisingWave via psql.

  ```bash
  psql -h localhost -p 4566 -d dev -U root
  ```

### 3. Create Kafka Topics

- Create `log_data` and `anomalies` topics in Kafka.

  ```bash
  docker exec <container_name> kafka-topics.sh --create --topic <topic_name> --partitions 1 --replication-factor 1 --bootstrap-server kafka:9092
  ```

- Verify topic creation.

  ```bash
  docker exec <container_name> kafka-topics.sh --list --bootstrap-server kafka:9092
  ```

### 4. Connect RisingWave to Kafka

- Run `create_data_source.py` to link RisingWave with Kafka topic `log_data`.

  ```bash
  python create_data_source.py
  ```

### 5. Produce Data to Kafka Topic

- Use `produce.py` to send data to `log_data` topic.

  ```bash
  python produce.py
  ```

### 6. Threat Detection with RisingWave

- Create a materialized view in RisingWave for anomaly detection using `create_mv.py`.

  ```bash
  python create_mv.py
  ```

- Use `show_result.py` to display results.

  ```bash
  python show_result.py
  ```

### 7. Sink Data Back to Kafka

- Run `sink.py` to create a sink in RisingWave and send data to Kafka topic `anomalies`.

  ```bash
  python sink.py
  ```

- Verify data transfer to `anomalies` topic in Kafka.

  ```bash
  kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic anomalies --from-beginning
  ```
