<!DOCTYPE html>
<html lang="es">
<head>
<link rel="stylesheet" type="text/css" href="/style/canciones.css" />
<title>{{nomalbum}}</title>
</head>
<body>
<a title="VargaxTune" href="/inicio"><img src="/style/images/vargaxtunepeque.png" /></a>
<img src="/style/images/itunespeque.png"><br>
<div class="div1">
<h1>{{nomalbum}}</h1>
<img src={{img}} width="150" height="150"/>
</div>
<table>
<tr>
	<th><h2 class="azul">Cancion</h2></th>
	<th></th>
	<th></th>	
	<th></th>
	<th></th>
	<th></th>	
	<th></th>
	<th></th>
	<th></th>	
	<th></th>
		<th></th>
	<th></th>	
	<th></th>
	<th></th>
	<th></th>	
	<th></th>
	<th></th>
	<th></th>	
	<th></th>
	<th>
	<h2 class="gris">Artista</h2>
	</th>
		<th></th>
	<th></th>	
	<th></th>
	<th></th>
	<th></th>	
	<th></th>
	<th></th>
	<th></th>	
	<th></th>
		<th></th>
	<th></th>	
	<th></th>
	<th></th>
	<th></th>	
	<th></th>
	<th></th>
	<th></th>	
	<th></th>
	<th><h2 class="azul">Escuchála</h2></th>
	</th>
	</tr>
% for cancion in listacanc:
   <tr>
	<th><h3 class="azul"><b>{{cancion["nombre"]}}</b></h3></th>
	<th></th>
	<th></th>	
	<th></th>
	<th></th>
	<th></th>	
	<th></th>
	<th></th>
	<th></th>	
	<th></th>
		<th></th>
	<th></th>	
	<th></th>
	<th></th>
	<th></th>	
	<th></th>
	<th></th>
	<th></th>	
	<th></th>
	<th>
	<h3 class="gris"><b>{{cancion["artista"]}}</b></h3>
	</th>
		<th></th>
	<th></th>	
	<th></th>
	<th></th>
	<th></th>	
	<th></th>
	<th></th>
	<th></th>	
	<th></th>
		<th></th>
	<th></th>	
	<th></th>
	<th></th>
	<th></th>	
	<th></th>
	<th></th>
	<th></th>	
	<th></th>
	<th><h3 class="azul"><b>{{cancion["media"]}}</b></h3></th>
	</tr>
	<br>
% end
</table>
</body>
</html>