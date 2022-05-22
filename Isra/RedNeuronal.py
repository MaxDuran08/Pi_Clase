from tabnanny import verbose
import numpy as np
import tensorflow as tf


class RedNeuronal:
    def __init__(self):
        self.historial=None
        self.modelo=None

    def Aprender(self):
        celsius = np.array([-40,-10,0,8,15,22,38],dtype=float)
        fahrenheit = np.array([-40,14,32,46,59,72,100],dtype=float)

        capa = tf.keras.layers.Dense(units=1, input_shape=[1])
        self.modelo = tf.keras.Sequential([capa])

        self.modelo.compile(
        optimizer = tf.keras.optimizers.Adam(0.1),
        loss = 'mean_squared_error'
        )

        print('Entrenamiento iniciado')
        self.historial = self.modelo.fit(celsius,fahrenheit,epochs=1000, verbose=False)
        print('Termino el entrenamiento')

    def RetornarHistorial(self):
        return self.historial

    def Predecir(self,valor):
        resultado = self.modelo.predict([valor])
        print(resultado)