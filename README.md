**TERCERA PRE ENTREGA**

1 Intenté mantener un diseño simple y responsive en el index que por ahora utilizo con extends en el resto (excepto el contenido del main) es decir extiendo el header y footer y para el resto uso blocks.


2. Las 3 clases definidas en models y forms son Cliente, Empleado y Producto (hay una llamada login que está comentada porque quise implementarla pero vi que era algo complejo y no requerido en la consigna al menos para
esta entrega, también varias funciones en views que no eliminé porque tal vez me sirvan para seguir trabajandolo más adelante)


3. Los formularios se encuentran usando los enlaces de la barra nav. Permiten agregar datos y están además las tablas con sus respectivos datos. Lo quise hacer todo en las mismas urls aunque en clase
lo haciamos con otras urls como "clienteForm". Se me hacía un poco molesto andar cambiando de url para ver cada cosa así que preferí poner todo en las paginas de clientes, empleados y productos.


4. Los formularios de busqueda también los incluí en esos enlaces por el mismo motivo, hay uno para cada modelo. Encontré una manera de hacer el filter con Q que importo de "django.db.models" que me gustó más porque no solo
filtro coincidencias de datos solamente en nombre por ejemplo, sino que también se puede buscar por apellido,id,etc. De manera que si quisiera buscar a alguien cuyo nombre no conozco pueda buscarlo por su id por ejemplo.


. Aún me faltan hacer cosas en el index de html y css que no las implementé porque no estaba seguro de como hacerlas, por ejemplo quería implementar un carrusel con imagenes, nombres y precios de los productos pero lo dejé
para un poco mas adelante para no perder demasiado tiempo con eso y llegar bien con las consignas.

. Estoy considerando para la entrega final hacer que esas urls de formularios solo sean accesibles para ciertos usuarios almacenados en la base de datos y quien entre a la pagina deberá iniciar sesión para poder verlos
  (porque los datos de clientes, empleados y productos podrían ser sensibles y privados para la empresa).

  .Hay algunos index que no se usan porque venian con la plantilla de bootstrap que quise usar pero finalmente no usé. No los eliminé ni el css de bootstrap porque capaz alguno me sirve o me da ideas para otras urls
  pero más adelante si no los uso los voy a eliminar.
