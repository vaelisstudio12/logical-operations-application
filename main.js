const minimize_window = () => pywebview.api.minimize_window();
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
};