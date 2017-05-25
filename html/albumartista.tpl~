<!DOCTYPE html>
<html lang="es">
<head>
<link rel="icon" type="image/png" href="/images/logovxt.png" />
<link rel="stylesheet" type="text/css" href="/style/album.css" />
<title>Albumes de {{nomartista}}</title>
</head>
<body>
<a title="VargaxTune" href="/inicio"><img src="/style/images/vargaxtunepeque.png" /></a>
<img src="/style/images/itunespeque.png">
% cont=0
<table>
% for album in listalbum:
	% if cont == 8:
	   <tr>
		<th><a title="{{album["codigo"]}}" href="/canciones/{{album["codigo"]}}"><h4>{{album["album"]}}</h4></a>
		<img src={{album["imagen"]}}>
		<h4>Artista: {{album["artista"]}}</h4>		
		</th>
		</tr>
		% cont=0
	% else:
		<th><a title="{{album["codigo"]}}" href="/canciones/{{album["codigo"]}}"><h4>{{album["album"]}}</h4></a>
		<img src={{album["imagen"]}}>
		<h4>Artista: {{album["artista"]}}</h4></th>
	% end
% cont=cont+1
% end
</table>
</body>
</html>