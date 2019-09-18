#!/usr/bin/perl

use 5.010;
use strict;
use warnings;

# Print a message.
print "Hello, Pep Consumer!\n";

use Scalar::Util qw(
    blessed
);
use Try::Tiny;

use Kafka qw(
    $DEFAULT_MAX_BYTES
    $DEFAULT_MAX_NUMBER_OF_OFFSETS
    $RECEIVE_EARLIEST_OFFSET
);
use Kafka::Connection;
use Kafka::Consumer;

my ( $connection, $consumer );
try {

    #-- Connection
    $connection = Kafka::Connection->new( host => 'wielder-kafka.kafka.svc.cluster.local' );

    #-- Consumer
    $consumer = Kafka::Consumer->new( Connection  => $connection );

    # Get a valid offset before the given time
    my $offsets = $consumer->offset_before_time(
        'demo',                      # topic
        0,                              # partition
        (time()-3600) * 1000,           # time
    );

    if ($offsets){

        if ( @$offsets ) {
            say "Received offset: $_" foreach @$offsets;
        } else {
            warn "Error: Offsets are not received\n";
        }
    }


    # Consuming messages
    my $messages = $consumer->fetch(
        'demo',                      # topic
        0,                              # partition
        0,                              # offset
        $DEFAULT_MAX_BYTES              # Maximum size of MESSAGE(s) to receive
    );

    if ( $messages ) {
        foreach my $message ( @$messages ) {
            if ( $message->valid ) {
                say 'payload    : ', $message->payload;
                say 'key        : ', $message->key;
                say 'offset     : ', $message->offset;
                say 'next_offset: ', $message->next_offset;
            } else {
                say 'error      : ', $message->error;
            }
        }
    }

} catch {
    my $error = $_;
    if ( blessed( $error ) && $error->isa( 'Kafka::Exception' ) ) {
        warn 'Error: (', $error->code, ') ',  $error->message, "\n";
        exit;
    } else {
        die $error;
    }
};

# Closes the consumer and cleans up
undef $consumer;
$connection->close;
undef $connection;