Feature: Raiz de un numero
    Como usuario de la calculadora
    deseo realizar la raiz de un numero
    para obtener el resultado preciso

    Scenario: Raiz de 25
        Dado que saco la raiz del número "25"
        cuando realizo la operacion
        entonces obtengo el resultado "5"

    Scenario: Raiz de 100
        Dado que saco la raiz del número "100"
        cuando realizo la operacion
        entonces obtengo el resultado "10"

    Scenario: Raiz de 1
        Dado que saco la raiz del número "1"
        cuando realizo la operacion
        entonces obtengo el resultado "1"
