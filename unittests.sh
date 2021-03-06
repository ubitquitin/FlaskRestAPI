#!/bin/bash
SERVER=ec2-13-58-211-147.us-east-2.compute.amazonaws.com
PORT=5000

mysql -h localhost --user=ec2-user --password=Toragpwns96 < ./RestData.sql
echo " "
echo "curl -X GET http://$SERVER:$PORT/"
curl -X GET http://$SERVER:$PORT/
echo " "
echo "curl -X POST http://$SERVER:$PORT/restaurants/BostonMarket"
curl -X POST http://$SERVER:$PORT/restaurants/BostonMarket
echo " "
echo "curl -X POST http://$SERVER:$PORT/restaurants/NafNaf"
curl -X POST http://$SERVER:$PORT/restaurants/NafNaf
echo " "
echo "curl -X POST http://$SERVER:$PORT/restaurants/Chipotle"
curl -X POST http://$SERVER:$PORT/restaurants/Chipotle
echo " "
echo "curl -X POST http://$SERVER:$PORT/restaurants/McDonalds"
curl -X POST http://$SERVER:$PORT/restaurants/McDonalds
echo " "
echo "curl -X POST http://$SERVER:$PORT/restaurants/BurgerKing"
curl -X POST http://$SERVER:$PORT/restaurants/BurgerKing
echo " "
echo "curl -X POST http://$SERVER:$PORT/restaurants"
curl -X POST http://$SERVER:$PORT/restaurants
echo " "
echo "curl -X DELETE http://$SERVER:$PORT/restaurants/NafNaf"
curl -X DELETE http://$SERVER:$PORT/restaurants/NafNaf
echo " "
echo "curl -X DELETE http://$SERVER:$PORT/restaurants/McDonalds"
curl -X DELETE http://$SERVER:$PORT/restaurants/McDonalds
echo " "
echo "curl -X POST http://$SERVER:$PORT/restaurants"
curl -X POST http://$SERVER:$PORT/restaurants
echo " "
echo "curl -X GET http://$SERVER:$PORT/restaurants/Chipotle"
curl -X GET http://$SERVER:$PORT/restaurants/Chipotle
echo " "
echo "curl -X POST http://$SERVER:$PORT/restaurants/Chipotle/menus/Breakfast"
curl -X POST http://$SERVER:$PORT/restaurants/Chipotle/menus/Breakfast
echo " "
echo "curl -X POST http://$SERVER:$PORT/restaurants/Chipotle/menus/Lunch"
curl -X POST http://$SERVER:$PORT/restaurants/Chipotle/menus/Lunch
echo " "
echo "curl -X POST http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner"
curl -X POST http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner
echo " "
echo "curl -X GET http://$SERVER:$PORT/restaurants/Chipotle/menus"
curl -X GET http://$SERVER:$PORT/restaurants/Chipotle/menus
echo " "
echo "curl -X DELETE http://$SERVER:$PORT/restaurants/Chipotle/menus/Breakfast"
curl -X DELETE http://$SERVER:$PORT/restaurants/Chipotle/menus/Breakfast
echo " "
echo "curl -X GET http://$SERVER:$PORT/restaurants/Chipotle/menus"
curl -X GET http://$SERVER:$PORT/restaurants/Chipotle/menus
echo " "
echo "curl -X POST http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner/menuitems/Burrito/Medium/20.00"
curl -X POST http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner/menuitems/Burrito/Medium/20.00
echo " "
echo "curl -X POST http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner/menuitems/BeefBowl/Large/5.99"
curl -X POST http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner/menuitems/BeefBowl/Large/5.99
echo " "
echo "curl -X GET http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner"
curl -X GET http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner
echo " "
echo "curl -X GET http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner/menuitems"
curl -X GET http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner/menuitems
echo " "
echo "curl -X GET http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner/menuitems/Burrito"
curl -X GET http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner/menuitems/Burrito
echo " "
echo "curl -X GET http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner/menuitems/BeefBowl"
curl -X GET http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner/menuitems/BeefBowl
echo " "
echo "curl -X DELETE http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner/menuitems/BeefBowl"
curl -X DELETE http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner/menuitems/BeefBowl
echo " "
echo "curl -X GET http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner/menuitems"
curl -X GET http://$SERVER:$PORT/restaurants/Chipotle/menus/Dinner/menuitems
echo " "
