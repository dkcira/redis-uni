#!/bin/bash
#===============================================================================
#
#          FILE: dockermacip.sh
# 
#         USAGE: ./dockermacip.sh 
# 
#   DESCRIPTION: find ip of docker-machine on the mac
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 06/29/2019 07:07
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

docker-machine ip default

