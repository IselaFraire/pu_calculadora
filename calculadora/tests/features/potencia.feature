Feature: Potencia de dos numeros
    Como usuario de la calculadora
    deseo realizar la potencia de dos numeros
    para obtener el resultado preciso

    Scenario: Potencia de 3 a la 3
        Dado que potencio dos números "3" y "3"
        cuando realizo la operacion
        entonces obtengo el resultado "27"

    Scenario: Potencia de 9 a la 3
        Dado que potencio dos números "9" y "3"
        cuando realizo la operacion
        entonces obtengo el resultado "729"

    Scenario: Potencia de 10 a la 5
        Dado que potencio dos números "10" y "5"
        cuando realizo la operacion
        entonces obtengo el resultado "100000"
