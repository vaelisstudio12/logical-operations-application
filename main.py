import webview
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_path(filename):
    return os.path.join(BASE_DIR, filename)

def init_files():
    files = {
        "index.html": """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Kesikli Matematik Motoru</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div class="bar">
            <a href="#" class="system-btn" onclick="minimize_window()">
                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 16 16">
                    <path d="M1 10L1 6L15 6V10L1 10Z"></path>
                </svg>
            </a>

            <a href="#" class="system-btn close-btn" onclick="close_window()">
                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 50 50">
                    <path d="M 9.15625 6.3125 L 6.3125 9.15625 L 22.15625 25 L 6.21875 40.96875 L 9.03125 43.78125 L 25 27.84375 L 40.9375 43.78125 L 43.78125 40.9375 L 27.84375 25 L 43.6875 9.15625 L 40.84375 6.3125 L 25 22.15625 Z"></path>
                </svg>
            </a>
        </div>

        <div style="padding: 20px;">
            <h2>Kesikli Matematik - Kompleks Önerme Motoru</h2>
            
            <!-- Değerler Kümesi Tanımlama Alanı -->
            <fieldset style="border: 2px solid aqua; padding: 15px; margin-bottom: 20px; border-radius: 8px;">
                <legend style="padding: 0 5px; font-weight: bold;">Önerme Değerleri Kümesi</legend>
                <div id="kumelerAlani" style="margin-bottom: 10px;">
                    <div style="margin-bottom: 8px;">
                        <input type="text" class="kume-anahtar" value="p" placeholder="p" style="border: 1px solid aqua; padding: 4px; width: 60px; text-align: center; background: #000; color: aqua;" oninput="comboboxlariGuncelle()"> = 
                        <select class="kume-deger" style="border: 1px solid aqua; padding: 4px; background: #000; color: aqua;">
                            <option value="true">Doğru (True)</option>
                            <option value="false">Yanlış (False)</option>
                        </select>
                        <button type="button" class="neon-btn" style="width: 50px; height: 30px; border-radius: 4px; font-size: 12px;" onclick="kumeSatirSil(this)">Sil</button>
                    </div>
                    <div style="margin-bottom: 8px;">
                        <input type="text" class="kume-anahtar" value="q" placeholder="q" style="border: 1px solid aqua; padding: 4px; width: 60px; text-align: center; background: #000; color: aqua;" oninput="comboboxlariGuncelle()"> = 
                        <select class="kume-deger" style="border: 1px solid aqua; padding: 4px; background: #000; color: aqua;">
                            <option value="true">Doğru (True)</option>
                            <option value="false" selected>Yanlış (False)</option>
                        </select>
                        <button type="button" class="neon-btn" style="width: 50px; height: 30px; border-radius: 4px; font-size: 12px;" onclick="kumeSatirSil(this)">Sil</button>
                    </div>
                </div>
                <button type="button" class="neon-btn" style="width: 140px; height: 35px; border-radius: 6px; font-size: 13px;" onclick="kumeSatirEkle()">Değişken Ekle</button>
            </fieldset>

            <!-- Kompleks Önerme Tablosu -->
            <table border="1" id="mathTable" style="border-collapse: collapse; border-color: aqua; width: 100%; margin-bottom: 15px; text-align: center;">
                <thead>
                    <tr style="height: 35px;">
                        <th>1. Bileşen</th>
                        <th>Bağlaç</th>
                        <th>2. Bileşen</th>
                        <th>Hesapla</th>
                        <th>Çıktı</th>
                        <th>İşlem</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="height: 40px;">
                        <td>
                            <select class="ifade-select-1" style="border: 1px solid aqua; padding: 4px; background: #000; color: aqua; width: 110px;"></select>
                        </td>
                        <td>
                            <select class="op-select" style="border: 1px solid aqua; padding: 4px; background: #000; color: aqua;">
                                <option value="AND">Ve (∧)</option>
                                <option value="OR">Veya (∨)</option>
                                <option value="XOR">Özel Veya (⊻)</option>
                                <option value="IMPLIES">İse (⇒)</option>
                                <option value="BICONDITIONAL">Ancak ve Ancak (⇔)</option>
                                <option value="NAND">Nand (⊼)</option>
                                <option value="NOR">Nor (⊽)</option>
                                <option value="XNOR">Xnor (⇔ Değil)</option>
                            </select>
                        </td>
                        <td>
                            <select class="ifade-select-2" style="border: 1px solid aqua; padding: 4px; background: #000; color: aqua; width: 110px;"></select>
                        </td>
                        <td>
                            <button type="button" class="neon-btn" style="width: 70px; height: 30px; border-radius: 4px; font-size: 12px;" onclick="satirHesapla(this)">Hesapla</button>
                        </td>
                        <td>
                            <span class="cikti-alani" style="font-weight: bold; text-shadow: 0 0 8px aqua; color: aqua;">-</span>
                        </td>
                        <td>
                            <button type="button" class="neon-btn" style="width: 50px; height: 30px; border-radius: 4px; font-size: 12px;" onclick="ifadeSatirSil(this)">Sil</button>
                        </td>
                    </tr>
                </tbody>
            </table>

            <div style="margin-bottom: 20px;">
                <button type="button" class="neon-btn" style="width: 140px; height: 35px; border-radius: 6px; font-size: 13px;" onclick="ifadeSatirEkle()">İfade Satırı Ekle</button>
            </div>
        </div>

        <script src="main.js" type="text/javascript"></script>
    </body>
</html>
""",
        "style.css": """* {
    background-color: #000000;
    color:aqua
}

.system-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
    border: 2px solid aqua;
    color: aqua; 
    text-decoration: none;
    border-radius: 4px;
    transition: all 0.2s ease;
    cursor: pointer;
}

.system-btn:hover {
    transition: all 0.2s ease;
    color: #000000;
    background: aqua;
    box-shadow: 0 0 5px aqua, 0 0 25px aqua, 0 0 50px aqua;
}
.bar {
    margin: 0 10px;
    justify-content: flex-end;
    display: flex;
}

.neon-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 100px;
    height: 40px;
    border: 2px solid aqua;
    color:aqua; 
    text-decoration: none;
    border-radius: 15px;
    transition: all 0.2s ease;
    cursor: pointer;
}

.neon-btn:hover {
    transition: all 0.2s ease;
    color:  #000000;
    background: aqua;
    box-shadow: 0 0 5px aqua, 0 0 15px aqua, 0 0 50px aqua;
}

.system-btn svg {
    background-color: transparent; 
    fill: aqua;
    transition: all 0.2s ease;
}

.system-btn:hover svg {
    fill: #000;
    background-color: transparent;
    transition: all 0.2s ease;
}

.neon-btn svg {
    background-color: transparent; 
    fill: aqua;
    transition: all 0.2s ease;
}

.neon-btn:hover svg {
    fill: #000;
    background-color: transparent;
    transition: all 0.2s ease;
}""",
        "main.js": """const minimize_window = () => pywebview.api.minimize_window();
const close_window = () => pywebview.api.close_window();

function comboboxlariGuncelle() {
    const anahtarlar = document.getElementsByClassName("kume-anahtar");
    let temelSecenekler = [];

    for (let i = 0; i < anahtarlar.length; i++) {
        let val = anahtarlar[i].value.trim();
        if (val) {
            temelSecenekler.push(val);
            temelSecenekler.push("~" + val);
        }
    }

    const select1s = document.getElementsByClassName("ifade-select-1");
    const select2s = document.getElementsByClassName("ifade-select-2");

    updateSelectOptions(select1s, temelSecenekler);
    updateSelectOptions(select2s, temelSecenekler);
}

function updateSelectOptions(selects, optionsList) {
    for (let i = 0; i < selects.length; i++) {
        let select = selects[i];
        let seciliDeger = select.value;

        select.innerHTML = "";
        
        let currentRowIndex = i + 1;
        let genisletilmisListe = [...optionsList];
        for (let r = 1; r < currentRowIndex; r++) {
            genisletilmisListe.push("Satır " + r);
        }

        genisletilmisListe.forEach(item => {
            let opt = document.createElement("option");
            opt.value = item;
            opt.text = item;
            if (item === seciliDeger) {
                opt.selected = true;
            }
            select.appendChild(opt);
        });
    }
}

function kumeSatirEkle() {
    const container = document.getElementById("kumelerAlani");
    const div = document.createElement("div");
    div.style.marginBottom = "8px";
    div.innerHTML = `
        <input type="text" class="kume-anahtar" placeholder="değişken" style="border: 1px solid aqua; padding: 4px; width: 60px; text-align: center; background: #000; color: aqua;" oninput="comboboxlariGuncelle()"> = 
        <select class="kume-deger" style="border: 1px solid aqua; padding: 4px; background: #000; color: aqua;">
            <option value="true">Doğru (True)</option>
            <option value="false">Yanlış (False)</option>
        </select>
        <button type="button" class="neon-btn" style="width: 50px; height: 30px; border-radius: 4px; font-size: 12px;" onclick="kumeSatirSil(this)">Sil</button>
    `;
    container.appendChild(div);
    comboboxlariGuncelle();
}

function kumeSatirSil(button) {
    button.parentNode.remove();
    comboboxlariGuncelle();
}

function ifadeSatirEkle() {
    const table = document.getElementById("mathTable").getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();
    newRow.style.height = "40px";
    
    newRow.innerHTML = `
        <td>
            <select class="ifade-select-1" style="border: 1px solid aqua; padding: 4px; background: #000; color: aqua; width: 110px;"></select>
        </td>
        <td>
            <select class="op-select" style="border: 1px solid aqua; padding: 4px; background: #000; color: aqua;">
                <option value="AND">Ve (∧)</option>
                <option value="OR">Veya (∨)</option>
                <option value="XOR">Özel Veya (⊻)</option>
                <option value="IMPLIES">İse (⇒)</option>
                <option value="BICONDITIONAL">Ancak ve Ancak (⇔)</option>
                <option value="NAND">Nand (⊼)</option>
                <option value="NOR">Nor (⊽)</option>
                <option value="XNOR">Xnor (⇔ Değil)</option>
            </select>
        </td>
        <td>
            <select class="ifade-select-2" style="border: 1px solid aqua; padding: 4px; background: #000; color: aqua; width: 110px;"></select>
        </td>
        <td>
            <button type="button" class="neon-btn" style="width: 70px; height: 30px; border-radius: 4px; font-size: 12px;" onclick="satirHesapla(this)">Hesapla</button>
        </td>
        <td>
            <span class="cikti-alani" style="font-weight: bold; text-shadow: 0 0 8px aqua; color: aqua;">-</span>
        </td>
        <td>
            <button type="button" class="neon-btn" style="width: 50px; height: 30px; border-radius: 4px; font-size: 12px;" onclick="ifadeSatirSil(this)">Sil</button>
        </td>
    `;
    comboboxlariGuncelle();
}

function ifadeSatirSil(button) {
    const row = button.parentNode.parentNode;
    if (row.parentNode.rows.length > 1) {
        row.parentNode.removeChild(row);
        comboboxlariGuncelle();
    } else {
        alert("En az bir ifade satırı kalmalıdır!");
    }
}

function satirHesapla(button) {
    const row = button.parentNode.parentNode;
    const rows = Array.from(document.querySelectorAll("#mathTable tbody tr"));
    const rowIndex = rows.indexOf(row);

    let tumSatirlar = [];
    for (let i = 0; i <= rowIndex; i++) {
        let r = rows[i];
        tumSatirlar.push({
            p1: r.querySelector(".ifade-select-1").value,
            baglac: r.querySelector(".op-select").value,
            p2: r.querySelector(".ifade-select-2").value
        });
    }

    const anahtarlar = document.getElementsByClassName("kume-anahtar");
    const degerler = document.getElementsByClassName("kume-deger");
    let degerlerKumesi = {};

    for (let i = 0; i < anahtarlar.length; i++) {
        let anahtar = anahtarlar[i].value.trim();
        if (anahtar) {
            degerlerKumesi[anahtar] = (degerler[i].value === "true");
        }
    }

    pywebview.api.hesapla_kompleks_matematik(degerlerKumesi, tumSatirlar, rowIndex).then(response => {
        const ciktiSpan = row.querySelector(".cikti-alani");
        if (response.success) {
            let sonuc = response.sonuc;
            if (sonuc) {
                ciktiSpan.innerText = "True";
                ciktiSpan.style.color = "aqua";
                ciktiSpan.style.textShadow = "0 0 8px aqua, 0 0 20px aqua";
            } else {
                ciktiSpan.innerText = "False";
                ciktiSpan.style.color = "red";
                ciktiSpan.style.textShadow = "0 0 8px red, 0 0 20px red";
            }
        } else {
            ciktiSpan.innerText = "Hata";
            ciktiSpan.style.color = "yellow";
            ciktiSpan.style.textShadow = "0 0 8px yellow";
            alert(response.mesaj);
        }
    });
}

window.onload = function() {
    comboboxlariGuncelle();
};""",
    }
    for filename, content in files.items():
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)

