-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pollution-db` DEFAULT CHARACTER SET utf8 ;
USE `pollution-db` ;

-- -----------------------------------------------------
-- Table `mydb`.`Stations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pollution-db`.`Stations` (
  `Station_Id` INT NOT NULL,
  `Location` VARCHAR(48) NULL,
  `Geo_Point_2d` VARCHAR(48) NULL,
  PRIMARY KEY (`Station_Id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Readings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pollution-db`.`Readings` (
  `Reading_Id` INT NOT NULL,
  `DateTime` DATETIME NULL,
  `NOx` FLOAT NULL,
  `NO2` FLOAT NULL,
  `NO` FLOAT NULL,
  `PM10` FLOAT NULL,
  `NVPM10` FLOAT NULL,
  `VPM10` FLOAT NULL,
  `NVPM2.5` FLOAT NULL,
  `PM2.5` FLOAT NULL,
  `VPM2.5` FLOAT NULL,
  `CO` FLOAT NULL,
  `O3` FLOAT NULL,
  `SO2` FLOAT NULL,
  `Temperature` FLOAT NULL,
  `RH` INT NULL,
  `AirPressure` INT NULL,
  `DateStart` DATETIME NULL,
  `DateEnd` DATETIME NULL,
  `Current` TEXT(5) NULL,
  `InstrumentType` VARCHAR(32) NULL,
  `Stations_Station_Id` INT NOT NULL,
  PRIMARY KEY (`Reading_Id`),
  INDEX `fk_Readings_Stations_idx` (`Stations_Station_Id` ASC),
  CONSTRAINT `fk_Readings_Stations`
    FOREIGN KEY (`Stations_Station_Id`)
    REFERENCES `pollution-db`.`Stations` (`Station_Id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Schema`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pollution-db`.`Schema` (
  `Measure` VARCHAR(32) NOT NULL,
  `Description` VARCHAR(24) NULL,
  `Unit` VARCHAR(24) NULL,
  PRIMARY KEY (`Measure`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
