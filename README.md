# python-selenium-page-object-model

We will see:
* 1 Create a simple login test
* 2 Unit Testing
* 3 Implement Page Object Model
* 4 Separate Test Scripts and objects
* 5 Create separate class for Locators
* 6 Run from cli
* 7 Add html reports

* Tutorial
    https://www.youtube.com/watch?v=BURK7wMcCwU

## Dependencies
    pip install selenium
    pip install htm-testRunner
## Run unittest
``` python -m unittest Tests/login.py ```

From project folder
``` python -m Tests.login ```

## Page Object Model (POM)
Patrón de diseño. El Page Object Model es la solución que se encontró al problema de que las funciones se repiten y las acciones las tenemos que hacer varias veces para diferentes tests. Es muy engorroso tener que cambiar cada implementación cuando algo cambió en el test, por lo que este acercamiento lo que hace es modelar cada página de nuestra aplicación una sola vez y llamar las acciones sobre ella todas las veces que necesitemos, desde una única fuente.

En este caso tenemos
* 1 - Login Page
    * a username locator 
    * b password locator
    * c login button locator
* 2 - Home Page
    * a welcome locator
    * b logout locator
