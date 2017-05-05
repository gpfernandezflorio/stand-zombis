Stand Apocalipsis Zombi
===

![preview](zombis1.png)

![preview](zombis2.png)

Descripción:
---
 * Simulador de propagación de plagas/enfermedades en el espacio utilizando ecuaciones diferenciales.
 * Software original desarrollado por Alex Alemi y Matt Bierbaum.
 * Modificado para incluír mapas de Argentina, Buenos Aires, el Conurbano y Capital Federal.

Instrucciones para ejecutar el stand:
---
 * (opcional) modificar la variable EVENT (en event.js) según el evento actual.
 * Abrir index.html en un navegador web.
 * Abrir mod.html en un navegador web.
 * Abrir la carpeta "resultados" en un navegador de archivos.

Requiere:
---
 * Navegador web Firefox en Ubuntu. Chromium no funciona.
 * Reproductor de video (VLC funciona. El programa por defecto de Ubuntu también, aunque no es tan lindo).
  - Configurarlo para que loopée.
 * No hace falta conexión a internet.

Instrucciones de uso:
---
 * Una vez elegido el mapa, hacer click para posicionar un zombi en el espacio. La simulación inicia automáticamente.
 * Los parámetros  y  pueden modificarse arrastrando el slider correspondiente en la pantalla.
 * La simulación se puede pausar con 'P' o haciendo click en 'Pause'.
 * La simulación se puede reiniciar con 'Q' o haciendo click en 'Reset'.
 * Para las explicaciones, utilizar las imágenes y los videos en la carpeta "resultados".

Links:
---
 * [Repositorio](https://git.exactas.uba.ar/extension-dc/stand-zombis/)
 * [Repositorio de la versión original](https://github.com/mattbierbaum/zombies-usa/)
 * [Demo online de la versión original](http://mattbierbaum.github.io/zombies-usa/)

Speech:
---
 Imaginen que se desata un apocalipsis zombi. ¿Qué harían? ... ¿Qué creen que haría un (científico|matemático)? ... Se uniría a la pelea pero primero se haría esta pregunta: ¿vale la pena el esfuerzo o estamos condenados a perder? La forma de responder a esta pregunta es modelando el problema y simulando el resultado. El modelo nos va a decir cómo se comporta el mundo. No se puede modelar la realidad a la perfección, así que los modelos son aproximados y por eso puede haber varios modelos válidos para un mismo problema. Por ejemplo, podemos modelar el apocalipsis zombi de la siguiente manera:

 Tenemos la cantidad de humanos H y la cantidad de zombis Z. Queremos saber si después de un determinado tiempo, los humanos pueden erradicar a los zombis o si los zombis van a adueñarse del planeta. Para eso necesitamos saber cómo se comportan la cantidad de humanos y de zombis a través del tiempo. ¿Cómo se modifica la cantidad de humanos? Si un zombi muerde a un humano y este se convierte en zombi, tenemos un humano menos. Cada vez que nace un humano, tenemos un humano más. Cuando un humano muere por causas naturales, tenemos un humano menos. Entonces, la cantidad de humanos dentro de un año va a ser la cantidad de humanos hoy, más la cantidad de humanos que nacen por año, menos la cantidad de humanos que mueren por causas naturales, menos la cantidad de humanos que se convierten en zombis.

 H1 = H0 + Nac. - Mue. - Zom.

 Por otro lado, la cantidad de zombis aumenta cuando un humano se convierte en zombi y se reduce cuando un humano mata a un zombi. Sin embargo, los zombis no mueren por causas naturales ni se reproducen. Así que la cantidad de zombis dentro de un año va a ser la cantidad de zombis hoy, más la cantidad de humanos que se convierten en zombis, menos la cantidad de zombis que son asesinados por humanos.

 Z1 = Z0 + Zom. - Mat.

 La cantidad de humanos que nacen y mueren las podemos aproximar sabiendo la tasa de natalidad y mortalidad de la población. Para conocer la cantidad de humanos que se convierten en zombis y la cantidad de zombis que se convierten en humanos, primero vamos a definir la tasa de interacción, que indica que tan probable es que un zombi y un humano se enfrenten y la tasa de conversión, que indica el resultado del enfrentamiento. Si la tasa de conversión vale 1.0, todo enfrentamiento termina con el humano convertido en zombi. Si vale 0.0, todo enfrentamiento termina en el humano matando al zombi.

Pasamos al simulador unidimensional.

Ver por ejemplo, si no hay interacción, los zombis se mantienen constantes y la curva de los humanos sólo depende de natalidad y mortalidad (esto sirve para simular el crecimiento poblacional real). Al incrementar la interacción, parece inevitable que en algún momento, los zombis ganen (por que la tasa de conversión es 1). Al bajar la tasa de conversión, llega un punto en el que es posible sobrevivir (ej: interacción=0.5 conversión (<) 0.56).

Este simulador sirve para el modelo que define el comportamiento con estas escuaciones, pero podrían hacer otros modelos del mismo problema. Por ejemplo, si se modelan distintas propiedades sobre los humanos y los zombis, cambiaría la ecucación que define la cantidad de humanos que se convierten y la cantidad de zombis que los humanos matan. Lo mismo si modelamos las armas con las que los humanos se defienden, etc.

También se pueden agregar variantes al modelo, como la cantidad de zombis que se "curan", en caso de que exista una cura, o la cantidad de humanos que los zombis matan (hasta ahora asumimos que los zombis no pueden matar humanos, sólo convertirlos).

Por otro lado, tenemos este otro simulador que en lugar de simular la cantidad de humanos y zombis a través del tiempo, simula la propagación de los zombis por el espacio, a través del tiempo.

Pasamos al simulador bidimensional.

En este caso, los parámetros son , que define una tasa "Kill to Bite", es decir, cuantos zombis mueren por cada humano que se convierte y , que define la velocidad con la que se mueven los zombis por el espacio.

Ver por ejemplo, que las zonas aisladas nunca se contagian. Al igual que con el simulador unidimensional, una forma de sobrevivir es eliminando la interacción. Otra, es contratacar. Si los humanos no matan zombis (tasa de conversión=1 en el anterior, ratio "Kill to Bite"=0 en este) es inevitable que los zombis ganen, lo cual tiene sentido.

Así que ahora ya saben qué tienen que hacer ante un apocalipsis zombi: Aislarse, o contratacar.

Más allá del tema de los zombis, esto se usa en la vida real para modelar y simular propagación de enfermedades, con un modelo muy similar al visto en el primer caso, sólo que nadie mata a los enfermos!