init_files()

class Api:
    def close_window(self):
        window = webview.active_window()
        if window: window.destroy()
    
    def minimize_window(self):
        window = webview.active_window()
        if window: window.minimize()

    def ifade_degeri_cozumle(self, ifade, degerler_kumesi, satir_sonuclari):
        ifade = ifade.strip()
        
        if ifade.startswith("Satır "):
            try:
                satir_no = int(ifade.split(" ")[1])
                idx = satir_no - 1
                if idx in satir_sonuclari:
                    return satir_sonuclari[idx]
                else:
                    raise Exception(f"'{ifade}' henüz hesaplanmadı!")
            except Exception as e:
                raise Exception(f"Satır referansı çözümlenemedi: {e}")

        not_eki = False
        if ifade.startswith("~"):
            not_eki = True
            ifade = ifade[1:].strip()

        if ifade not in degerler_kumesi:
            raise Exception(f"'{ifade}' değişkeni değerler kümesinde tanımlı değil!")

        deger = degerler_kumesi[ifade]
        return (not deger) if not_eki else deger

    def hesapla_kompleks_matematik(self, degerler_kumesi, satirlar, hedef_index):
        try:
            satir_sonuclari = {}

            for i in range(hedef_index + 1):
                satir = satirlar[i]
                p1_str = satir["p1"]
                baglac = satir["baglac"]
                p2_str = satir["p2"]

                v1 = self.ifade_degeri_cozumle(p1_str, degerler_kumesi, satir_sonuclari)
                v2 = self.ifade_degeri_cozumle(p2_str, degerler_kumesi, satir_sonuclari)

                if baglac == "AND":
                    res = v1 and v2
                elif baglac == "OR":
                    res = v1 or v2
                elif baglac == "XOR":
                    res = v1 != v2
                elif baglac == "IMPLIES":
                    res = (not v1) or v2
                elif baglac == "BICONDITIONAL":
                    res = v1 == v2
                elif baglac == "NAND":
                    res = not (v1 and v2)
                elif baglac == "NOR":
                    res = not (v1 or v2)
                elif baglac == "XNOR":
                    res = v1 != v2 # XNOR (Equivalence negatifidir, v1 == v2 yerine v1 != v2 ters mantık veya v1 == v2'nin değili)
                else:
                    res = False
                
                # XNOR düzeltmesi: Karşılıklı koşulun değili (eşit değilse true, eşitse false) -> v1 != v2 eşdeğerliği
                if baglac == "XNOR":
                    res = v1 == v2

                satir_sonuclari[i] = res

            return {"success": True, "sonuc": satir_sonuclari[hedef_index]}
        except Exception as e:
            return {"success": False, "mesaj": str(e)}

api = Api()

def main():
    window = webview.create_window(
        title='Application', url='index.html',
        width=1900, height=1080, frameless=True, resizable=True, js_api=api
    )
    webview.start()

if __name__ == '__main__':
    main()