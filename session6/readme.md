

# Network commands

## to check listening port 5050
    netstat -an -o | grep LISTEN | grep 5050



# Exceptions

## classic c error handling:
    result = test_function()
    if(result != 0) {
        // handle error
    }

## OOP exception handling
    first -> excptions are raised or thrown
    then  -> exceptions are catched and handled

    fn1 --call--> f2 --call--> f3 --call--> f4

    fn1
        fn2 -> handle ex
            fn3 -> raise ex
                fn4 -> raise ex


