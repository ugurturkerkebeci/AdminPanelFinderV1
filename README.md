<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f3f4f6;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        p {
            color: #666;
            text-align: center;
        }
        input[type="text"] {
            width: calc(100% - 20px);
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin-bottom: 10px;
        }
        .success {
            color: #4CAF50;
        }
        .error {
            color: #f44336;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Admin Panel Bulucu</h1>
        <p>Belirtilen URL'de yönetim panelini bulmak için anahtar kelimeleri tara.</p>
        <input type="text" id="urlInput" placeholder="Tarama yapılacak URL">
        <button onclick="startScan()">Tara</button>
        <ul id="results"></ul>
    </div>

    <script>
        function startScan() {
            var url = document.getElementById("urlInput").value;
            if (!url) {
                alert("Lütfen bir URL girin.");
                return;
            }
            document.getElementById("results").innerHTML = "";
            var keywords = ["admin", "panel", "login", "administrator"]; // Anahtar kelimeler burada tanımlanabilir
            var results = document.getElementById("results");
            keywords.forEach(function(keyword) {
                var fullUrl = url + "/" + keyword;
                var li = document.createElement("li");
                li.innerText = "Deneniyor: " + fullUrl;
                results.appendChild(li);
                fetch(fullUrl, { method: "GET", mode: "no-cors" })
                    .then(function(response) {
                        if (response.status === 200) {
                            li.classList.add("success");
                            li.innerText += " - Aktif";
                        } else {
                            li.classList.add("error");
                            li.innerText += " - Deaktif";
                        }
                    })
                    .catch(function(error) {
                        li.classList.add("error");
                        li.innerText += " - İstek hatası";
                    });
            });
        }
    </script>
</body>
</html>
