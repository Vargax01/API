<!DOCTYPE html>
<html lang="es">
<head>
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
% if TOKENS.has_key("verifier"):
<a title="Twitter" href="/twittear/{{codigocan}}"><h2 class="centro">Compartir via twitter</h2></a><br>
% end
<img src="/style/images/twitter1.png" class="twitter">
</body>
</html>