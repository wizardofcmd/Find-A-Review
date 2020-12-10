import requests

resp = requests.get("https://findabookapp.herokuapp.com/api/book/read.php")
book_data = resp.json
print(resp)
