#!/usr/bin/perl
#
# The traditional first program.

# Strict and warnings are recommended.
use strict;
use warnings;

my $W = "PERL_SCRIPT:    ";


print "$W Hello, World!\n";

my $total = $#ARGV + 1;
my $counter = 1;

# get script name
my $scriptname = $0;

print "$W Total args passed to $scriptname : $total\n";

# Use loop to print all args stored in an array called @ARGV
foreach my $a(@ARGV) {
    print "$W Arg # $counter : $a\n";
    $counter++;
}

# (2) we got two command line args, so assume they are the
# first name and last name
my $message=$ARGV[0];

print "\n\n$W Message is, $message !!!\n\n";

sleep(3);
print STDOUT 'STDOUT:  garmushka';

print STDERR 'STDERR:  fanatic';