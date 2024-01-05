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
    "help_help": {
        "de": "Zeigt diese Hilfe an und beendet bmconnect.",
        "en": "Shows this help message and exits bmconnect.",
        "es": "Muestra este mensaje de ayuda y sale.",
        "fr": "Affiche ce message d'aide et quitte.",
        "it": "Mostra questo messaggio di aiuto ed esce.",
        "pl": "Wyświetla komunikat pomocy i kończy działanie.",
        "ru": "Выводит сообщение о помощи и завершает работу.",
        "tr": "Bu yardım mesajını gösterir ve çıkar.",
    },
    "help_login": {
        "de": (
            "Konfiguriert die Anmeldedaten für das Garmin Connect-Konto und testet sie. Sollte"
            " zusammen mit der Option --user verwendet werden, sonsten werden die"
            " Anmeldeinformationen für den Standardbenutzer festgelegt. Diese Option wird"
            " abgespeichert."
        ),
        "en": (
            "Configures the login credentials for the Garmin Connect account and tests them. Should"
            " be used together with the --user option, otherwise the credentials for the default"
            " user will be set. This option is saved."
        ),
        "es": (
            "Configura las credenciales de inicio de sesión para la cuenta de Garmin Connect y las"
            " prueba. Debe utilizarse junto con la opción --user; de lo contrario, se establecerán"
            " las credenciales para el usuario predeterminado. Esta opción se guarda."
        ),
        "fr": (
            "Configure et teste les informations de connexion pour le compte Garmin Connect. Doit"
            " être utilisée avec l'option --user, sinon les informations de connexion sont définies"
            " pour l'utilisateur standard. Cette option est enregistrée."
        ),
        "it": (
            "Configura le credenziali di accesso per l'account Garmin Connect e le verifica. Deve"
            " essere usato insieme all'opzione --user, altrimenti verranno impostate le credenziali"
            " per l'utente predefinito. Questa opzione viene salvata."
        ),
        "pl": (
            "Konfiguruje poświadczenia logowania dla konta Garmin Connect i testuje je. Powinna być"
            " używana razem z opcją --user, w przeciwnym razie zostaną ustawione poświadczenia dla"
            " domyślnego użytkownika. Ta opcja jest zapisywana."
        ),
        "ru": (
            "Настраивает учетные данные для входа в учетную запись Garmin Connect и проверяет их."
            " Следует использовать вместе с параметром --user, иначе будут установлены учетные"
            " данные для пользователя по умолчанию. Этот параметр сохраняется."
        ),
        "tr": (
            "Garmin Connect hesabı için oturum açma kimlik bilgilerini yapılandırır ve test eder."
            " --user seçeneği ile birlikte kullanılmalıdır, aksi takdirde varsayılan kullanıcı için"
            " kimlik bilgileri ayarlanacaktır. Bu seçenek kaydedilir."
        ),
    },
    "help_user": {
        "de": (
            "Legt den aktiven Benutzer des Beurer-Geräts fest, dessen Messungen auf Garmin Connect"
            " hochgeladen werden sollen. Der Standardwert ist --default_user, wenn er nicht gesetzt"
            " ist."
        ),
        "en": (
            "Configures the active user from the Beurer device whose measurements shall be uploaded"
            " to Garmin Connect. Defaults to --default_user if not set."
        ),
        "es": (
            "Configura el usuario activo del dispositivo Beurer cuyas mediciones se cargarán en"
            " Garmin Connect. El valor predeterminado es --default_user si no se establece."
        ),
        "fr": (
            "Configure l'utilisateur actif de l'appareil Beurer dont les mesures seront"
            " téléchargées sur Garmin Connect. La valeur par défaut est --default_user si elle"
            " n'est pas définie."
        ),
        "it": (
            "Configura l'utente attivo del dispositivo Beurer le cui misurazioni devono essere"
            " caricate su Garmin Connect. Se non è impostato, il valore predefinito è"
            " --default_user."
        ),
        "pl": (
            "Konfiguruje aktywnego użytkownika z urządzenia Beurer, którego pomiary będą przesyłane"
            " do serwisu Garmin Connect. Domyślnie --default_user, jeśli nie ustawiono."
        ),
        "ru": (
            "Настраивает активного пользователя с устройства Beurer, чьи измерения будут"
            " загружаться в Garmin Connect. По умолчанию --default_user, если не задано."
        ),
        "tr": (
            "Beurer cihazından ölçümleri Garmin Connect'e yüklenecek olan aktif kullanıcıyı"
            " yapılandırır. Ayarlanmamışsa --default_user olarak varsayılır."
        ),
    },
    "help_default_user": {
        "de": (
            "Legt den Standardbenutzer des Beurer-Geräts fest, dessen Messungen auf Garmin Connect"
            " hochgeladen werden sollen, wenn --user nicht angegeben wird. Der Standardwert ist 1,"
            " wenn er nicht gesetzt ist. Diese Option wird gespeichert."
        ),
        "en": (
            "Configure the default user from the Beurer device whose measurements shall be uploaded"
            " to Garmin Connect if --user is not given. Defaults to 1 if not set. This option is"
            " persisted."
        ),
        "es": (
            "Configura el usuario predeterminado del dispositivo Beurer cuyas mediciones se"
            " cargarán en Garmin Connect si no se indica --user. El valor predeterminado es 1 si no"
            " se establece. Esta opción se guarda."
        ),
        "fr": (
            "Configure l'utilisateur par défaut de l'appareil Beurer dont les mesures seront"
            " téléchargées sur Garmin Connect si --user n'est pas indiqué. La valeur par défaut est"
            " 1 si elle n'est pas définie. Cette option est sauvegardée."
        ),
        "it": (
            "Configura l'utente predefinito del dispositivo Beurer le cui misurazioni saranno"
            " caricate su Garmin Connect se --user non viene indicato. L'impostazione predefinita è"
            " 1 se non è stata impostata. Questa opzione viene salvata."
        ),
        "pl": (
            "Konfiguruje domyślnego użytkownika z urządzenia Beurer, którego pomiary będą"
            " przesyłane do serwisu Garmin Connect, jeśli nie podano opcji --user. Domyślnie 1,"
            " jeśli nie ustawiono. Ta opcja jest zapisywana."
        ),
        "ru": (
            "Настраивает пользователя по умолчанию с устройства Beurer, чьи измерения будут"
            " загружаться в Garmin Connect, если параметр --user не задан. По умолчанию принимает"
            " значение 1, если не задано. Этот параметр сохраняется."
        ),
        "tr": (
            "Eğer --user belirtilmemişse, ölçümleri Garmin Connect'e yüklenecek olan Beurer"
            " cihazındaki varsayılan kullanıcıyı yapılandırır. Ayarlanmamışsa varsayılan değer"
            " 1'dir. Bu seçenek kaydedilir."
        ),
    },
    "help_ignore": {
        "de": (
            "Weist bmconnect an, die in den Messungen gespeicherte Benutzerkennung zu ignorieren."
            " Wird für Geräte benötigt, die keine Benutzer-ID in den Messwerten unterstützen, aber"
            " mehrere Benutzer auf dem Gerät zur Auswahl haben."
        ),
        "en": (
            "Tells bmconnect to ignore the user id stored in the measurements. Needed for devices,"
            " that do not support user id in the readouts, but have multiple users on the device"
            " for selection."
        ),
        "es": (
            "Indica a bmconnect que ignore el identificador de usuario almacenado en las"
            " mediciones. Necesario para dispositivos que no admiten ID de usuario en las lecturas,"
            " pero que tienen varios usuarios en el dispositivo para su selección."
        ),
        "fr": (
            "Indique à bmconnect d'ignorer l'identifiant de l'utilisateur stocké dans les mesures."
            " Nécessaire pour les appareils qui ne supportent pas l'identifiant de l'utilisateur"
            " dans les relevés, mais qui ont plusieurs utilisateurs sur l'appareil pour la"
            " sélection."
        ),
        "it": (
            "Indica a bmconnect di ignorare l'id utente memorizzato nelle misurazioni. Necessario"
            " per i dispositivi che non supportano l'id utente nelle letture, ma che hanno più"
            " utenti sul dispositivo per la selezione."
        ),
        "pl": (
            "Mówi bmconnect, aby ignorował identyfikator użytkownika przechowywany w pomiarach."
            " Wymagane w przypadku urządzeń, które nie obsługują identyfikatora użytkownika w"
            " odczytach, ale mają wielu użytkowników na urządzeniu do wyboru."
        ),
        "ru": (
            "Указывает bmconnect игнорировать идентификатор пользователя, хранящийся в измерениях."
            " Необходим для устройств, которые не поддерживают идентификатор пользователя в"
            " показаниях, но имеют несколько пользователей на устройстве для выбора."
        ),
        "tr": (
            "bmconnect'e ölçümlerde saklanan kullanıcı kimliğini göz ardı etmesini söyler."
            " Okumalarda kullanıcı kimliğini desteklemeyen, ancak seçim için cihazda birden fazla"
            " kullanıcı bulunan cihazlar için gereklidir."
        ),
    },
    "help_language": {
        "de": (
            "Konfiguriert die von bmconnect verwendete Sprache. Insbesondere für Messungsnotizen,"
            " die auf Garmin Connect hochgeladen werden. Diese Option wird gespeichert."
        ),
        "en": (
            "Configures the language used by bmconnect. Especially for measurement notes uploaded"
            " to Garmin Connect. This option is saved."
        ),
        "es": (
            "Configura el idioma utilizado por bmconnect. Especialmente para las notas de medición"
            " cargadas en Garmin Connect. Esta opción se guarda."
        ),
        "fr": (
            "Configure la langue utilisée par bmconnect. Notamment pour les notes de mesure"
            " téléchargées sur Garmin Connect. Cette option est sauvegardée."
        ),
        "it": (
            "Configura la lingua utilizzata da bmconnect. In particolare per le note di misurazione"
            " caricate su Garmin Connect. Questa opzione viene salvata."
        ),
        "pl": (
            "Konfiguruje język używany przez bmconnect. Dotyczy to zwłaszcza notatek z pomiarów"
            " przesyłanych do serwisu Garmin Connect. Ta opcja jest zapisywana."
        ),
        "ru": (
            "Настройка языка, используемого bmconnect. Особенно для заметок об измерениях,"
            " загружаемых в Garmin Connect. Этот параметр сохраняется."
        ),
        "tr": (
            "bmconnect tarafından kullanılan dili yapılandırır. Özellikle Garmin Connect'e yüklenen"
            " ölçüm notları için. Bu seçenek kaydedilir."
        ),
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
