git clone https://github.com/yakubilik/newsletter.git

docker build -t newsletter .

docker run --rm -p 5000:5000 newsletter

go to http://localhost:5000/home

to add news at the menu bar click ADD 

login as admin 

admin credentials: email = "yakupkeskin777@gmail.com" password = "admin"

give it a title, content and image url.

for have 100 news from api click fresh button at the menu.
