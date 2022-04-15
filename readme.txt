¡Hola! 

Somos Agustín Tornati y Ailín Dagnino. Bienvenido a nuestro WIP (Work in Progress)

Nuestro blog está destinado a reviews de pelis, libros y series.
Primero, al entrar al link del servidor (http://127.0.0.1:8000/) enconrtarás el home.
En el home, podrás leer una vista previa de cada post ordenado por más reciente, 
editar los posts ya existentes, agregar posts nuevos, acceder a las consignas del trabajo, o a la pag del curso.

Para crear un post nuevo, el botón de "Add post" nos permite indicar título, slug (lo que va en la url),
creador y status (si queremos publicarlo, o queremos guardar un borrador, por defecto, se selecciona borrador).
Ademas hay un botón de categoría que nos permitirá indicar qué es sobre lo que estamos escribiendo.

Al tocar post, te lleva a la vista detallada de tu propio post. Para volver a home, simplemente toca "home" 
en la esquina superior izquierda.

Para editar lo recién mencionado, tanto en la vista detallada como en el home podrás tocar "editar" y modificar los campos. 

Con read more, podrás acceder a la vista detallada del post.

Si quieres buscar un post en particular, el search bar te ayudará con eso. Solamente tipea lo que quieres buscar,
y podrás seleccionar e ir al post que corresponda a tu búsqueda. 

También hicimos el log in y el register para limitar el uso de las funcionalidades de la página

PD:
No logramos hacer funcionar las vistas que queremos después del sign in:
- Quisieramos que cuando uno toca "edit" o "add post" luego del sign in idealmente lo lleve 
  a editar o a agregar un post directamente. No logramos modificar eso, con lo que intentamos que lleve 
  al home, pero solo muestra el about del costado, y no muestra el listado de posts.
- Del mismo modo con el log out quisieramos que muestre el inicio con todos los posts, y solo
  muestra el about del costado.

Lo solucionamos redireccionando a una vista que da anuncio del inicio/cierre de sesión y
redirige al home mediante un botón. Son pasos extra pero está funcional.


Desde ya, muchas gracias y esperemos que te guste el proyecto!
