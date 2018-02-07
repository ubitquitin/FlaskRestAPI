import pymysql

class Constants:

	MYSQLSERVER = "localhost"
	MYSQLUSER = "ec2-user"
	MYSQLPASS = "Toragpwns96"

class DatabaseManager:
	
	@staticmethod
	def connect_to_db(logger,server=Constants.MYSQLSERVER,user=Constants.MYSQLUSER,password=Constants.MYSQLPASS):
		try:
			mysqlconnection = pymysql.connect(server,user,password);
			logger.info("Connected to MySQL db server [" + server + "]")
		except Exception as e:
			logger.error("ERROR ALERT --> Connection Error to reportsdb")
			exit(1)
		return mysqlconnection





	@staticmethod
	def getRestaurants(logger):
		logger.info("Getting a list of Restaurants from DB")
		mysqlconnection = DatabaseManager.connect_to_db(logger)
		restaurant_map = dict()
		sql = "SELECT id, name from RestData.restaurants"
		logger.info(sql)
		cursor = mysqlconnection.cursor()
		try:
			cursor.execute(sql)
			for row in cursor:
				restaurant_map[str(row[0])] = str(row[1])
			logger.info("Found [%d] restaurants and [%d] entries in restaurant_map dictionary" % (cursor.rowcount,len(restaurant_map)))
			cursor.close()
		except Exception as e:
			logger.error("ERROR ALERT --> Error fetching restaurants " + str(e))
		DatabaseManager.disconnect_from_db(logger,mysqlconnection)
		return restaurant_map
	
	@staticmethod
	def addRestaurant(logger,name):
		logger.info("Adding " + name + "to restaurant list")
		mysqlconnection = DatabaseManager.connect_to_db(logger)
		sql = "INSERT into RestData.restaurants(name) VALUES ('" + name + "')"
		logger.info(sql)
		cursor = mysqlconnection.cursor()
		id = 0
		try:
			cursor.execute(sql)
			if cursor.lastrowid:
				id = str(cursor.lastrowid)
				logger.info('id='+ id)
				mysqlconnection.commit()
		except Exception as e:
			logger.error("ERROR ALERT --> Error adding restaurant " + str(e))
		cursor.close()
		DatabaseManager.disconnect_from_db(logger,mysqlconnection)
		return id
		

	@staticmethod
	def delRestaurant(logger,name):
		mysqlconnection = DatabaseManager.connect_to_db(logger)
		sql = "DELETE FROM RestData.restaurants where name = '" + name + "'"
		logger.info(sql)
		cursor = mysqlconnection.cursor()
		result = False
		try:
			cursor.execute(sql)
			mysqlconnection.commit()
			result = True

		except Exception as e:
			logger.error("ERROR ALERT --> Error deleting restaurant " + str(e))
		cursor.close()
		DatabaseManager.disconnect_from_db(logger,mysqlconnection)
		return result					
	
        @staticmethod
        def getRestaurantMenus(logger,restaurantname):
                logger.info("Getting a list of Menus from Restaurant " + restaurantname)
                mysqlconnection = DatabaseManager.connect_to_db(logger)
                menu_map = dict()
                sql = "SELECT A.id,A.name from RestData.menus A, RestData.restaurants B where B.name='" + restaurantname +"' and B.id = A.restaurantid"
                logger.info(sql)
                cursor = mysqlconnection.cursor()
                try:
                        cursor.execute(sql)
                        for row in cursor:
                                menu_map[str(row[0])] = str(row[1])
                        logger.info("Found [%d] restaurants and [%d] entries in restaurant_map dictionary" % (cursor.rowcount,len(menu_map)))
                        cursor.close()
                except Exception as e:
                        logger.error("ERROR ALERT --> Error fetching menus " + str(e))
                DatabaseManager.disconnect_from_db(logger,mysqlconnection)
                return menu_map

        @staticmethod
        def addRestaurantMenu(logger,restaurantname,menuname):
                logger.info("Adding menu [" + menuname + "] for restaurant [" + restaurantname + "] to db")
                mysqlconnection = DatabaseManager.connect_to_db(logger)
                sql = "INSERT INTO RestData.menus (name,restaurantid) SELECT '" + menuname + "', id from RestData.restaurants where name = '" + restaurantname + "'"
                logger.info(sql)
                cursor = mysqlconnection.cursor()
                id = 0
                try:
                        cursor.execute(sql)
                        if cursor.lastrowid:
                                id = str(cursor.lastrowid)
                                logger.info('id='+ id)
                                mysqlconnection.commit()
                except Exception as e:
                        logger.error("ERROR ALERT --> Error adding menu " + str(e))
                cursor.close()
                DatabaseManager.disconnect_from_db(logger,mysqlconnection)
                return id


        @staticmethod
        def delRestaurantMenu(logger,restaurantname,menuname):
                mysqlconnection = DatabaseManager.connect_to_db(logger)
                sql = "DELETE FROM RestData.menus where name = '" + menuname + "' AND restaurantid = (select id from RestData.restaurants where name = '" + restaurantname + "')"
                logger.info(sql)
                cursor = mysqlconnection.cursor()
                result = False
                try:
                        cursor.execute(sql)
                        mysqlconnection.commit()
                        result = True

                except Exception as e:
                        logger.error("ERROR ALERT --> Error deleting menu " + str(e))
                cursor.close()
                DatabaseManager.disconnect_from_db(logger,mysqlconnection)
                return result


 	@staticmethod
        def getRestaurantMenuItems(logger,restaurantname,menuname):
                logger.info("Getting a list of MenuItems from Manu " + menuname + " of restaurant " + restaurantname)
                mysqlconnection = DatabaseManager.connect_to_db(logger)
                menuitems_map = dict()
                sql = "SELECT C.id, C.name from RestData.restaurants A, RestData.menus B, RestData.menuitems C where A.name='" + restaurantname +"' and A.id = B.restaurantid and B.name = '" + menuname + "' and B.id = C.menuid"
                logger.info(sql)
                cursor = mysqlconnection.cursor()
                try:
                        cursor.execute(sql)
                        for row in cursor:
                                menuitems_map[str(row[0])] = str(row[1])
                        logger.info("Found [%d] menuitems and [%d] entries in menuitems_map dictionary" % (cursor.rowcount,len(menuitems_map)))
                        cursor.close()
                except Exception as e:
                        logger.error("ERROR ALERT --> Error fetching menu items " + str(e))
                DatabaseManager.disconnect_from_db(logger,mysqlconnection)
                return menuitems_map

        @staticmethod
        def addRestaurantMenuItem(logger,restaurantname,menuname,menuitemname,size,price):
                logger.info("Adding menuitem [" + menuitemname + "] from menu [" + menuname +"] for restaurant [" + restaurantname + "] to db")
                mysqlconnection = DatabaseManager.connect_to_db(logger)
                sql = "INSERT INTO RestData.menuitems (name,size,price,menuid) "
		sql += "SELECT '" + menuitemname + "', '" + size + "', '" + price + "', A.id"  
		sql += " from RestData.menus A "
		sql += " where A.name = '" + menuname + "' "
		sql += " and A.restaurantid = (select B.id from RestData.restaurants B where B.name = '" + restaurantname + "')"

                logger.info(sql)
                cursor = mysqlconnection.cursor()
                id = 0
                try:
                        cursor.execute(sql)
                        if cursor.lastrowid:
                                id = str(cursor.lastrowid)
                                logger.info('id='+ id)
                                mysqlconnection.commit()
                except Exception as e:
                        logger.error("ERROR ALERT --> Error adding menuitem " + str(e))
                cursor.close()
                DatabaseManager.disconnect_from_db(logger,mysqlconnection)
                return id


        @staticmethod
        def delRestaurantMenuItem(logger,restaurantname,menuname,menuitemname):
                mysqlconnection = DatabaseManager.connect_to_db(logger)
                sql = "DELETE FROM RestData.menuitems where name = '" + menuitemname + "' AND menuid = (select id from RestData.menus where name = '" + menuname + "')"
                logger.info(sql)
                cursor = mysqlconnection.cursor()
                result = False
                try:
                        cursor.execute(sql)
                        mysqlconnection.commit()
                        result = True

                except Exception as e:
                        logger.error("ERROR ALERT --> Error deleting menuitem " + str(e))
                cursor.close()
                DatabaseManager.disconnect_from_db(logger,mysqlconnection)
                return result

	@staticmethod
        def getRestaurantMenuItem(logger,restaurantname, menuname, menuitemname):
    	    	logger.info("Getting menuitem for restaurant " + restaurantname + " and menu " + menuname + " and menuitem " + menuitemname + " from DB")
            	mysqlconnection = DatabaseManager.connect_to_db(logger)
        	menuitems_map = dict()
        	sql = "SELECT C.id, C.name, C.size, C.price from RestData.restaurants A, RestData.menus B, RestData.menuitems C "
        	sql += "where A.name = '" + restaurantname + "' and A.id = B.restaurantid and B.name = '" + menuname + "' and B.id = C.menuid and C.name = '" + menuitemname + "'"
        	logger.info(sql)
        	cursor = mysqlconnection.cursor()
        	try:
            		cursor.execute(sql)
            		for row in cursor:
                		menuitems_map[str(row[0])] = row
            		logger.info("Found [%d] menuitems and [%d] entries in menuitems_map dictionary" % (cursor.rowcount,len(menuitems_map)))
            		cursor.close()
        	except Exception as e:
            		logger.error("ERROR ALERT --> Error fetching menuitem " + str(e))
        	DatabaseManager.disconnect_from_db(logger,mysqlconnection)
        	return menuitems_map

	@staticmethod
	def disconnect_from_db(logger,mysqlconnection):
		mysqlconnection.close()
		logger.info("Disconnected from %s" % Constants.MYSQLSERVER)
