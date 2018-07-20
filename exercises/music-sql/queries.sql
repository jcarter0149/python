-- Query all of the entries in the Genre table
select * from Genre

-- Using the INSERT statement, add one of your favorite artists to the Artist table.
INSERT into Artist(ArtistName, YearEstablished)
Values("The Dead South", 2014)

-- Using the INSERT statement, add one, or more, albums by your artist to the Album table.
insert into album
select null, 'Good Company', '4/26/2014', 2000, 'Curve Music', artist.artistid, genre.genreid
from artist, Genre
Where artist.Artistname = 'The Dead South'
AND genre.label = 'Bluegrass'

-- Using the INSERT statement, add some songs that are on that album to the Song table.
insert into song
select null, 'Good Company', 243, '4/26/2014', genre.genreid, artist.Artistid, album.albumid
from artist, Genre, Album
Where artist.Artistname = 'The Dead South'
AND genre.label = 'Bluegrass'
AND album.title = 'Good Company'

-- Write a SELECT query that provides the song titles, album title, and artist name for all of the data you just entered in. Use the LEFT JOIN keyword sequence to connect the tables, and the WHERE keyword to filter the results to the album and artist you added.
SELECT a.Title as AlbumTitle, s.Title as SongName, art.ArtistName
FROM Album a
JOIN Song s, Artist art
ON s.AlbumId = a.AlbumId
WHERE artistName = "The Dead South"

-- Write a SELECT statement to display how many songs exist for each album. You'll need to use the COUNT() function and the GROUP BY keyword sequence.