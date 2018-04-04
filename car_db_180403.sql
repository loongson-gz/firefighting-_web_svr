/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50548
Source Host           : localhost:3306
Source Database       : car_db

Target Server Type    : MYSQL
Target Server Version : 50548
File Encoding         : 65001

Date: 2018-04-03 12:12:16
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_car
-- ----------------------------
DROP TABLE IF EXISTS `t_car`;
CREATE TABLE `t_car` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `plate_num` varchar(255) NOT NULL,
  `car_type` varchar(255) DEFAULT NULL,
  `member_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`plate_num`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `t_car_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `t_member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of t_car
-- ----------------------------
INSERT INTO `t_car` VALUES ('2', 'WJ粤8003X', '豪士科A类泡沫消防车', '2');
INSERT INTO `t_car` VALUES ('3', 'WJ粤6276X', 'VD泡沫水罐消防车', '1');

-- ----------------------------
-- Table structure for t_car_compent
-- ----------------------------
DROP TABLE IF EXISTS `t_car_compent`;
CREATE TABLE `t_car_compent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `car_id` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `qr_code` varchar(255) NOT NULL,
  PRIMARY KEY (`id`,`qr_code`),
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of t_car_compent
-- ----------------------------
INSERT INTO `t_car_compent` VALUES ('1', '2', '行车记录仪', '0200106003');
INSERT INTO `t_car_compent` VALUES ('2', '2', '发动机', '0200105003');
INSERT INTO `t_car_compent` VALUES ('3', '2', '电气设备、灯光、喇叭、雨刮', '0200106003');
INSERT INTO `t_car_compent` VALUES ('4', '2', '各仪表工作状态、工作指示、照明', '0200106003');
INSERT INTO `t_car_compent` VALUES ('5', '2', '转向系统、制动器', '0200108003');
INSERT INTO `t_car_compent` VALUES ('6', '2', '燃油存量', '0200105003');
INSERT INTO `t_car_compent` VALUES ('7', '2', '油液、水、电和灭火器是否充足', '0200108003');
INSERT INTO `t_car_compent` VALUES ('8', '2', '前轮胎', '0200101003');
INSERT INTO `t_car_compent` VALUES ('9', '2', '水泵系统', '0200108003');
INSERT INTO `t_car_compent` VALUES ('10', '2', '车容', '0200101003');
INSERT INTO `t_car_compent` VALUES ('11', '2', '器材门安全锁装置、室内消防物有无紧固', '0200107003');
INSERT INTO `t_car_compent` VALUES ('12', '2', '车顶消防物有无松脱紧固', '0200107003');
INSERT INTO `t_car_compent` VALUES ('13', '3', '行车记录仪', '0200106276');
INSERT INTO `t_car_compent` VALUES ('14', '3', '发动机', '0200105276');
INSERT INTO `t_car_compent` VALUES ('15', '3', '电气设备、灯光、喇叭、雨刮', '0200106276');
INSERT INTO `t_car_compent` VALUES ('16', '3', '各仪表工作状态、工作指示、照明', '0200106276');
INSERT INTO `t_car_compent` VALUES ('17', '3', '转向系统、制动器', '0200108276');
INSERT INTO `t_car_compent` VALUES ('18', '3', '燃油存量', '0200106276');
INSERT INTO `t_car_compent` VALUES ('19', '3', '油液、水、电和灭火器是否充足', '0200106276');
INSERT INTO `t_car_compent` VALUES ('20', '3', '前轮胎', '0200101276');
INSERT INTO `t_car_compent` VALUES ('21', '3', '水泵系统', '0200108276');
INSERT INTO `t_car_compent` VALUES ('22', '3', '车容', '0200101276');
INSERT INTO `t_car_compent` VALUES ('23', '3', '器材门安全锁装置、室内消防物有无紧固', '0200107276');
INSERT INTO `t_car_compent` VALUES ('24', '3', '车顶消防物有无松脱紧固', '0200107276');
INSERT INTO `t_car_compent` VALUES ('25', '2', '后轮胎', '0200102003');
INSERT INTO `t_car_compent` VALUES ('26', '2', '左轮胎', '0200103003');
INSERT INTO `t_car_compent` VALUES ('27', '2', '右轮胎', '0200104003');
INSERT INTO `t_car_compent` VALUES ('28', '3', '后轮胎', '0200102276');
INSERT INTO `t_car_compent` VALUES ('29', '3', '左轮胎', '0200103276');
INSERT INTO `t_car_compent` VALUES ('30', '3', '右轮胎', '0200104276');

