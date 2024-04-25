<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
   
    
</head>
<body>
    <h1>Admin Panel Bulucu Uygulaması</h1>
    <p>Admin paneli bulucu bir Python uygulamasıdır. Bu program, belirli bir URL üzerinde belirtilen anahtar kelimeleri kullanarak potansiyel admin panellerini taramak için tasarlandı.</p>
    <h2>Nasıl Çalışır?</h2>
    <ul>
        <li>Kullanıcı, taranacak URL'yi girdikten sonra program, bir dosyadan alınan anahtar kelimeleri kullanarak tarama işlemini gerçekleştirir.</li>
        <li>Her anahtar kelime için ayrı bir iş parçacığı oluşturulur ve belirli bir admin paneli URL'sini denemek için istek gönderilir.</li>
        <li>İstek sonucuna bağlı olarak, her bir URL'nin aktif veya pasif olduğu belirlenir ve sonuçlar ekrana yazdırılır.</li>
    </ul>
    <h2>Kullanılan Teknolojiler</h2>
    <ul>
        <li><code>requests</code> kütüphanesi: HTTP istekleri göndermek için kullanıldı.</li>
        <li><code>threading</code> modülü: Eş zamanlı olarak çoklu anahtar kelime taraması yapmak için kullanıldı.</li>
        <li><code>colorama</code> kütüphanesi: Renkli çıktılar için kullanıldı, böylece sonuçlar daha okunabilir hale getirildi.</li>
    </ul>
    <p>Bu uygulamanın amacı, web uygulamalarında güvenlik açıklarını tespit etmeye yardımcı olmaktadır. Ancak, herhangi bir web sitesinde yetkisiz tarama yapmak yasa dışı olabilir ve izin almadan yapılması etik değildir. Bu nedenle, bu tür araçları sadece meşru ve etiketli bir şekilde kullanmalısınız.</p>
</body>
</html>
