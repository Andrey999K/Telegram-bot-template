# Telegram bot template

***

### Установка  
Для установки требуется **[python 3.11](https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe)**  
```
pip install -r requirements.txt
```

***

### Запуск  

```
python bot.py
```  

### Файлы

**bot.py** — файл для запуска telegram-бота  

**config.py** — файл с токеном телеграм бота и прочими параметрами  
  
**requirements.txt** — файл со всеми сторонними библиотеками  

***

### Папки

**handlers** — папка с файлами, содержащими обработчики для различных команд и событий бота  

  * **collbacks.py** — обработчики coolback
  * **text.py** — обработчики текста
  * **command.py** — обработчики команд  
  
**utils** — папка с файлами, содержащими переменные, функции и классы  

  * **decorators.py** — функции декораторы
  * **function.py** — прочие функции
  * **variables.py** — переменные  
  
