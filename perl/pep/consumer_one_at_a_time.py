#!/usr/bin/env python

from kafka import KafkaConsumer, OffsetAndMetadata, TopicPartition
import subprocess as sp
import shlex

import time


def cmd_for_return_code(command, msg='msg'):
    """
    Runs a linux shell command and:
    1. Ignores standard output.
    2. Listens for errors.
    3. Waits for return code.
    :param msg: if you wish to add a compound string as arg
    :param command: compound Linux command
    :return: return code.
    """

    args = shlex.split(command)
    args.append(msg)

    # p = sp.Popen(args, stdout=sp.PIPE, stderr=sp.PIPE)

    p = sp.Popen(args, stderr=sp.PIPE)

    output, err = p.communicate()
    print(f'\n\noutput: {output}')
    print(f'err: {err}')

    rc = p.returncode

    print(f'perl returned with return code: {rc}')

    return rc


def do_something_time_consuming():
    try:
        print('sleeping...')
        time.sleep(4)
        print('... slept')
    except Exception as e:
        print(e)


KAFKA_BROKERS = 'wielder-kafka.kafka.svc.cluster.local:9092'
KAFKA_TOPIC = 'demo'
GROUP_ID = 'pep2'

print(f'KAFKA_BROKERS: {KAFKA_BROKERS}\n Topic {KAFKA_TOPIC}\n group id: {GROUP_ID}')

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKERS,
    group_id=GROUP_ID,
    enable_auto_commit=False,
    max_poll_records=1
)

print(f'bootstrap_servers: {KAFKA_BROKERS} subscribing to {KAFKA_TOPIC}')
consumer.subscribe([KAFKA_TOPIC])

for message in consumer:
    print(f"message is of type: {type(message)}")
    print(message)

    # do_something_time_consuming()
    _cmd = f"perl ./pep.pl"
    cmd_for_return_code(_cmd, msg=message.value)

    meta = consumer.partitions_for_topic(message.topic)

    partition = TopicPartition(message.topic, message.partition)
    offsets = OffsetAndMetadata(message.offset + 1, meta)
    options = {partition: offsets}

    print(f'\noptions: {options}\n')

    response = consumer.commit(offsets=options)



