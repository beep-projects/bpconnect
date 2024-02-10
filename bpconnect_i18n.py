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

"""Module to hold the internationalization string for bpconnect.py

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
        "de": "von bpconnect eingetragen",
        "en": "entered by bpconnect",
        "es": "introducido por bpconnect",
        "fr": "inscrit par bpconnect",
        "it": "inserito da bpconnect",
        "pl": "wpisany przez bpconnect",
        "ru": "введено bpconnect",
        "tr": "bpconnect tarafından girildi",
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
    "info_found_credentials_in_config": {
        "de": "Anmeldeinformationen in der Konfigurationsdatei gefunden",
        "en": "Credentials found in config file",
        "es": "Credenciales encontradas en el archivo de configuración",
        "fr": "Informations d'identification trouvées dans le fichier de configuration",
        "it": "Credenziali trovate nel file di configurazione",
        "pl": "Poświadczenia znalezione w pliku konfiguracyjnym",
        "ru": "Учетные данные найдены в файле конфигурации",
        "tr": "Yapılandırma dosyasında kimlik bilgileri bulundu",
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
    "info_measurements_added": {
        "de": "Messungen hinzugefügt zu",
        "en": "measurements added to",
        "es": "medidas añadidas",
        "fr": "mesures ajoutées à",
        "it": "misure aggiunte",
        "pl": "pomiarów dodanych do",
        "ru": "измерений добавлено",
        "tr": "ölçüm eklendi",
    },
    "help_help": {
        "de": "Zeigt diese Hilfe an und beendet bpconnect.",
        "en": "Shows this help message and exits bpconnect.",
        "es": "Muestra este mensaje de ayuda y sale de bpconnect.",
        "fr": "Affiche ce message d'aide et quitte bpconnect.",
        "it": "Mostra questo messaggio di aiuto ed esce da bpconnect.",
        "pl": "Wyświetla ten komunikat pomocy i zamyka bpconnect.",
        "ru": "Выводит это справочное сообщение и завершает работу bpconnect.",
        "tr": "Bu yardım mesajını gösterir ve bpconnect'ten çıkar.",
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
    "help_offline": {
        "de": (
            "Deaktiviert die Synchronisierung mit einem Garmin Connect-Konto. Nützlich, wenn Du nur"
            " bpreport.py verwenden möchtest. Diese Option wird nicht gespeichert."
        ),
        "en": (
            "Deactivates synchronization with a Garmin Connect account. Useful if you only want to"
            " use bpreport.py. This option is not saved."
        ),
        "es": (
            "Desactiva la sincronización con una cuenta de Garmin Connect. Útil si sólo desea"
            " utilizar bpreport.py. Esta opción no se guarda."
        ),
        "fr": (
            "Désactive la synchronisation avec un compte Garmin Connect. Utile si tu ne veux"
            " utiliser que bpreport.py. Cette option n'est pas enregistrée."
        ),
        "it": (
            "Disattiva la sincronizzazione con un account Garmin Connect. Utile se si desidera"
            " utilizzare solo bpreport.py. Questa opzione non viene salvata."
        ),
        "pl": (
            "Dezaktywuje synchronizację z kontem Garmin Connect. Przydatne, jeśli chcesz używać"
            " tylko bpreport.py. Ta opcja nie jest zapisywana."
        ),
        "ru": (
            "Отключает синхронизацию с учетной записью Garmin Connect. Полезно, если вы хотите"
            " использовать только bpreport.py. Этот параметр не сохраняется."
        ),
        "tr": (
            "Garmin Connect hesabı ile senkronizasyonu devre dışı bırakır. Yalnızca bpreport.py"
            " kullanmak istiyorsanız kullanışlıdır. Bu seçenek kaydedilmez."
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
            " wenn er nicht gesetzt ist. Diese Option wird abgespeichert."
        ),
        "en": (
            "Configure the default user from the Beurer device whose measurements shall be uploaded"
            " to Garmin Connect if --user is not given. Defaults to 1 if not set. This option is"
            " saved."
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
            "Weist bpconnect an, die in den Messungen gespeicherte Benutzerkennung zu ignorieren."
            " Wird für Geräte benötigt, die keine Benutzer-ID in den Messwerten unterstützen, aber"
            " mehrere Benutzer auf dem Gerät zur Auswahl haben."
        ),
        "en": (
            "Tells bpconnect to ignore the user id stored in the measurements. Needed for devices,"
            " that do not support user id in the readouts, but have multiple users on the device"
            " for selection."
        ),
        "es": (
            "Indica a bpconnect que ignore el identificador de usuario almacenado en las"
            " mediciones. Necesario para dispositivos que no admiten ID de usuario en las lecturas,"
            " pero que tienen varios usuarios en el dispositivo para su selección."
        ),
        "fr": (
            "Indique à bpconnect d'ignorer l'identifiant de l'utilisateur stocké dans les mesures."
            " Nécessaire pour les appareils qui ne supportent pas l'identifiant de l'utilisateur"
            " dans les relevés, mais qui ont plusieurs utilisateurs sur l'appareil pour la"
            " sélection."
        ),
        "it": (
            "Indica a bpconnect di ignorare l'id utente memorizzato nelle misurazioni. Necessario"
            " per i dispositivi che non supportano l'id utente nelle letture, ma che hanno più"
            " utenti sul dispositivo per la selezione."
        ),
        "pl": (
            "Mówi bpconnect, aby ignorował identyfikator użytkownika przechowywany w pomiarach."
            " Wymagane w przypadku urządzeń, które nie obsługują identyfikatora użytkownika w"
            " odczytach, ale mają wielu użytkowników na urządzeniu do wyboru."
        ),
        "ru": (
            "Указывает bpconnect игнорировать идентификатор пользователя, хранящийся в измерениях."
            " Необходим для устройств, которые не поддерживают идентификатор пользователя в"
            " показаниях, но имеют несколько пользователей на устройстве для выбора."
        ),
        "tr": (
            "bpconnect'e ölçümlerde saklanan kullanıcı kimliğini göz ardı etmesini söyler."
            " Okumalarda kullanıcı kimliğini desteklemeyen, ancak seçim için cihazda birden fazla"
            " kullanıcı bulunan cihazlar için gereklidir."
        ),
    },
    "help_language": {
        "de": (
            "Konfiguriert die von bpconnect/bpreport verwendete Sprache. Diese Option wird"
            " gespeichert."
        ),
        "en": "Configures the language used by bpconnect/bpreport. This option is saved.",
        "es": "Configura el idioma utilizado por bpconnect/bpreport. Esta opción se guarda.",
        "fr": "Configure la langue utilisée par bpconnect/bpreport. Cette option est sauvegardée.",
        "it": "Configura la lingua utilizzata da bpconnect/bpreport. Questa opzione viene salvata.",
        "pl": "Konfiguruje język używany przez bpconnect/bpreport. Ta opcja jest zapisywana.",
        "ru": "Настройка языка, используемого bpconnect/bpreport. Этот параметр сохраняется.",
        "tr": "bpconnect/bpreport tarafından kullanılan dili yapılandırır. Bu seçenek kaydedilir.",
    },
    "help_save_locally": {
        "de": (
            "Speichert die gelesenen Daten lokal, um sie mit anderen Tools weiterverarbeiten zu"
            " können. Diese Option wird gespeichert."
        ),
        "en": (
            "Saves the read data locally so that it can be further processed with other tools. This"
            " option is saved."
        ),
        "es": (
            "Guarda localmente los datos leídos para poder procesarlos posteriormente con otras"
            " herramientas. Esta opción se guarda."
        ),
        "fr": (
            "Enregistre les données lues localement afin de pouvoir les traiter avec d'autres"
            " outils. Cette option est enregistrée."
        ),
        "it": (
            "Salva i dati letti localmente per poterli elaborare ulteriormente con altri strumenti."
            " Questa opzione viene salvata."
        ),
        "pl": (
            "Zapisuje odczytane dane lokalnie, aby można je było dalej przetwarzać za pomocą innych"
            " narzędzi. Ta opcja jest zapisywana."
        ),
        "ru": (
            "Сохраняет считанные данные локально, чтобы их можно было обработать другими"
            " инструментами. Эта опция сохраняется."
        ),
        "tr": (
            "Okunan verileri diğer araçlarla daha fazla işlenebilmesi için yerel olarak kaydeder."
            " Bu seçenek kaydedilir."
        ),
    },
    "help_dont_save_locally": {
        "de": (
            "Beendet das lokale Speichern der gelesenen Daten, falls zuvor mit --save_locally"
            " aktiviert worden war. Diese Option wird gespeichert."
        ),
        "en": (
            "Ends the local saving of the read data if it was previously activated with"
            " --save_locally. This option is saved."
        ),
        "es": (
            "Finaliza el guardado local de los datos leídos si se activó previamente con"
            " --save_locally. Esta opción se guarda."
        ),
        "fr": (
            "Arrête la sauvegarde locale des données lues, si elle a été activée auparavant avec"
            " --save_locally. Cette option est enregistrée."
        ),
        "it": (
            "Termina il salvataggio locale dei dati letti se è stato precedentemente attivato con"
            " --save_locally. Questa opzione viene salvata."
        ),
        "pl": (
            "Kończy lokalne zapisywanie odczytanych danych, jeśli zostało ono wcześniej aktywowane"
            " opcją --save_locally. Ta opcja jest zapisywana."
        ),
        "ru": (
            "Прекращает локальное сохранение прочитанных данных, если оно было ранее активировано с"
            " помощью опции --save_locally. Эта опция сохраняется."
        ),
        "tr": (
            "Daha önce --save_locally ile etkinleştirildiyse, okunan verilerin yerel olarak"
            " kaydedilmesini sonlandırır. Bu seçenek kaydedilir."
        ),
    },
    "help_name": {
        "de": (
            "Der Name der im erstellten Protokoll verwendet werden soll. Wird so ausgegeben, wie"
            " eingegeben."
        ),
        "en": "The name to be used in the generated report. Is output as entered.",
        "es": (
            "El nombre que se utilizará en el informe generado. Se emite tal y como se ha"
            " introducido."
        ),
        "fr": (
            "Le nom qui doit être utilisé dans le rapport généré. Il est édité tel qu'il a été"
            " saisi."
        ),
        "it": "Il nome da utilizzare nel rapporto generato. Viene emesso come inserito.",
        "pl": (
            "Nazwa, która zostanie użyta w wygenerowanym raporcie. Jest wyświetlana w takiej"
            " postaci, w jakiej została wprowadzona."
        ),
        "ru": (
            "Имя, которое будет использоваться в создаваемом отчете. Выводится в том виде, в"
            " котором введено."
        ),
        "tr": "Oluşturulan raporda kullanılacak ad. Girildiği gibi çıktı alınır.",
    },
    "help_birthday": {
        "de": (
            "Das Datum, welches als Geburtsdatum in dem erstellten Protokoll verwendet werden soll."
            " Das Datum muss in jedem gültigen ISO 8601-Format angegeben werden (z.B. 2021-06-11,"
            " 20210611, 2021-W23-5), ausgenommen Ordnungszahlen (z. B. 2021-162)"
        ),
        "en": (
            "The date to be used as the date of birth in the generated report. The date must be"
            " specified in any valid ISO 8601 format (e.g. 2021-06-11, 20210611, 2021-W23-5),"
            " except ordinal numbers (e.g. 2021-162)"
        ),
        "es": (
            "La fecha que se utilizará como fecha de nacimiento en el informe generado. La fecha"
            " debe especificarse en cualquier formato ISO 8601 válido (por ejemplo, 2021-06-11,"
            " 20210611, 2021-W23-5), excepto los números ordinales (por ejemplo, 2021-162)."
        ),
        "fr": (
            "La date qui doit être utilisée comme date de naissance dans le rapport généré. La date"
            " doit être indiquée dans n'importe quel format ISO 8601 valide (par exemple"
            " 2021-06-11, 20210611, 2021-W23-5), à l'exception des nombres ordinaux (par exemple"
            " 2021-162)."
        ),
        "it": (
            "La data da utilizzare come data di nascita nel report generato. La data deve essere"
            " specificata in qualsiasi formato ISO 8601 valido (ad es. 2021-06-11, 20210611,"
            " 2021-W23-5), ad eccezione dei numeri ordinali (ad es. 2021-162)."
        ),
        "pl": (
            "Data, która zostanie użyta jako data urodzenia w wygenerowanym raporcie. Data musi być"
            " określona w dowolnym prawidłowym formacie ISO 8601 (np. 2021-06-11, 20210611,"
            " 2021-W23-5), z wyjątkiem liczb porządkowych (np. 2021-162)."
        ),
        "ru": (
            "Дата, которая будет использоваться в качестве даты рождения в создаваемом отчете. Дата"
            " должна быть указана в любом допустимом формате ISO 8601 (например, 2021-06-11,"
            " 20210611, 2021-W23-5), за исключением порядковых номеров (например, 2021-162)."
        ),
        "tr": (
            "Oluşturulan raporda doğum tarihi olarak kullanılacak tarih. Tarih, sıra numaraları"
            " (örneğin 2021-162) hariç olmak üzere geçerli herhangi bir ISO 8601 formatında"
            " (örneğin 2021-06-11, 20210611, 2021-W23-5) belirtilmelidir"
        ),
    },
    "help_start_date": {
        "de": (
            "Startdatum des Protokollzeitraums, das in Verbindung mit --end_date verwendet wird, um"
            " den tatsächlichen Zeitraum anzugeben, für den das Protokoll erstellt wird. Das Datum"
            " muss in jedem gültigen ISO 8601-Format angegeben werden (z. B. 2021-06-11, 20210611,"
            " 2021-W23-5), ausgenommen Ordnungszahlen (z. B. 2021-162)"
        ),
        "en": (
            "Start date of the reporting period which is used in conjunction with --end_date to"
            " specify the actual period the report is generated for. The date must be specified in"
            " any valid ISO 8601 format (e.g. 2021-06-11, 20210611, 2021-W23-5), except ordinal"
            " numbers (e.g. 2021-162)"
        ),
        "es": (
            "Fecha de inicio del periodo del informe que se utiliza junto con --end_date para"
            " especificar el periodo real para el que se genera el informe. La fecha debe"
            " especificarse en cualquier formato ISO 8601 válido (por ejemplo, 2021-06-11,"
            " 20210611, 2021-W23-5), excepto los números ordinales (por ejemplo, 2021-162)."
        ),
        "fr": (
            "Date de début de la période de déclaration, utilisée conjointement avec --end_date"
            " pour spécifier la période réelle pour laquelle le rapport est généré. La date doit"
            " être spécifiée dans n'importe quel format ISO 8601 valide (par exemple 2021-06-11,"
            " 20210611, 2021-W23-5), à l'exception des nombres ordinaux (par exemple 2021-162)."
        ),
        "it": (
            "Data di inizio del periodo di rendicontazione, utilizzata insieme a --end_date per"
            " specificare il periodo effettivo per il quale viene generato il report. La data deve"
            " essere specificata in qualsiasi formato ISO 8601 valido (ad esempio, 2021-06-11,"
            " 20210611, 2021-W23-5), ad eccezione dei numeri ordinali (ad esempio, 2021-162)."
        ),
        "pl": (
            "Data rozpoczęcia okresu raportowania, która jest używana w połączeniu z --end_date w"
            " celu określenia rzeczywistego okresu, dla którego generowany jest raport. Data musi"
            " być określona w dowolnym prawidłowym formacie ISO 8601 (np. 2021-06-11, 20210611,"
            " 2021-W23-5), z wyjątkiem liczb porządkowych (np. 2021-162)."
        ),
        "ru": (
            "Дата начала отчетного периода, которая используется в сочетании с --end_date для"
            " указания фактического периода, за который формируется отчет. Дата должна быть указана"
            " в любом допустимом формате ISO 8601 (например, 2021-06-11, 20210611, 2021-W23-5),"
            " кроме порядковых номеров (например, 2021-162)."
        ),
        "tr": (
            "Raporun oluşturulduğu gerçek dönemi belirtmek için --end_date ile birlikte kullanılan"
            " raporlama döneminin başlangıç tarihi. Tarih, sıra numaraları (örneğin 2021-162)"
            " hariç, geçerli herhangi bir ISO 8601 biçiminde (örneğin 2021-06-11, 20210611,"
            " 2021-W23-5) belirtilmelidir"
        ),
    },
    "help_end_date": {
        "de": (
            "Enddatum des Protokollzeitraums, das in Verbindung mit --start_date verwendet wird, um"
            " den tatsächlichen Zeitraum anzugeben, für den das Protokoll erstellt wird. Das Datum"
            " muss in jedem gültigen ISO 8601-Format angegeben werden (z. B. 2021-06-11, 20210611,"
            " 2021-W23-5), ausgenommen Ordnungszahlen (z. B. 2021-162)"
        ),
        "en": (
            "End date of the reporting period which is used in conjunction with --start_date to"
            " specify the actual period the report is generated for. The date must be specified in"
            " any valid ISO 8601 format (e.g. 2021-06-11, 20210611, 2021-W23-5), except ordinal"
            " numbers (e.g. 2021-162)"
        ),
        "es": (
            "Fecha final del periodo del informe que se utiliza junto con --start_date para"
            " especificar el periodo real para el que se genera el informe. La fecha debe"
            " especificarse en cualquier formato ISO 8601 válido (por ejemplo, 2021-06-11,"
            " 20210611, 2021-W23-5), excepto los números ordinales (por ejemplo, 2021-162)."
        ),
        "fr": (
            "Date de fin de la période de déclaration, utilisée conjointement avec --start_date"
            " pour spécifier la période réelle pour laquelle le rapport est généré. La date doit"
            " être spécifiée dans n'importe quel format ISO 8601 valide (par exemple 2021-06-11,"
            " 20210611, 2021-W23-5), à l'exception des nombres ordinaux (par exemple 2021-162)."
        ),
        "it": (
            "Data di fine del periodo di rendicontazione, utilizzata insieme a --start_date per"
            " specificare il periodo effettivo per cui viene generato il report. La data deve"
            " essere specificata in qualsiasi formato ISO 8601 valido (ad esempio, 2021-06-11,"
            " 20210611, 2021-W23-5), ad eccezione dei numeri ordinali (ad esempio, 2021-162)."
        ),
        "pl": (
            "Data końcowa okresu raportowania, która jest używana w połączeniu z --start_date w"
            " celu określenia rzeczywistego okresu, dla którego generowany jest raport. Data musi"
            " być podana w dowolnym prawidłowym formacie ISO 8601 (np. 2021-06-11, 20210611,"
            " 2021-W23-5), z wyjątkiem liczb porządkowych (np. 2021-162)."
        ),
        "ru": (
            "Дата окончания отчетного периода, которая используется в сочетании с --start_date для"
            " указания фактического периода, за который формируется отчет. Дата должна быть указана"
            " в любом допустимом формате ISO 8601 (например, 2021-06-11, 20210611, 2021-W23-5),"
            " кроме порядковых номеров (например, 2021-162)."
        ),
        "tr": (
            "Raporun oluşturulduğu gerçek dönemi belirtmek için --start_date ile birlikte"
            " kullanılan raporlama döneminin bitiş tarihi. Tarih, sıra numaraları (örn. 2021-162)"
            " hariç, geçerli herhangi bir ISO 8601 biçiminde (örn. 2021-06-11, 20210611,"
            " 2021-W23-5) belirtilmelidir"
        ),
    },
    "help_gender": {
        "de": (
            "Das Geschlecht, welches in dem erstellten Protokoll verwendet werden soll. Freitext,"
            " such dir aus, wonach du dich fühlst."
        ),
        "en": "The gender to be used in the created report. Free text, choose what you feel like.",
        "es": (
            "El género que se utilizará en el informe creado. Texto libre, elija lo que le parezca."
        ),
        "fr": (
            "Le sexe qui doit être utilisé dans le rapport créé. Texte libre, choisissez ce que"
            " vous ressentez."
        ),
        "it": (
            "Il genere da utilizzare nel rapporto creato. Testo libero, scegliere quello che si"
            " ritiene opportuno."
        ),
        "pl": (
            "Płeć, która zostanie użyta w utworzonym raporcie. Dowolny tekst, wybierz to, na co"
            " masz ochotę."
        ),
        "ru": (
            "Пол, который будет использоваться в созданном отчете. Свободный текст, выберите то,"
            " что считаете нужным."
        ),
        "tr": "Oluşturulan raporda kullanılacak cinsiyet. Serbest metin, ne hissettiğinizi seçin.",
    },
    "plot_label_frequency": {
        "de": "Häufigkeit",
        "en": "Frequency",
        "es": "Frecuencia",
        "fr": "Fréquence",
        "it": "Frequenza",
        "pl": "Częstotliwość",
        "ru": "Частота",
        "tr": "Frekans",
    },
    "plot_title_risk_index_hist": {
        "de": "Anzahl Messungen pro Klassifizierung",
        "en": "Readings per Classification",
        "es": "Número de medidas por clasificación",
        "fr": "Nombre de mesures par classification",
        "it": "Numero di misure per classificazione",
        "pl": "Liczba pomiarów na klasyfikację",
        "ru": "Количество измерений для каждой классификации",
        "tr": "Sınıflandırma başına ölçüm sayısı",
    },
    "plot_label_diastolic": {
        "de": "diastolisch",
        "en": "diastolic",
        "es": "diastólica",
        "fr": "diastolique",
        "it": "diastolico",
        "pl": "diastolisch",
        "ru": "диастолический",
        "tr": "diyastolik",
    },
    "plot_label_systolic": {
        "de": "systolisch",
        "en": "systolic",
        "es": "sistólica",
        "fr": "systolique",
        "it": "sistolico",
        "pl": "systolisch",
        "ru": "систолический",
        "tr": "sistolik",
    },
    "plot_label_pulse_pressure": {
        "de": "Pulsdruck",
        "en": "pulse pressure",
        "es": "presión de pulso",
        "fr": "pression pulsée",
        "it": "pressione arteriosa differenziale",
        "pl": "ciśnienie tętna",
        "ru": "лульсовое давление",
        "tr": "nabız basıncı",
    },
    "plot_title_bp_classification": {
        "de": "Klassifizierung",
        "en": "Classification",
        "es": "Clasificación",
        "fr": "Classification",
        "it": "Classificazione",
        "pl": "Klasyfikacja",
        "ru": "Классификация",
        "tr": "Sınıflandırması",
    },
    "plot_label_pressure": {
        "de": "Druck (mmHg)",
        "en": "Pressure (mmHg)",
        "es": "Tensión (mmHg)",
        "fr": "Pression (mmHg)",
        "it": "Pressione (mmHg)",
        "pl": "Ciśnienie (mmHg)",
        "ru": "Давление (мм рт. ст.)",
        "tr": "Basınç (mmHg)",
    },
    "plot_label_percentage": {
        "de": "Prozent (%)",
        "en": "Percentage (%)",
        "es": "Porcentaje (%)",
        "fr": "Pourcentage (%)",
        "it": "Percentuale (%)",
        "pl": "Procent (%)",
        "ru": "Процент (%)",
        "tr": "Yüzde (%)",
    },
    "plot_title_bp_distribution": {
        "de": "Verteilung",
        "en": "Distribution",
        "es": "Distribución",
        "fr": "Distribution",
        "it": "Distribuzione",
        "pl": "Rozkład",
        "ru": "Распределение артериального давления",
        "tr": "Dağılımı",
    },
    "template_meta_content": {
        "de": "Blutdruck-Protokoll",
        "en": "Blood Pressure Report",
        "es": "Informe sobre la tensión arterial",
        "fr": "Rapport sur la tension artérielle",
        "it": "Rapporto sulla pressione sanguigna",
        "pl": "Raport dotyczący ciśnienia krwi",
        "ru": "Рассылка",
        "tr": "Kan Basıncı Raporu",
    },
    "template_document_title": {
        "de": "Blutdruck-Protokoll",
        "en": "Blood Pressure Report",
        "es": "Informe sobre la tensión arterial",
        "fr": "Rapport sur la tension artérielle",
        "it": "Rapporto sulla pressione sanguigna",
        "pl": "Raport dotyczący ciśnienia krwi",
        "ru": "Отчет о кровяном давлении",
        "tr": "Kan Basıncı Raporu",
    },
    "template_disclaimer": {
        "de": (
            "Die angegebene Klassifizierung basiert auf Daten der International Society of"
            " Hypertension (ISH). Die gesundheitsbezogenen Daten sind nicht für medizinische Zwecke"
            " bestimmt und dienen auch nicht der Diagnose, Heilung oder Vorbeugung von Krankheiten"
            " oder Zuständen."
        ),
        "en": (
            "The given classification is based on data from the International Society of"
            " Hypertension (ISH). Health-related data is not intended to be used for medical"
            " purposes, nor is it intended to diagnose, cure or prevent any disease or condition."
        ),
        "es": (
            "La clasificación dada se basa en datos de la International Society of Hypertension"
            " (ISH). Los datos relacionados con la salud no están destinados a ser utilizados con"
            " fines médicos, ni a diagnosticar, curar o prevenir ninguna enfermedad o afección."
        ),
        "fr": (
            "La classification donnée est basée sur les données de l'International Society of"
            " Hypertension (ISH). Les données relatives à la santé ne sont pas destinées à être"
            " utilisées à des fins médicales, ni à diagnostiquer, guérir ou prévenir une maladie ou"
            " un état."
        ),
        "it": (
            "La classificazione fornita si basa sui dati della International Society of"
            " Hypertension (ISH). I dati relativi alla salute non sono destinati a essere"
            " utilizzati per scopi medici, né a diagnosticare, curare o prevenire alcuna malattia o"
            " condizione."
        ),
        "pl": (
            "Podana klasyfikacja opiera się na danych International Society of Hypertension (ISH)."
            " Dane dotyczące zdrowia nie są przeznaczone do celów medycznych ani do diagnozowania,"
            " leczenia lub zapobiegania jakimkolwiek chorobom lub stanom."
        ),
        "ru": (
            "Приведенная классификация основана на данных International Society of Hypertension"
            " (ISH). Данные о здоровье не предназначены для использования в медицинских целях, а"
            " также для диагностики, лечения или профилактики каких-либо заболеваний или состояний."
        ),
        "tr": (
            "Verilen sınıflandırma International Society of Hypertension (ISH) verilerine"
            " dayanmaktadır. Sağlıkla ilgili verilerin tıbbi amaçlarla kullanılması amaçlanmadığı"
            " gibi herhangi bir hastalığı veya durumu teşhis etmek, iyileştirmek veya önlemek için"
            " de tasarlanmamıştır."
        ),
    },
    "template_section_title_measurements": {
        "de": "Messungen",
        "en": "Measurements",
        "es": "Medidas",
        "fr": "Mesures",
        "it": "Misure",
        "pl": "Pomiary",
        "ru": "Измерения",
        "tr": "Ölçümler",
    },
    "template_table_header_time": {
        "de": "Uhrzeit",
        "en": "Time",
        "es": "Hora del día",
        "fr": "Heure",
        "it": "Ora del giorno",
        "pl": "Pora dnia",
        "ru": "Время суток",
        "tr": "Günün saati",
    },
    "template_table_header_measurement": {
        "de": "Messung",
        "en": "Measurement",
        "es": "Medida",
        "fr": "Mesure",
        "it": "Misurazione",
        "pl": "Pomiar",
        "ru": "Измерение",
        "tr": "Ölçüm",
    },
    "template_table_header_pulse_pressure": {
        "de": "Pulsdruck",
        "en": "Pulse Pressure",
        "es": "Presión de pulso",
        "fr": "Pression pulsée",
        "it": "Pressione arteriosa differenziale",
        "pl": "Ciśnienie tętna",
        "ru": "Пульсовое давление",
        "tr": "Nabız basıncı",
    },
    "template_table_header_pulse": {
        "de": "Puls",
        "en": "Pulse",
        "es": "Pulso",
        "fr": "Pouls",
        "it": "Impulso",
        "pl": "Puls",
        "ru": "Импульс",
        "tr": "Nabız",
    },
    "template_table_header_classification": {
        "de": "Klassifizierung",
        "en": "Classification",
        "es": "Clasificación",
        "fr": "Classification",
        "it": "Classificazione",
        "pl": "Klasyfikacja",
        "ru": "Классификация",
        "tr": "Sınıflandırma",
    },
    "template_table_header_notes": {
        "de": "Notizen",
        "en": "Notes",
        "es": "Notas",
        "fr": "Notas",
        "it": "Note",
        "pl": "Uwagi",
        "ru": "Примечания",
        "tr": "Notlar",
    },
    "template_document_footer_date": {
        "de": "erstellt mit bpreport am",
        "en": "created with bpreport on",
        "es": "creado con bpreport en",
        "fr": "créé avec bpreport le",
        "it": "creato con bpreport su",
        "pl": "utworzony za pomocą bpreport on",
        "ru": "созданный с помощью bpreport на",
        "tr": "tarihinde bpreport ile oluşturulmuştur",
    },
    "template_abbrev_years": {
        "de": "J.",
        "en": "yrs",
        "es": "años)",
        "fr": "ans",
        "it": "anni",
        "pl": "lata",
        "ru": "Лет",
        "tr": "yıl",
    },
    "plot_title_bp_measurement_series": {
        "de": "Tägliche Durchschnittswerte",
        "en": "Daily Averages",
        "es": "Medias diarias",
        "fr": "Moyennes journalières",
        "it": "Medie giornaliere",
        "pl": "Średnie dzienne",
        "ru": "Средние дневные значения",
        "tr": "Günlük Ortalamalar",
    },
    "plot_title_2hour_average": {
        "de": "2-Stunden-Durchschnitt",
        "en": "2-Hour Average",
        "es": "Media de 2 horas",
        "fr": "Moyenne sur 2 heures",
        "it": "Media di 2 ore",
        "pl": "Średnia 2-godzinna",
        "ru": "2-часовое среднее",
        "tr": "2-Saatlik Ortalama",
    },
    "plot_label_date": {
        "de": "Datum",
        "en": "Date",
        "es": "Fecha",
        "fr": "Date",
        "it": "Data",
        "pl": "Data",
        "ru": "Дата",
        "tr": "Tarih",
    },
    "plot_label_time": {
        "de": "Uhrzeit",
        "en": "Time of day",
        "es": "Hora del día",
        "fr": "Hora del día",
        "it": "Ora del giorno",
        "pl": "Pora dnia",
        "ru": "Время дня",
        "tr": "Günün saati",
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
