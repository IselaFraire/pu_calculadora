Feature: Resta de dos numeros
    Como usuario de la calculadora
    deseo realizar la resta de dos numeros
    para obtener el resultado preciso

    Scenario: Resta de 3 menos uno
        Dado que resto dos números "3" y "1"
        cuando realizo la operacion
        entonces obtengo el resultado "2"

    Scenario: Resta de 2 menos dos
        Dado que resto dos números "2" y "2"
        cuando realizo la operacion
        entonces obtengo el resultado "0"

    Scenario: Resta de 1000 menos cien
        Dado que resto dos números "1000" y "100"
        cuando realizo la operacion
        entonces obtengo el resultado "900"
