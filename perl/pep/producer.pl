#!/usr/bin/perl
#
# The traditional first program.

# Strict and warnings are recommended.
use strict;
use warnings;

# Print a message.
print "Hello, Pep Producer!\n";


use 5.010;
use strict;
use warnings;

use Scalar::Util qw(
    blessed
);
use Try::Tiny;

use Kafka::Connection;
use Kafka::Producer;

my ( $connection, $producer );
try {

    #-- Connection
    $connection = Kafka::Connection->new(
        host => 'wielder-kafka.kafka.svc.cluster.local',
        port => '9092',
    );

    #-- Producer
    $producer = Kafka::Producer->new( Connection => $connection );

    # Sending a single message
    my $response = $producer->send(
        'demo',          # topic
        0,                  # partition
        'Single message'    # message
    );

    # Sending a series of messages
    $response = $producer->send(
        'demo',          # topic
        0,                  # partition
        [                   # messages
            'The first message',
            'The second message',
            'The third message',
        ]
    );

} catch {
    my $error = $_;
    if ( blessed( $error ) && $error->isa( 'Kafka::Exception' ) ) {
        warn 'Error: (', $error->code, ') ',  $error->message, "\n";
        exit;
    } else {
        die $error;
    }
};

# Closes the producer and cleans up
undef $producer;
$connection->close;
undef $connection;