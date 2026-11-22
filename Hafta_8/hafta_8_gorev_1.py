
def eposta_denetle(adres):
    # 1. Tam olarak bir '@' karakteri olmalı
    if adres.count("@") != 1:
        return "Tam olarak bir @ olmalı"

    # '@' konumunu find ile bulup kullanıcı adı ve alan adını dilimle ayırıyoruz
    at_konum = adres.find("@")
    kullanici = adres[:at_konum]
    alan = adres[at_konum + 1 :]

    # 2. Kullanıcı adı boş olmamalı ve yalnızca harf, rakam veya '.' içermeli
    if len(kullanici) == 0:
        return "Geçersiz karakter: kullanıcı adı boş"

    for ch in kullanici:
        if not (ch.isalnum() or ch == "."):
            return f"Geçersiz karakter: {ch}"

    # 3. Kullanıcı adı '.' ile başlayamaz veya bitemez
    if kullanici.startswith(".") or kullanici.endswith("."):
        return "Nokta ile başlayamaz/bitemez"

    # 4. Alan adında en az bir '.' olmalı ve '.' ile başlayıp bitmemeli
    if "." not in alan or alan.startswith(".") or alan.endswith("."):
        return "Alan adı hatalı"

    for ch in alan:
        if not (ch.isalnum() or ch == "."):
            return "Alan adı hatalı"

    return "Geçerli"


if __name__ == "__main__":
    print(eposta_denetle("ece.yilmaz@nisantasi.edu.tr"))
    print(eposta_denetle("ece@@mail.com"))
    print(eposta_denetle("ece yilmaz@mail.com"))
    print(eposta_denetle(".ece@mail.com"))
    print(eposta_denetle("ece@mail"))