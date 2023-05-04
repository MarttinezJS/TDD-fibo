## Curls
### /hello - Devuelve el mensaje "Hello FastAPI"
~~~
curl -X 'GET' \
  'http://localhost:8000/hello' \
  -H 'accept: application/json'
~~~
### /IsPrime - Recibe un número entero y devuelve "true" o "false" si el número es primo
~~~
curl -X 'GET' \
  'http://localhost:8000/is-prime/13' \
  -H 'accept: application/json'
~~~

### /fibonacci -  Recibe un número entero con la posición y devuelve el número fibonacci que corresponda (1, 1, 2, 3, 5, 8, 13, 21…)

~~~
curl -X 'GET' \
  'http://localhost:8000/fibonacci/8' \
  -H 'accept: application/json'
~~~