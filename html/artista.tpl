<!DOCTYPE html>
<html lang="es">
<head>
<link rel="icon" type="image/png" href="/style/images/logovxt.png" />
<link rel="stylesheet" type="text/css" href="/style/artista.css" />
<title>Artista {{para1}}</title>
</head>
<body>
<a title="VargaxTune" href="/inicio"><img src="/style/images/vargaxtunepeque.png" /></a>
<img src="/style/images/itunespeque.png">
<table>
% for artista in listartista:
<a title="{{artista["codigo"]}}" href="/albumartista/{{artista["codigo"]}}"><h4>{{artista["artista"]}}</h4></a>	
% end
</table>
</body>
</html>