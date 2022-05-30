English steps
To launch this app you need to install Python in your computer, you can donwload it from the official webiste https://www.python.org/downloads/.

Also is needed to install some packages:
* pip install pyttsx3
* pip install SpeechRecognition
* pip install AVMSpeechMath
* pip install pywhatkit==5
* pip install requests
* pip install PyAudio

-Note:
    If you are running this software in Linux OS you will get some error with the last package.
    
Fix:
* pip install pipwin
* pipwin install pyaudio
* sudo apt-get install libasound-dev portaudio 19-dev libportaudio2 libportaudiocpp0
* pip install pyaudio --user

-Note:
    If you are running this software in Windows OS you will get some error with the last package.
    
Fix:
* Type "python" in cmd to check your python version
* Look for that version in https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
* For example if you python version is '3.10.4' and win32 socket you should download PyAudio-0.2.1-cp310-cp310-win_amd64.whl
* Then go into the folder where this file has been downloaded and execute -> pip install <name_of_donwloaded_file>

Also you will need to install MySQL to be able to use DataBase features
* https://dev.mysql.com/downloads/installer/

Once you have everything installed, then you can run the app by command line -> python main.py

Video demostration: https://youtu.be/qExY1cDqw4k


Pasos en Español

Para ejecutar esta aplicación es necesario tener instalado Python en el ordenador donde se vaya a hacer uso de la misma.
Se puede descargar Python desde su sitio web oficial https://www.python.org/downloads/.

Es necesario instalar algunos paquetes:
* pip install pyttsx3
* pip install SpeechRecognition
* pip install AVMSpeechMath
* pip install pywhatkit==5
* pip install requests
* pip install PyAudio

-Nota:
    Si estás ejecutando la aplicación en un SO Linux encontrarás algunos errores con el último paquete.
    
Solución:
* pip install pipwin
* pipwin install pyaudio
* sudo apt-get install libasound-dev portaudio 19-dev libportaudio2 libportaudiocpp0
* pip install pyaudio --user

-Nota:
    Si estás ejecutando la aplicación en un SO Windows encontrarás algunos errores con el último paquete.
    
Solución:
* Escribe "python" en la consola para verificar tu versión
* Busca tu versión en -> https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
* Por ejemplo si tu versión de python es la '3.10.4' y socket win32 tendrías que descargar PyAudio-0.2.1-cp310-cp310-win_amd64.whl
* Una vez descargado, navega a la carpeta donde esté descargado y ejecuta el siguiente comando -> pip install <nombre_del_archivo_descargado>

También necesitarás descargar MySQL para las funcionalidades relacionadas con la base de datos
* https://dev.mysql.com/downloads/installer/

Una vez todo instalado, puedes ejecutar la aplicación con el siguiente comando -> python main.py

Video demostración: https://youtu.be/qExY1cDqw4k
