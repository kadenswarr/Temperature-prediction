@ECHO OFF

cmd /k "C:\Users\Kaden\a_weather_project\weathervenv\Scripts\activate & cd /d	C:\Users\Kaden\a_weather_project\weatherdata_grabber & scrapy crawl daily -o weather_data.csv"
