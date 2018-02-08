from flask import Flask, url_for
from flask_caching import Cache
from flask import Response
import logging
import json
import collections
import pymysql
from databasemanager import DatabaseManager
import time

app = Flask(__name__)

file_handler = logging.FileHandler('restaurants.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
cache = Cache(app,config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

@app.route('/cachetest')
@cache.cached(timeout=10)
def test():
	return time.ctime()
 
@app.route('/')
def api_root():
    return 'Hello and Welcome to my Restaurant API'


####################################################################restaurants####################
@app.route('/restaurants',methods = ['GET','POST'])
@cache.cached(timeout=60)
def api_restaurants():
	restaurant_map = DatabaseManager.getRestaurants(app.logger)
	objects_list = []
	for j, k in restaurant_map.iteritems():
		d = collections.OrderedDict()
		d['id'] = str(j)
		d['name'] = str(k)
		objects_list.append(d)
	js = json.dumps(objects_list)
	resp = Response(js, status=200, mimetype='application/json')
	return resp


@app.route('/restaurants/<restaurantname>',methods = ['POST'])
def api_add_restaurant(restaurantname):
	with app.app_context():
		cache.clear()
	id = DatabaseManager.addRestaurant(app.logger,restaurantname)
	result = 'Restaurant added. URL ' + url_for('api_restaurants') + '/' + restaurantname
	return result

	
@app.route('/restaurants/<restaurantname>',methods = ['GET'])
@cache.cached(timeout=60)
def api_get_restaurants(restaurantname):
	restaurant_map = DatabaseManager.getRestaurants(app.logger)
	result = 'Uknown restaurant name does not exist'
	if restaurantname in restaurant_map.values():
		result = 'Restaurant name is ' + restaurantname + ' and exists in the system'
	return result

@app.route('/restaurants/<restaurantname>',methods = ['DELETE'])
def api_del_restaurant(restaurantname):
	with app.app_context():
                cache.clear()
	ret = DatabaseManager.delRestaurant(app.logger,restaurantname)
	result = 'Unable to delete restaurant named ' + restaurantname
	if ret:
		result = 'Successfully deleted restaurant named ' + restaurantname
	return result

#############################################################################################menus##

@app.route('/restaurants/<restaurantname>/menus',methods = ['GET','POST'])
@cache.cached(timeout=60)
def api_restaurant_menus(restaurantname):
        menu_map = DatabaseManager.getRestaurantMenus(app.logger,restaurantname)
        objects_list = []
        for j, k in menu_map.iteritems():
                d = collections.OrderedDict()
                d['id'] = str(j)
                d['name'] = str(k)
                objects_list.append(d)
        js = json.dumps(objects_list)
        resp = Response(js, status=200, mimetype='application/json')
        return resp


@app.route('/restaurants/<restaurantname>/menus/<menuname>',methods = ['POST'])
def api_add_restaurant_menu(restaurantname,menuname):
	with app.app_context():
                cache.clear()
        id = DatabaseManager.addRestaurantMenu(app.logger,restaurantname,menuname)
	result = 'Restaurant does not exist!'
	restaurant_map = DatabaseManager.getRestaurants(app.logger)
	if restaurantname in restaurant_map.values():
	        result = 'Menu added. URL ' + url_for('api_restaurant_menus',restaurantname = restaurantname) + '/' + menuname
        return result


@app.route('/restaurants/<restaurantname>/menus/<menuname>',methods = ['GET'])
@cache.cached(timeout=60)
def api_get_restaurant_menu(restaurantname,menuname):
        menu_map = DatabaseManager.getRestaurantMenus(app.logger,restaurantname)
        result = 'Unknown menu, name does not exist'
        if menuname in menu_map.values():
                result = 'Menu name is ' + menuname + ' from restaurant ' + restaurantname +' and exists in the system'
        return result

@app.route('/restaurants/<restaurantname>/menus/<menuname>',methods = ['DELETE'])
def api_del_restaurant_menu(restaurantname,menuname):
	with app.app_context():
                cache.clear()
	result = 'Menu not found'
	menu_map = DatabaseManager.getRestaurantMenus(app.logger,restaurantname)
        if menuname in menu_map.values():
        	ret = DatabaseManager.delRestaurantMenu(app.logger,restaurantname,menuname)
        	result = 'Unable to delete menu named ' + menuname + 'from restaurant named ' + restaurantname
		if ret:
                	result = 'Successfully deleted menu named ' + menuname + ' from restaurant named ' + restaurantname

        return result


################################################################################################### menu items #################################################################


@app.route('/restaurants/<restaurantname>/menus/<menuname>/menuitems',methods = ['GET','POST'])
@cache.cached(timeout=60)
def api_restaurant_menu_items(restaurantname,menuname):
        menuitems_map = DatabaseManager.getRestaurantMenuItems(app.logger,restaurantname,menuname)
        objects_list = []
        for j, k in menuitems_map.iteritems():
                d = collections.OrderedDict()
                d['id'] = str(j)
                d['name'] = str(k)
                objects_list.append(d)
        js = json.dumps(objects_list)
        resp = Response(js, status=200, mimetype='application/json')
        return resp


@app.route('/restaurants/<restaurantname>/menus/<menuname>/menuitems/<menuitemname>/<size>/<price>',methods = ['POST'])
def api_add_restaurant_menu_item(restaurantname,menuname,menuitemname,size,price):
	with app.app_context():
                cache.clear()
        id = DatabaseManager.addRestaurantMenuItem(app.logger,restaurantname,menuname,menuitemname,size,price)
        result = 'Restaurant does not exist!'
	restaurant_map = DatabaseManager.getRestaurants(app.logger)
	if restaurantname in restaurant_map.values():
        	result = 'Menu does not exist for ' + menuname
		menu_map = DatabaseManager.getRestaurantMenus(app.logger,restaurantname)
        	if menuname in menu_map.values():
                	result = 'Menu item added. URL ' + url_for('api_restaurant_menus',restaurantname = restaurantname) + '/' + menuname
        return result


@app.route('/restaurants/<restaurantname>/menus/<menuname>/menuitems/<menuitemname>',methods = ['GET'])
@cache.cached(timeout=60)
def api_get_restaurant_menu_item(restaurantname,menuname,menuitemname):
        menuitems_map = DatabaseManager.getRestaurantMenuItem(app.logger,restaurantname,menuname,menuitemname)
	objects_list = []
	for j, k in menuitems_map.iteritems():
		d = collections.OrderedDict()
		d['id'] = str(j)
		d['name'] = str(k[1])
		d['size'] = str(k[2])
		d['price'] = str(k[3])
		objects_list.append(d)
	js = json.dumps(objects_list)
	resp = Response(js, status=200, mimetype='application/json')
	return resp	


@app.route('/restaurants/<restaurantname>/menus/<menuname>/menuitems/<menuitemname>',methods = ['DELETE'])
def api_del_restaurant_menu_item(restaurantname,menuname,menuitemname):
	with app.app_context():
                cache.clear()
        result = 'Menuitem not found'
        menuitem_map = DatabaseManager.getRestaurantMenuItems(app.logger,restaurantname,menuname)
        if menuitemname in menuitem_map.values():
                ret = DatabaseManager.delRestaurantMenuItem(app.logger,restaurantname,menuname,menuitemname)
                result = 'Unable to delete menuitem named ' + menuitemname + 'from restaurant named ' + restaurantname + 'in menu ' + menuname
                if ret:
                        result = 'Successfully deleted menu item named ' + menuitemname + ' from restaurant named ' + restaurantname + ' in menu named ' + menuname

        return result











if __name__ == '__main__':
    app.run(host='ec2-13-58-211-147.us-east-2.compute.amazonaws.com')
