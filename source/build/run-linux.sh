#!/bin/sh
if [ -z `which sludge-engine` ];
then
    echo "---------"
    echo "Please install the sludge-engine package and try again."
    echo "Apologies for the inconvenience :)"
else
    sludge-engine ld32-keyboardmonkey.slg
fi
