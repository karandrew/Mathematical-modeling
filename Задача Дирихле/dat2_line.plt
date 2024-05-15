unset surface
set contour
set view map
set cntrparam levels discrete 0.1, 0.2, 0.3 , 0.4, 0.5, 0.6, 0.7, 0.8, 0.9
splot "data2.txt" with lines
