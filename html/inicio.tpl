<!DOCTYPE html>
<html lang="es">
<head>
<link rel="icon" type="image/png" href="/images/logovxt.png" />
<link rel="stylesheet" type="text/css" href="/style/sytle.css" />
<meta charset="utf-8">
<title>VargaxTune</title>
</head>
<body>
<div class="div1">
  <img src="style/images/vargaxtune.png"><br>
  <img src="style/images/itunes.png">
</div>
<div class="div2">
<form id="formulario" action="inicio" method="post">
<table>
<tr>
<th></th>
<th><h2>Nombre Canción, Album o Artista</h2></th>
<th></th>
</tr>
<tr>
<th></th>
<th><input type="text" name="nombre"/></th>
<th></th>
</tr>
<tr>
<th></th>
<th><h2>Buscar por</h2></th>
<th></th>
</tr>
<tr>
<th></th>
<th>
<select id="tipo" name="tipo">
 <option value="" selected="seleccion">--Categoría--</option>
 <option value="artista">Artista</option>
 <option value="cancion">Canción</option>
 <option value="album">Album</option> 
 </select>
</th>
<th></th>
</tr>
</table>
<input type="submit" name="buscar" value="Buscar" class="buscar" />
</form>
% if cont == 1:
	<h3>Conectado con</h3>
	<img src="style/images/logotw1.png" />
		<a href="/twitter_logout"><h3>Desconectar</h3></a>
% else:
	<a href="{{authorize_url}}"><h3>Conectar con Twitter</h3></a>
% end
</div>
</body>
</html>