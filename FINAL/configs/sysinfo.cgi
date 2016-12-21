#!/bin/sh
echo "Content-type: text/html; charset=utf-8"
echo ""
echo ""
echo "<pre>"
echo "<b>"
echo "<br>"
echo "Адрес клиента:" $HTTP_X_REAL_IP
echo "Адрес порта:" $HTTP_X_REAL_PORT
echo "Адрес nginx:" $REMOTE_ADDR
echo "Порт nginx:" $REMOTE_PORT
echo "Версия nginx:" $HTTP_X_NGINX_VERSION
echo "</b>"
echo "<br>"
echo "<b>Средняя загрузка (LoadAverage)</b>"
echo "1min 5min 15min"
cat /proc/loadavg | awk -F ' ' '{print $1,$2,$3}'
echo "<br>"
echo "<b>Загрузка дисков (iostat)</b>"
iostat -xkd | awk 'NR>2 {print}'
echo "<br>"
echo "<b>Загрузка сети</b>"
cat /proc/net/dev
echo "<br>"
echo "<b>Top talkers по сети (сортировка по убыванию)</b>"

echo "<br>"
echo "<b>Статистика по сетевым соединениям</b>"
echo "TCP"
cat /proc/net/tcp
echo "UDP"
cat /proc/net/udp
echo "<br>"
echo "<b>Средняя загрузка CPU</b>"
mpstat | awk 'NR>2 {print}'
echo "<br>"
echo "<b>Информация о дисках</b>"
df
echo "<br>"
echo "<b>Дата:</b>"
date
echo "<br>"
echo "<pre>"
