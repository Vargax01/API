<!DOCTYPE html>
<html lang="es">
<head>
<link rel="stylesheet" type="text/css" href="/style/correo.css" />
<title>Compartir</title>
</head>
<body>
<a title="VargaxTune" href="/inicio"><img src="/style/images/vargaxtunepeque.png" /></a>
<img src="/style/images/itunespeque.png"><br>
% if cont == 1:
 <h1 class="centro">Tweet Enviado</h1>
 <a href="/correo/{{codigo}}"><h3>Volver Atras</h3></a>
% else:
<h1 class="centro">Correo Enviado</h1>
<a href="/correo/{{codigocan}}"><h3>Volver Atras</h3></a>
% end
</body>
</html>