-- ----------------------------
-- Table structure for t_member
-- ----------------------------
DROP TABLE IF EXISTS `t_member`;
CREATE TABLE `t_member` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `finger_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `department` varchar(255) DEFAULT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`finger_id`),
  KEY `id` (`id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `t_member_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `t_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of t_member
-- ----------------------------
INSERT INTO `t_member` VALUES ('1', '103', '张三', '三班', '1');
INSERT INTO `t_member` VALUES ('2', '203', '王五', '天河中队', '2');
INSERT INTO `t_member` VALUES ('3', '66', '李四', '二班', '3');

-- ----------------------------
-- Table structure for t_param
-- ----------------------------
DROP TABLE IF EXISTS `t_param`;
CREATE TABLE `t_param` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `finger_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of t_param
-- ----------------------------
INSERT INTO `t_param` VALUES ('1', '0');

-- ----------------------------
-- Table structure for t_record
-- ----------------------------
DROP TABLE IF EXISTS `t_record`;
CREATE TABLE `t_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `car_id` int(11) NOT NULL,
  `member_id` int(11) NOT NULL,
  `compent_id` int(11) NOT NULL,
  `check_status` tinyint(1) unsigned zerofill NOT NULL DEFAULT '0',
  `compent_status` tinyint(1) NOT NULL DEFAULT '1',
  `desc` varchar(255) DEFAULT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`id`),
  KEY `car_id` (`car_id`),
  KEY `member_id` (`member_id`),
  KEY `compent_id` (`compent_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of t_record
-- ----------------------------

-- ----------------------------
-- Table structure for t_record_leader
-- ----------------------------
DROP TABLE IF EXISTS `t_record_leader`;
CREATE TABLE `t_record_leader` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `record_mechanic_id` int(11) NOT NULL,
  `status` int(255) NOT NULL DEFAULT '0',
  `desc` varchar(255) DEFAULT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`id`),
  KEY `record_check_id` (`record_mechanic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of t_record_leader
-- ----------------------------

-- ----------------------------
-- Table structure for t_record_mechanic
-- ----------------------------
DROP TABLE IF EXISTS `t_record_mechanic`;
CREATE TABLE `t_record_mechanic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `record_id` int(11) NOT NULL,
  `status` varchar(255) NOT NULL DEFAULT '0',
  `desc` varchar(255) DEFAULT NULL,
  `date` date NOT NULL DEFAULT '0000-00-00',
  `time` time DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `record_id` (`record_id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of t_record_mechanic
-- ----------------------------

-- ----------------------------
-- Table structure for t_role
-- ----------------------------
DROP TABLE IF EXISTS `t_role`;
CREATE TABLE `t_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `level` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `title` (`name`),
  KEY `level` (`level`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of t_role
-- ----------------------------
INSERT INTO `t_role` VALUES ('1', '司机', '1');
INSERT INTO `t_role` VALUES ('2', '维修技师', '2');
INSERT INTO `t_role` VALUES ('3', '值班领导', '3');

-- ----------------------------
-- Table structure for t_task
-- ----------------------------
DROP TABLE IF EXISTS `t_task`;
CREATE TABLE `t_task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `car_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `status` int(11) unsigned zerofill NOT NULL DEFAULT '00000000000',
  PRIMARY KEY (`id`),
  KEY `car_id` (`car_id`),
  CONSTRAINT `t_task_ibfk_1` FOREIGN KEY (`car_id`) REFERENCES `t_car` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of t_task
-- ----------------------------

-- ----------------------------
-- Table structure for t_task_month
-- ----------------------------
DROP TABLE IF EXISTS `t_task_month`;
CREATE TABLE `t_task_month` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `compent_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `compent_id` (`compent_id`),
  CONSTRAINT `t_task_month_ibfk_1` FOREIGN KEY (`compent_id`) REFERENCES `t_car_compent` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of t_task_month
-- ----------------------------

-- ----------------------------
-- Table structure for t_task_normal
-- ----------------------------
DROP TABLE IF EXISTS `t_task_normal`;
CREATE TABLE `t_task_normal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `compent_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `compent_id` (`compent_id`),
  CONSTRAINT `t_task_normal_ibfk_1` FOREIGN KEY (`compent_id`) REFERENCES `t_car_compent` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of t_task_normal
-- ----------------------------

-- ----------------------------
-- Table structure for t_task_week
-- ----------------------------
DROP TABLE IF EXISTS `t_task_week`;
CREATE TABLE `t_task_week` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `compent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `compent_id` (`compent_id`),
  CONSTRAINT `t_task_week_ibfk_1` FOREIGN KEY (`compent_id`) REFERENCES `t_car_compent` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of t_task_week
-- ----------------------------
