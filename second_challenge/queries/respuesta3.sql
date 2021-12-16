USE my_db;

SELECT v.DIA, COUNT(*) NUMERO_DE_VUELOS
FROM vuelos v
GROUP BY v.DIA
ORDER BY NUMERO_DE_VUELOS DESC
LIMIT 1;

# El dia con mayor numero de vuelos es 2021-05-02