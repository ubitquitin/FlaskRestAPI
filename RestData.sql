DROP TABLE IF EXISTS RestData.menuitems;
DROP TABLE IF EXISTS RestData.menus;
DROP TABLE IF EXISTS RestData.restaurants;

CREATE TABLE RestData.restaurants (
  id bigint(20) NOT NULL AUTO_INCREMENT,
  name varchar(100),
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=latin1;

CREATE TABLE RestData.menus (
  id bigint(20) NOT NULL AUTO_INCREMENT,
  name varchar(100),
  restaurantid bigint(20),
PRIMARY KEY (`id`),
FOREIGN KEY (restaurantid) REFERENCES restaurants(id) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2000 DEFAULT CHARSET=latin1;

CREATE TABLE RestData.menuitems (
  id bigint(20) NOT NULL AUTO_INCREMENT,
  menuid bigint(20),
  name varchar(100),
  size varchar(30),
  price double,
PRIMARY KEY (id),
FOREIGN KEY (menuid) REFERENCES menus(id) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3000 DEFAULT CHARSET=latin1;


