book_info = (
("Best Mystery & Thriller","The Silent Patient",68821),
("Best Horror","The Institute",75717),
("Best History & Biography","The five",31783 ),
("Best Fiction","The Testaments",98291)
)

for i in book_info:
    (award,name,vote_count)=i
    print(name," won the '",award,"' catagory with ",vote_count," votes",sep="")