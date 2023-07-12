# Ağ Tarayıcı Programı

Bu program, belirli bir IP adresi aralığında veya belirli bir IP adresindeki açık portları taramak için kullanılan bir ağ tarayıcıdır.

## Özellikler

- Otomatik ağ tarayıcısı: Belirli bir IP adresi bloğunda (örneğin, 192.168.1.0/24) bulunan tüm cihazları tarar.
- Manuel IP adresi tarayıcısı: Belirli bir hedef IP adresindeki açık portları tarar.
- Port tarama: Belirli bir başlangıç ve bitiş portu arasındaki tüm portları tarar.
- Tarama sonuçlarını kaydetme: Tarayıcı sonuçlarını TXT dosyasına kaydederek daha sonra kontrol etme imkanı sağlar.

## Kullanım

1. Programı çalıştırın ve aşağıdaki seçeneklerden birini seçin:
   - Otomatik ağ tarayıcısı (1)
   - Manuel IP adresi tarayıcısı (2)
2. Program size gerekli bilgileri soracak:
   - Başlangıç portunu girin
   - Bitiş portunu girin
   veya
   - Tarayacağınız hedef IP adresini girin
   - Başlangıç portunu girin
   - Bitiş portunu girin
3. Tarayıcı sonuçları, programın çalıştığı klasöre `network_scan.txt` veya `manual_scan.txt` dosyasına kaydedilecektir.
4. Tarama tamamlandığında, program kapanacaktır. Ayrıca, "Ctrl+C" tuş kombinasyonuna bastığınızda program normal şekilde kapatılacaktır.

---

## Lisans

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Bu projeyi [MIT Lisansı](https://opensource.org/licenses/MIT) altında lisansladık. Lisansın tam açıklamasını burada bulabilirsiniz.
