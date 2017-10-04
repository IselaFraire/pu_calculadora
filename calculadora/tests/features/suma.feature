Feature: Suma de dos numeros
    Como usuario de la calculadora
    deseo realizar la suma de dos numeros
    para obtener el resultado preciso

    Scenario: Suma de 2 mas dos
        Dado que sumo los números "2" y "2"
        cuando realizo la operacion
        entonces obtengo el resultado "4"

    Scenario: Suma de 2 mas dos
        Dado que sumo los números "7" y "5"
        cuando realizo la operacion
        entonces obtengo el resultado "12"

    Scenario: Suma de 0 mas -7
        Dado que sumo los números "0" y "-7"
        cuando realizo la operacion
        entonces obtengo el resultado "-7"

    Scenario: Suma de 1000 mas 100
        Dado que sumo los números "1000" y "100"
        cuando realizo la operacion
        entonces obtengo el resultado "1100"
