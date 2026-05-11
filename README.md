# Proje Adı

vbl1

## Proje Hakkında

Bu proje, çeşitli Python modüllerinden oluşan bir yazılım uygulamasıdır. Projede agent ve asistan dosyaları ile, front-end tarafında ise HTML dosyaları ile kullanıcı ara yüzleri oluşturulmuştur.

## Kurulum

Projeyi çalıştırmak için gereksinim dosyasındakı paketlerin kurulması gerekmektedir. Bunun için:

```
pip install -r requirements.txt
```

komutunu çalıştırarak gerekli tüm bağımlılıkları yükleyebilirsiniz.

## Kullanım

Proje, arka planda `app.py`, `agent.py`, `asistan.py` ve `llm.py` Python dosyaları ve ön yüzde `frontend` klasöründeki HTML dosyaları ile çalışmaktadır. Her bir bileşen spesifik işlemler için tasarlanmıştır.

## Agent Tools

The agent can use the `get_datetime` tool to read the backend server's current date and time. The tool returns a JSON-style response with `current_datetime`, `date`, and `time` fields.

## Katkıda Bulunma

Katkıda bulunmak isteyenler standart bir pull request süreci üzerinden projeye katkıda bulunabilirler.

## Lisans

Bu projeye ait lisans bilgileri burada yer alacaktır.
