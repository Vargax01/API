<!DOCTYPE html>
<html lang="es">
<head>
<link rel="icon" type="image/png" href="/style/images/logovxt.png" />
<link rel="stylesheet" type="text/css" href="/style/correo.css" />
<title>Compartir</title>
</head>
<body>
<a title="VargaxTune" href="/inicio"><img src="/style/images/vargaxtunepeque.png" /></a>
<img src="/style/images/itunespeque.png"><br>
<form id="formcorreo" action="#" method="post">
<table>
<tr>
<th>
<h1>Almacene sus canciones favoritas en su correo</h1></th>
</tr>
<tr>
<th><h2>Escribe tu correo: </h2>
<input type="text" name="correo" /></th>
</tr>
<tr>
<th><img src="/style/images/gmail1.png"></th>
</tr>
</table>
<input type="submit" name="enviar" value="Enviar Correo" class="enviar" />
</form>
% if cont == 1:
	<a href="/twittear/{{codigocan}}"><h3 class="centro">Compartir en Twitter</h3></a>
	<img src="/style/images/twitter1.png" class="twitter">
% end
</body>
</html>