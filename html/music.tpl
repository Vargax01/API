<!DOCTYPE html>
<html lang="es">
<head>
<link rel="stylesheet" type="text/css" href="/style/canciones.css" />
<title>Canciones {{para1}}</title>
</head>
<body>
<a title="VargaxTune" href="/inicio"><img src="/style/images/vargaxtunepeque.png" /></a>
<img src="/style/images/itunespeque.png"><br>
<table>
<tr>
	<th></th>
	<th><h2 class="gris">Cancion</h2></th>
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
	<th><h2 class="gris">Escuchála</h2></th>
	</th>
	</tr>
% for cancion in listacan:	
   <tr>
   <th><img src={{cancion["imagen"]}} /></th>
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
	<h3 class="azul"><b>{{cancion["artista"]}}</b></h3>
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
	<th><audio src={{cancion["media"]}} controls></audio></th>
	<th><a title="{{cancion["codigo"]}}" href="/correo/{{cancion["codigo"]}}"><img src="/style/images/like1.png" /></a></th>
	</tr>	
% end
</table>
</div>
</body>
</html>