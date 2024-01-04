# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------------------------
# Copyright (c) 2023,2024 The beep-projects contributors
# this file originated from https://github.com/beep-projects
# Do not remove the lines above.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see https://www.gnu.org/licenses/
# -------------------------------------------------------------------------------------------------

"""Module to hold the internationalization string for bmconnect.py

Supported language codes are stored in text_lang:
  "de","en","es","fr","it","pl","ru","tr"
text is a dictionary holding the translations in dictionaries like
  "text_id": {
    "de": "text_german",
    "en": "text_english",
    "es": "text_spanish",
    "fr": "text_french",
    "it": "text_italian",
    "pl": "text_polish",
    "ru": "text_russian",
    "tr": "text_turkish"
  }
"""

text_lang = ["de", "en", "es", "fr", "it", "pl", "ru", "tr"]

text = {
    "Blood pressure value category": {
        "de": "Bereich der Blutdruckwerte",
        "en": "Blood pressure value category",
        "es": "Rango de los valores de la presión arterial",
        "fr": "Plage des valeurs de tension",
        "it": "Intervallo dei valori di pressione",
        "pl": "Zakres wartości ciśnienia",
        "ru": "Диапазон значений кровяного давления",
        "tr": "Tansiyon değerlerinin aralığı",
    },
    "Systole": {
        "de": "Systole",
        "en": "Systole",
        "es": "Sístole",
        "fr": "Systole",
        "it": "Sistole",
        "pl": "Ciśnienie skurczowe",
        "ru": "Систолическое давление",
        "tr": "Sistol",
    },
    "Diastole": {
        "de": "Diastole",
        "en": "Diastole",
        "es": "Diástole",
        "fr": "Diastole",
        "it": "Diastole",
        "pl": "Ciśnienie rozkurczowe",
        "ru": "Диастолическое давление",
        "tr": "Diyastol",
    },
    "Recommendation": {
        "de": "Empf.",
        "en": "Recom.",
        "es": "Recom.",
        "fr": "Recom.",
        "it": "Raccom.",
        "pl": "Rekom.",
        "ru": "Реком.",
        "tr": "Öneri",
    },
    "severe hypertension": {
        "de": "starke Hypertonie",
        "en": "severe hypertension",
        "es": "hipertensión elevada",
        "fr": "forte hypertonie",
        "it": "forte ipertensione",
        "pl": "wysokie nadciśnienie",
        "ru": "тяжелая гипертония",
        "tr": "Şiddetli hipertansiyon",
    },
    "moderate hypertension": {
        "de": "mittlere Hypertonie",
        "en": "moderate hypertension",
        "es": "hipertensión media",
        "fr": "hypertonie moyenne",
        "it": "moderata ipertensione",
        "pl": "średnie nadciśnienie",
        "ru": "пограничная гипертония",
        "tr": "Orta şiddette hipertansiyon",
    },
    "mild hypertension": {
        "de": "leichte Hypertonie",
        "en": "mild hypertension",
        "es": "hipertensión leve",
        "fr": "légère hypertonie",
        "it": "leggera ipertensione",
        "pl": "lekkie nadciśnienie",
        "ru": "слабая степень гипертонии",
        "tr": "Hafif hipertansiyon",
    },
    "high normal": {
        "de": "hoch normal",
        "en": "high normal",
        "es": "Normal alta",
        "fr": "Normale haute",
        "it": "Normale alto",
        "pl": "Normalne wysokie",
        "ru": "Высокое в допустимых пределах",
        "tr": "Yüksek normal",
    },
    "normal": {
        "de": "normal",
        "en": "normal",
        "es": "Normal",
        "fr": "Normale",
        "it": "Normale",
        "pl": "Normalne",
        "ru": "Нормальное",
        "tr": "Normal",
    },
    "optimal": {
        "de": "optimal",
        "en": "optimal",
        "es": "Ideal",
        "fr": "Optimale",
        "it": "Ottimale",
        "pl": "Optymalne",
        "ru": "Оптимальное",
        "tr": "İdeal",
    },
    "hypotension": {
        "de": "Hypotonie",
        "en": "hypotension",
        "es": "Hipotensión",
        "fr": "Hypotonie",
        "it": "Ipotensione",
        "pl": "Niedociśnienie",
        "ru": "Гипотония",
        "tr": "Hipotansiyon",
    },
    "arrhythmia recognized": {
        "de": "Arrythmie erkannt! ",
        "en": "Arrythmia recognized!",
        "es": "¡Arritmia reconocida!",
        "fr": "Arrythmie détectée !",
        "it": "Aritmia riconosciuta!",
        "pl": "Arytmia rozpoznana!",
        "ru": "Аритмия признана!",
        "tr": "Aritmi fark edildi!",
    },
    "seek medical attention": {
        "de": "einen Arzt aufsuchen",
        "en": "seek medical attention",
        "es": "Consulte a su médico",
        "fr": "consulter un médecin",
        "it": "Rivolgersi a un medico",
        "pl": "Udaj się do lekarza",
        "ru": "Обращение к врачу",
        "tr": "Bir doktora başvurun",
    },
    "regular monitoring by doctor": {
        "de": "regelmäßige Kontrolle beim Arzt",
        "en": "regular monitoring by doctor",
        "es": "Sométase a revisio- nes periódicas en la consulta de su médico",
        "fr": "examen régulier par un médecin",
        "it": "Controlli medici regolari",
        "pl": "Regularna kontrola lekarska",
        "ru": "Регулярное посещение врача",
        "tr": "Düzenli doktor kontrolü",
    },
    "self-monitoring": {
        "de": "Selbstkontrolle",
        "en": "self-monitoring",
        "es": "Haga un seguimiento por su cuenta",
        "fr": "Auto-contrôle",
        "it": "Autocontrollo",
        "pl": "Samodzielna kontrola",
        "ru": "Самоконтроль",
        "tr": "Kendi kendine kontrol",
    },
    "error_no_credentials": {
        "de": (
            "Es sind keine Anmeldedaten für die Anmeldung bei Garmin Connect festgelegt. Führen Sie"
            " das Programm erneut mit der Option --login aus, um die Anmeldedaten manuell"
            " einzugeben."
        ),
        "en": (
            "No credentials for login to Garmin Connect are set. Run again with --login option, to"
            " enter the credentials manually."
        ),
        "es": (
            "No se han establecido credenciales para iniciar sesión en Garmin Connect. Vuelve a"
            " ejecutarlo con la opción --login para introducir las credenciales manualmente."
        ),
        "fr": (
            "Aucun identifiant de connexion à Garmin Connect n'est défini. Exécutez à nouveau le"
            " programme avec l'option --login, pour saisir manuellement les informations"
            " d'identification."
        ),
        "it": (
            "Non sono state impostate le credenziali di accesso a Garmin Connect. Eseguire"
            " nuovamente l'operazione con l'opzione --login, per inserire manualmente le"
            " credenziali."
        ),
        "pl": (
            "Nie ustawiono danych logowania do serwisu Garmin Connect. Uruchom ponownie z opcją"
            " --login, aby ręcznie wprowadzić dane uwierzytelniające."
        ),
        "ru": (
            "Не заданы учетные данные для входа в Garmin Connect. Повторите запуск с параметром"
            " --login, чтобы ввести учетные данные вручную."
        ),
        "tr": (
            "Garmin Connect'e giriş için kimlik bilgileri ayarlanmamıştır. Kimlik bilgilerini"
            " manuel olarak girmek için --login seçeneği ile tekrar çalıştırın."
        ),
    },
    "info_login_success_as": {
        "de": "Anmeldung erfolgreich als",
        "en": "Login successful as",
        "es": "Inicio de sesión con éxito como",
        "fr": "Connexion réussie comme",
        "it": "Accesso riuscito come",
        "pl": "Logowanie powiodło się jako",
        "ru": "Вход в систему успешный, так как",
        "tr": "Giriş başarılı olarak",
    },
    "info_garmin_email": {
        "de": "Email-Adresse",
        "en": "Email Address",
        "es": "Dirección de correo electrónico",
        "fr": "Adresse électronique",
        "it": "Indirizzo e-mail",
        "pl": "Adres e-mail",
        "ru": "Адрес электронной почты",
        "tr": "E-posta Adresi",
    },
    "info_garmin_password": {
        "de": "Passwort",
        "en": "Password",
        "es": "Contraseña",
        "fr": "Mot de passe",
        "it": "Password",
        "pl": "Hasło",
        "ru": "Пароль",
        "tr": "Parola",
    },
    "info_upload_note": {
        "de": "von bmconnect eingetragen",
        "en": "entered by bmconnect",
        "es": "introducido por bmconnect",
        "fr": "inscrit par bmconnect",
        "it": "inserito da bmconnect",
        "pl": "wpisany przez bmconnect",
        "ru": "введено bmconnect",
        "tr": "bmconnect tarafından girildi",
    },
    "info_risk": {
        "de": "Risiko",
        "en": "Risk",
        "es": "Riesgo",
        "fr": "Riesgo",
        "it": "Il rischio",
        "pl": "Ryzyko",
        "ru": "Риск",
        "tr": "Risk",
    },
    "info_searching_device": {
        "de": "Suche nach einem Beurer-Gerät",
        "en": "Searching for a Beurer device",
        "es": "Búsqueda de un dispositivo Beurer",
        "fr": "Recherche d'un appareil Beurer",
        "it": "Ricerca di un dispositivo Beurer",
        "pl": "Wyszukiwanie urządzenia Beurer",
        "ru": "Поиск устройства Брейера",
        "tr": "Bir Beurer cihazı arayın",
    },
    "info_connected": {
        "de": "Verbindung hergestellt zu",
        "en": "Connection established to",
        "es": "Conexión establecida con",
        "fr": "Connexion établie avec",
        "it": "Connessione stabilita a",
        "pl": "Połączenie nawiązane z",
        "ru": "Установлено соединение с",
        "tr": "Bağlantı kuruldu",
    },
    "info_could_not_ping_device": {
        "de": "Gerät gefunden, aber Verbindung fehlgeschlagen",
        "en": "Found a device, but connection failed",
        "es": "Dispositivo encontrado, pero falla la conexión",
        "fr": "Appareil trouvé, mais connexion échouée",
        "it": "Dispositivo trovato, ma connessione fallita",
        "pl": "Znaleziono urządzenie, ale połączenie nie powiodło się",
        "ru": "Устройство найдено, но соединение не удалось",
        "tr": "Cihaz bulundu, ancak bağlantı başarısız oldu",
    },
    "info_device_not_found": {
        "de": "Kein Gerät gefunden",
        "en": "No device found",
        "es": "No se ha encontrado ningún dispositivo",
        "fr": "Aucun appareil trouvé",
        "it": "Nessun dispositivo trovato",
        "pl": "Nie znaleziono urządzenia",
        "ru": "УУстройство не найдено",
        "tr": "Cihaz bulunamadı",
    },
    "info_trying_gc_login": {
        "de": "Versuche Login bei Garmin Connect mit gespeichertem Token von",
        "en": "Trying to log into Garmin Connect with saved token from",
        "es": "Intenta iniciar sesión en Garmin Connect con un token guardado de",
        "fr": "Essaye de te connecter à Garmin Connect avec le jeton enregistré de",
        "it": "Tenta di accedere a Garmin Connect con un token salvato da",
        "pl": (
            "Próbuje zalogować się do serwisu Garmin Connect przy użyciu tokena zapisanego w"
            " aplikacji"
        ),
        "ru": "Попытка войти в Garmin Connect с сохраненным маркером из",
        "tr": "'den kaydedilmiş bir belirteç ile Garmin Connect'te oturum açmaya çalışır",
    },
    "info_login_failed_trying_email_pw": {
        "de": "Anmeldung fehlgeschlagen, versuche E-Mail und Passwort zu verwenden",
        "en": "Login failed, try to use e-mail and password",
        "es": "Error de inicio de sesión, intente utilizar el correo electrónico y la contraseña",
        "fr": "Échec de la connexion, essaie d'utiliser l'e-mail et le mot de passe",
        "it": "Accesso fallito, provare a usare email e password",
        "pl": "Logowanie nie powiodło się, spróbuj użyć adresu e-mail i hasła",
        "ru": "Вход в систему не удался, попробуйте использовать электронную почту и пароль",
        "tr": "Giriş başarısız oldu, e-posta ve şifre kullanmayı deneyin",
    },
    "info_login_success": {
        "de": "Login erfolgreich",
        "en": "Login successful",
        "es": "Inicio de sesión correcto",
        "fr": "Connexion réussie",
        "it": "Accesso riuscito",
        "pl": "Logowanie powiodło się",
        "ru": "Вход в систему успешный",
        "tr": "Giriş başarılı",
    },
    "info_measurements_read": {
        "de": "Messungen vom Gerät gelesen",
        "en": "Measurements read from the device",
        "es": "Medidas leídas en el aparato",
        "fr": "mesures lues par l'appareil",
        "it": "Misure lette dal dispositivo",
        "pl": "Pomiary odczytane z urządzenia",
        "ru": "Измерения, считанные с прибора",
        "tr": "Cihazdan okunan ölçümler",
    },
    "info_measurements_uploaded": {
        "de": "Messungen zu Garmin Connect hochgeladen",
        "en": "measurements uploaded to Garmin Connect",
        "es": "mediciones cargadas en Garmin Connect",
        "fr": "mesures téléchargées sur Garmin Connect",
        "it": "misurazioni caricate su Garmin Connect",
        "pl": "pomiarów przesłanych do Garmin Connect",
        "ru": "измерений, загруженных в Garmin Connect",
        "tr": "ölçüm Garmin Connect'e yüklendi",
    },
    "text_id": {
        "de": "text_german",
        "en": "text_english",
        "es": "text_spanish",
        "fr": "text_french",
        "it": "text_italian",
        "pl": "text_polish",
        "ru": "text_russian",
        "tr": "text_turkish",
    },
}
