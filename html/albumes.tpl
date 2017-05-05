<!DOCTYPE html>
<html lang="es">
<head>
<title>Albumes</title>
</head>
<body>
% for album in listalbum:
<h4>{{album["album"]}}</h4>
<img src={{album["imagen"]}}>
% end
</body>
</html>