<!DOCTYPE html>
<html lang="es">
<head>
<link rel="stylesheet" type="text/css" href="/style/album.css" />
<title>Albumes {{album1}}</title>
</head>
<body>
% cont=0
<table>
% for album in listalbum:
	% if cont == 9:
		<tr>
		<th><h4>{{album["album"]}}</h4>
		<img src={{album["imagen"]}}></th>
		</tr>
		% cont=0
	% else:
		<th><h4>{{album["album"]}}</h4>
		<img src={{album["imagen"]}}></th>
	% end
% cont=cont+1
% end
</table>
</body>
</html>