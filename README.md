# Pre-entrega N°3 del curso de Python - CoderHouse
# Comision: 54140
# Estudiante: Pablo Martinez

`Bienvenido a mi pre-entrega.`

`Dentro de ingreso está el registro de personal y control de acceso/egreso.`

> esto fue posible por los modelos Usuario, Ingrego y Egreso. 
> Ya que Usuario registra los que serán los vendedores en el área de ventas.
> Por otro lado los modelos Ingreso y Egreso son para control de acceso, donde marcan la entrada o salida de su turno de trabajo.


`Dentro de ventas se pueden agregar los productos, los clientes y efectuar las ventas.`

> En ventas tenemos los modelos NuevoCliente, que registra los clientes.
> El modelo NuevoProducto que carga los productos para vender.
> El modelo Venta que realiza la venta en sí, donde llama las ForeignKey NuevoCliente, NuevoProducto y Usuario.
> Tambien hay modelos que son ForeignKey dentro de NuevoCliente y NuevoProducto, que son: Localidad, Pais y Marca.

> Dentro de Usuarios, NuevoProducto, NuevoCliente y Venta, se crearon views para mostrar los registros.
> Dentro de la lista de Productos podemos editar los productos.
> Dentro de la lista de Clientes podemos buscarlos por nombre.

`En un futuro se podría:`
> Crear un área de venta donde el cliente pueda iniciar sesión, comprar él y no tenga que intervenir el "vendedor".
> En la misma área, antes mencionada, se podría crear una sección de consulta donde el cliente envía la consulta al vendedor y este le responde por mail u otro medio.
