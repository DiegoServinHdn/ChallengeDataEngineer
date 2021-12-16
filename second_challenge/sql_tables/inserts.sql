use my_db;

INSERT INTO aerolineas (NOMBRE_AEROLINEA) VALUES ('Volaris'), ('Aeromar'), ('Interjet'), ('Aeromexico');
    
INSERT INTO aeropuertos (NOMBRE_AEROPUERTO) VALUES ('Benito Juarez'), ('Guanajuato'), ('La paz'), ('Oaxaca');

INSERT INTO movimientos (DESCRIPCION) VALUES ('Salida'), ('Llegadas');

INSERT INTO vuelos (ID_AEROLINEA, ID_AEROPUERTO, ID_MOVIMIENTO, DIA) 
	VALUES 
    (1, 1, 1, '2021-05-02'),
    (2, 1, 1, '2021-05-02'),
    (3, 2, 2, '2021-05-02'),
    (4, 3, 2, '2021-05-02'),
    (1, 3, 2, '2021-05-02'),
    (2, 1, 1, '2021-05-02'),
    (2, 3, 1, '2021-05-04'),
    (3, 4, 1, '2021-05-04'),
    (3, 4, 1, '2021-05-04');