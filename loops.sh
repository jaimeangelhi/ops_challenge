
# Execution:                    bash loops.sh
# Additional sources:           X

# Declaration of Variables

var=0

# Declaration of functions

# Main

while [ $var -lt 10 ]
do
    echo $var
    var=$((var+1))
done

# End