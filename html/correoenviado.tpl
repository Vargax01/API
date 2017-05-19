<!DOCTYPE html>
<html lang="es">
<head>
<link rel="stylesheet" type="text/css" href="/style/correo.css" />
<title>Compartir</title>
</head>
<body>
<a title="VargaxTune" href="/inicio"><img src="/style/images/vargaxtunepeque.png" /></a>
<img src="/style/images/itunespeque.png"><br>
<h1 class="centro">Correo Enviado</h1>
% if TOKENS.has_key("verifier"):
<a title="Twitter" href="/twittear/{{codigocan}}"><h2 class="centro">Compartir via twitter</h2></a><br>
<img src="/style/images/twitter1.png" class="twitter">
% end
</body>
</html>